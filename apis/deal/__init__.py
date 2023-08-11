from flask import Blueprint

# Create a Blueprint for the coupon routes
deal_bp = Blueprint('deal', __name__)

# Import the coupon routes to register the blueprint
from . import routes
