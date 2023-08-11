import os

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = "transaction-saving-db/db_transaction.sqlite3"
    CARD_COUPON_SV_URL = 'http://192.168.1.156:5500'

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    CARD_COUPON_SV_URL = 'http://192.168.1.156:5555'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    CARD_COUPON_SV_URL = 'http://192.168.1.156:5050'

# Determine the current environment based on the 'FLASK_ENV' environment variable
if os.environ.get("FLASK_ENV") == "production":
    app_config = ProductionConfig()
elif os.environ.get("FLASK_ENV") == "testing":
    app_config = TestingConfig()
elif os.environ.get("FLASK_ENV") == "development":
    app_config = DevelopmentConfig()
