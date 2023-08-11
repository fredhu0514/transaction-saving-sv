import json
import pprint
import requests
from datetime import datetime

# Replace this with the URL of your Flask server
BASE_URL = 'http://172.24.0.2:5000'

def get_deals():
    headers = {
        'User-Agent': 'My Python Script',
        'Content-Type': 'application/json'
    }

    # Send a POST request to the API to add the coupon
    url = f"{BASE_URL}/api/deal/discover/discover-it-cash-back/top-deals"
    data = {
        "amount": 100.000,
        "quarterly_special_usage": 0.000,
        "_datetime": datetime.now().isoformat(),
        "category": 1,
        "payment": 0,
        "merchant": 0
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)

    try:
        response.raise_for_status()  # Check if the request was successful (status code 200-299)
        req_data = response.json()['getTopDealsResponse']
        pprint.pprint(req_data)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)  # Print the raw response content
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")

if __name__ == '__main__':
    get_deals()
