#設定app一些參數的地方
import os
from flask_cors import CORS
from flask import Flask,jsonify
from flask_smorest import Api
from dotenv import load_dotenv
# from resources.item import blp as ItemBlueprint
from resources.user import blp as UserBlueprint
from resources.book import blp as BookBlueprint
from resources.page import blp as PageBlueprint
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from db import db
import models
from models import BlockListModel
import datetime

def create_app(db_url=None):
    app = Flask(__name__)
    CORS(app)
    load_dotenv()
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "WebAPP API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    migrate =Migrate(app, db)

    api=  Api(app)
    app.config["JWT_SECRET_KEY"] = "260816861759538803540142184473204903862"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes = 60)
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        if BlockListModel.query.filter(BlockListModel.expired == jwt_payload["jti"]).first():
            return True
        else :
            return False
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return(
            jsonify(
                {"descripition": "The token has been revoked", "error": "token_revoked"}
            ),
            401,
        )
    
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jjwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is expired",
                    "error": "fresh_token_required"
                }
            ),
            401,
        )

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
    # with app.app_context():
    #     db.create_all()

    # api.register_blueprint(ItemBlueprint)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(BookBlueprint)
    api.register_blueprint(PageBlueprint)
    
    return app

