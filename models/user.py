#在db.py宣告完SQLalchemy的db後，在models的資料夾內設定資料表的內容
from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id  = db.Column(db.Integer, primary_key = True)
    username  = db.Column(db.String(80), unique = True, nullable = False)
    password  = db.Column(db.String(256), nullable = False)
    pages = db.relationship("PageModel", back_populates = "user", lazy ="dynamic", cascade = "all, delete-orphan")
    books = db.relationship("BookModel", back_populates = "user", lazy ="dynamic", cascade = "all, delete-orphan")
    