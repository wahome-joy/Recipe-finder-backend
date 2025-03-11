import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from app.extensions import db, migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from datetime import timedelta


load_dotenv()

def create_app():
    app = Flask(__name__)

    #db configuration
    db_config = {
        'POSTGRES_USER': os.getenv('POSTGRES_USER'),
        'POSTGRES_PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'POSTGRES_HOST': os.getenv('POSTGRES_HOST'),
        'DB_PORT': os.getenv('DB_PORT'),
        'POSTGRES_DB': os.getenv('POSTGRES_DB')
    }
    
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{db_config['POSTGRES_USER']}:{db_config['POSTGRES_PASSWORD']}"
        f"@{db_config['POSTGRES_HOST']}:{db_config['DB_PORT']}/{db_config['POSTGRES_DB']}"
    )
    app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_secret_key')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24) #set after hoe long should the access token expire

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app,resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}},supports_credentials=True)
    jwt = JWTManager(app)
    # @app.before_request
    # def handle_preflight():
    #     """ Ensure OPTIONS requests return correct CORS headers. """
    #     if request.method == "OPTIONS":
    #         response = jsonify({"message": "CORS Preflight OK"})
    #         response.headers["Access-Control-Allow-Origin"] = "*"
    #         response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    #         response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    #         response.headers["Content-Type"] = "application/json"  # Set JSON Content-Type
    #         return response, 200

    # @app.after_request
    # def add_cors_headers(response):
    #     """ Ensure all responses include correct CORS headers and JSON Content-Type. """
    #     response.headers["Access-Control-Allow-Origin"] = "*"
    #     response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    #     response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        
    #     #  Ensure the response is always JSON
    #     if response.content_type == "text/html; charset=utf-8":
    #         response.headers["Content-Type"] = "application/json"


    #importing the bp inside the function to avoid circular imports
    from .routes.foods import foods_bp
    from .routes.user import user_bp

    #register the blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(foods_bp)

    return app