# 設定api的地方，用到flask_smorest的blueprint
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity, get_jwt, jwt_required
from db import db
from models import UserModel, BlockListModel
from schemas import UserSchema, BlockListSchema

blp = Blueprint("users", __name__, description= "Operations on users")
# dev only
@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return { "message": "User deleted."}, 200

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message= "A user with that username already exists.")
        
        user = UserModel(
            username = user_data["username"],
            password = pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201
    
@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity = user.id, fresh= True)
            refresh_token = create_refresh_token(identity = user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        
        abort(401, message= "Invalid credentials")

@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh =True)
    def post(self):
        current_user= get_jwt_identity()
        if current_user:
            new_token = create_access_token(identity= current_user, fresh = False)
            return {"access_token" : new_token}

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = BlockListModel(
            expired = get_jwt()["jti"]
        )
        db.session.add(jti)
        db.session.commit()
        # BlOCKLIST.add(jti)
        return {"message":" Sucessfully logout"}
    
    @blp.response(200, BlockListSchema(many = True))
    def get(self):
        return BlockListModel.query.all()

# dev only
@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return { "message": "User deleted."}, 200
    
@blp.route("/user")
class Storelist(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()