import requests
import json
import urllib.parse
from config import PRODUCT_HEADERS_REVIEW_HEADERS,PRODUCT_REVIEW_URL
def fetch_all_customer_reviews(ItemGroupID, ItemNumber, WebItemNumber):
    if not all([ItemGroupID, ItemNumber, WebItemNumber]):
        return []

    base_url = PRODUCT_REVIEW_URL
    all_reviews = []
    page_index = 1
    per_page = 100

    base_payload = {
        "IsGetSummary": True,
        "IsGetTopReview": False,
        "IsGetItemProperty": False,
        "IsGetAllReviewCategory": False,
        "IsSearchWithoutStatistics": False,
        "IsGetFilterCount": False,
        "IsGetFeatures": True,
        "SearchProperty": {
            "CombineGroup": 2,
            "FilterDate": 0,
            "IsB2BExclusiveReviews": False,
            "IsBestCritialReview": False,
            "IsBestFavorableReview": False,
            "IsItemMarkOnly": True,
            "IsProductReviewSearch": True,
            "IsPurchaserReviewOnly": False,
            "IsResponsiveSite": False,
            "IsSmartPhone": False,
            "IsVendorResponse": False,
            "IsVideoReviewOnly": False,
            "ItemGroupId": ItemGroupID,
            "ItemNumber": ItemNumber,
            "NeweggItemNumber": WebItemNumber,
            "PageIndex": 1,  # will update in loop
            "PerPageItemCount": per_page,
            "RatingReviewDisplayType": 0,
            "ReviewTimeFilterType": 0,
            "RatingType": -1,
            "ReviewType": 3,
            "SearchKeywords": "",
            "SearchLanguage": "",
            "SellerId": "",
            "SortOrderType": 1,
            "SubCategoryId": "343",
            "TransNumber": 0,
            "WithImage": False,
            "HotKeyword": ""
        }
    }

    while True:
        print(f"Extracting reviews from page {page_index}...")
        base_payload["SearchProperty"]["PageIndex"] = page_index
        base_payload["SearchProperty"]["PerPageItemCount"] = per_page

        json_str = json.dumps(base_payload, separators=(',', ':'))
        encoded = urllib.parse.quote(json_str)
        url = f"{base_url}?reviewRequestStr={encoded}"

        response = requests.get(url, headers=PRODUCT_HEADERS_REVIEW_HEADERS)
        if response.status_code != 200:
            print(f"Error fetching page {page_index}: {response.status_code}")
            break

        data = response.json().get("SearchResult", {})
        reviews = data.get("CustomerReviewList", [])

        if not reviews:  # no more reviews
            break

        for review in reviews:
            all_reviews.append({
                "title": review.get("Title"),
                "reviewer_nick_name": review.get("NickName"),
                "rating": review.get("Rating"),
                "reviewer_display_name": review.get("DisplayName"),
                "review_date": review.get("InDate"),
                "reviewer_comments": review.get("Comments"),
                "is_buyer": review.get("IsBuyer"),
            })

        if len(reviews) < 100:  # last page
            break
        page_index += 1  # move to next page

    return all_reviews