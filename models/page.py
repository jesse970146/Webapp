#在db.py宣告完SQLalchemy的db後，在models的資料夾內設定資料表的內容
from db import db


class PageModel(db.Model):
    __tablename__ = "pages"

    id  = db.Column(db.Integer, primary_key = True)
    # tag = db.Column(db.String(80), nullable = False)
    # book_name  = db.Column(db.String(80), nullable = False)
    page_number = db.Column(db.Integer, nullable = False)
    text = db.Column(db.String(), nullable = False)
    image_url = db.Column(db.String(), nullable = False)
    book_id =db.Column(db.Integer, db.ForeignKey("books.id"), unique = False, nullable = False)
    user_id =db.Column(db.Integer, db.ForeignKey("users.id"), unique = False, nullable = False)
    user = db.relationship("UserModel", back_populates = "pages" )
    book = db.relationship("BookModel", back_populates = "pages" )