import asyncio
import aiohttp
from flask import jsonify, request

from . import deal_bp
from app import app
from .discover import DiscoverItCashBack

async def fetch_from_card_coupon_sv(session, url, data):
    """
    Asynchronously fetch data from the card coupon service.

    Args:
        session (aiohttp.ClientSession): An aiohttp client session.
        url (str): The URL to fetch data from.
        data (dict): Data to send with the request.

    Returns:
        dict: JSON response from the card coupon service.
    """
    headers = {
        'User-Agent': 'My Python Script',
    }
    async with session.get(url, data=data, headers=headers) as response:
        return await response.json()

async def get_available_coupons_async(req_data, data):
    """
    Asynchronously fetch available coupons from the card-coupon-sv.

    Args:
        req_data (dict): Request data from the client.

    Returns:
        list: List of available coupons.
    """
    
    

    async with aiohttp.ClientSession() as session:
        url = f"{app.config['CARD_COUPON_SV_URL']}/api/coupon/get_available_coupons_with_constraints"
        async with session.get(url, data=data) as response:
            response_data = await response.json()
            return response_data.get("getAvailableCouponsWithConstraintsResponse", [])

@deal_bp.route('/discover/discover-it-cash-back/top-deals', methods=['POST'])
def add_top_deals_job_discover_dicb():
    """
    Endpoint to get top deals asynchronously.

    Returns:
        JSON response: Top deals response.
    """
    req_data = request.json
    # Fetch available coupons asynchronously
    data = {
        "card_id": 1,
        "datetime": req_data["_datetime"],
        "category": req_data.get("category", 0),
        "payment": req_data.get("payment", 0),
        "merchant": req_data.get("merchant", 0)
    }

    available_coupons = asyncio.run(get_available_coupons_async(req_data, data))

    top_deals = DiscoverItCashBack.get_top_deals(
        req_data["quarterly_special_usage"], 
        req_data["amount"], 
        available_coupons
    )
    return jsonify({"getTopDealsResponse": top_deals})
    # except Exception as e:
    #     return jsonify({"error": str(e)})
