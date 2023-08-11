from flask import Flask
from config import app_config

def create_app():
    # Create and configure the Flask app instance
    app = Flask(__name__)
    app.config.from_object(app_config)

    # Register the blueprints for different resources
    from apis.deal import deal_bp

    app.register_blueprint(deal_bp, url_prefix='/api/deal')

    return app

# Create the Flask app
app = create_app()

if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", port=5000)
