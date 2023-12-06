import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity, get_jwt, jwt_required
from db import db
from models import BookModel, UserModel, PageModel  
from schemas import BookSchema

blp = Blueprint("books", __name__, description= "Operations on books")

@blp.route("/book")
class Booklist(MethodView):
    
    @blp.response(200, BookSchema(many = True))
    def get(self):
        return BookModel.query.all()

@blp.route("/user/book")
class BookInUser(MethodView):
    @jwt_required()
    @blp.response(200, BookSchema(many=True)) # get user all book
    def get(self):
        user_id= get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        return user.books
    
    @jwt_required()
    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, book_data):  # create book
        user_id= get_jwt_identity()     
        Book = BookModel(**book_data, user_id = user_id, thumb = 0)
        
        try:
            db.session.add(Book)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message = str(e))
        return Book
    
@blp.route("/book/<int:book_id>")
class Book(MethodView):
    @jwt_required()
    @blp.response(200, BookSchema)
    def get(self, book_id): # get specific book
        Book = BookModel.query.get_or_404(book_id)
        return Book
    

    @jwt_required()
    @blp.response(202,
                  description="Deletes a book if no pages are within it.",
                  example={"message": "Book deleted"}
                  )
    @blp.alt_response(404, description="Book not found.")
    @blp.alt_response(400,
                      description="Returned if the book is assigned to one or more pages. In this case, the book is not deleted."
                      )
    def delete(self, book_id):
        Book = BookModel.query.get_or_404(book_id)
        user_id= get_jwt_identity()  
        if Book.user_id != user_id:
            abort(401,
              message="Signature verification failed. Make sure the book is belong to the user."
              )

        if not Book.pages:
            db.session.delete(Book)
            db.session.commit()
            return {"message": "Book deleted"}
        abort(400,
              message="Could not delete book. Make sure the book is not associated with any pages, then try again"
              )

@blp.route("/thumb/<book_id>")
class thumb(MethodView):
    @jwt_required()
    @blp.response(200, BookSchema)
    def post(self,book_id):
        Book = BookModel.query.get_or_404(book_id)
        if Book:
            Book.thumb +=1

        db.session.add(Book)
        db.session.commit()
        return Book