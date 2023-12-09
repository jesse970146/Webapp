from db import db

class BookModel(db.Model):
    __tablename__ = "books"

    id  = db.Column(db.Integer, primary_key = True)
    book_name  = db.Column(db.String(80), unique = True, nullable = False)
    thumb = db.Column(db.Integer, unique = False, nullable = False)
    tag = db.Column(db.String(80), nullable = False)
    user_id =db.Column(db.Integer, db.ForeignKey("users.id"), unique = False, nullable = False)
    user = db.relationship("UserModel", back_populates = "books" )
    
    pages = db.relationship("PageModel", back_populates = "book", lazy ="dynamic", cascade = "all, delete-orphan")