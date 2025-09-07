

# Add product URLs here to extract data from them
EXT_PRODUCT_URL = [ "https://www.newegg.com/amd-ryzen-7-9000-series-ryzen-7-9800x3d-granite-ridge-zen-5-socket-am5-desktop-cpu-processor/p/N82E16819113877"
]
PRODUCT_HEADERS = {
  'Cookie': 'NID=0M4M72724M0M6I9D2Q; NVTC=248326808.0001.3abb3916e.1757167025.1757232764.1757235669.4; NV_NVTCTIMESTAMP=1757235669; __cf_bm=3jSN8dxr3GqtTw1waPHsiKqguYmEXRhLTbN0fJJSK_M-1757235668-1.0.1.1-0cBnoj3iuAFUmNdptO_S0b2bj3dxYYggGm5.m.mKxQ85X8ylxgqk.PbObGv4qdiIQbAIQj30mnZOub7v_eRYcr_aTsCL5CP6VjmhoOV_OMQ; NE_STC_V1=4afda3da93413bdc7cde656d136df10b66488323b34a34dc736a0305f44a3f98047bd687'
}

PRODUCT_REVIEW_URL = "https://www.newegg.com/product/api/ProductReview"

PRODUCT_HEADERS_REVIEW_HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://www.newegg.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'Cookie': 'YOUR_COOKIES_HERE'
}

DB_NAME = "newegg_products.db"