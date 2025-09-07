import requests
from parsel import Selector
import json
from config import EXT_PRODUCT_URL,PRODUCT_HEADERS,DB_NAME
from sqlite_db import insert_product_data
from product_reviews import fetch_all_customer_reviews

payload = {}

for url in EXT_PRODUCT_URL:
  try:
    response = requests.get(url, headers=PRODUCT_HEADERS)
  except:
    print("Url -> ", url)
    print("Status code -> ", response.status_code)
    print("Please use proxy to access the website")
    continue

  selector = Selector(response.text)
  json_string = selector.xpath('//*[contains(text(), "window.__initialState__ =")]//text()').get('')
  json_string = json_string.split('window.__initialState__ =')[-1].strip().rstrip(';')    
  json_load = json.loads(json_string)


  try:
      brand = json_load['ItemDetail']['DetailSpecificationObject']['Groups'][1]['Properties'][0]['Value']
  except (IndexError, KeyError, TypeError):
      brand = None


  # product data to be extracted
  extract_data = {
      'title': json_load['ItemDetail']['Description'].get('Title', None),
      'price': json_load['ItemDetail'].get('FinalPrice', None),
      'description': json_load['ItemDetail']['Description'].get('BulletDescription', None),
      'brand': brand,
      "rating_count": json_load['ItemDetail']['Review'].get('HumanRating', None),
      "rating": json_load['ItemDetail']['Review'].get('RatingOneDecimal', None)
  }

  # custorer reviews
  try:
      ItemGroupID = json_load["ItemDetail"]["ItemGroupID"]
      ItemNumber = json_load["ItemDetail"]["Item"]
      WebItemNumber = json_load["SyncLoadReviews"]["SearchResult"]["CustomerReviewList"][0]["WebItemNumber"]

  except (KeyError, IndexError, TypeError) as e:
      ItemGroupID = None
      ItemNumber = None
      WebItemNumber = None

  customers_reviews = fetch_all_customer_reviews(
      ItemGroupID=ItemGroupID,
      ItemNumber=str(ItemNumber),
      WebItemNumber=WebItemNumber
  )

  extract_data['customer_reviews'] = json.dumps(customers_reviews) if customers_reviews else None
  extract_data['total_reviews'] = len(customers_reviews) if customers_reviews else 0

  # insert data into sqlite db
  insert_product_data(DB_NAME, extract_data)


  