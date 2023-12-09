import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity, get_jwt, jwt_required
from db import db
from models import BookModel, UserModel, PageModel  
from schemas import PageSchema,PageUpdateSchema

blp = Blueprint("pages", __name__, description= "Operations on pages")

@blp.route("/page")
class Pagelist(MethodView):
    
    @blp.response(200, PageSchema(many = True))
    def get(self):
        return PageModel.query.all()
    
    # @jwt_required()
    # @blp.arguments(PageSchema)
    # @blp.response(201, PageSchema)
    # def post(self, page_data):
    #     user_id= get_jwt_identity()  
    #     Book = BookModel.query.get_or_404(page_data["book_id"])
    #     for i in Book.pages:
    #         if i.page_number == page_data["page_number"]:
    #             return abort(409, message= "A page with that page number has exists.")
        
    #     if Book:
    #         page = PageModel( **page_data, user_id = user_id)
    #         try:
    #             db.session.add(page)
    #             db.session.commit()
    #         except SQLAlchemyError:
    #             abort(500, message = "An error occurred while inserting the page.")
    #         return page
    #     else:
    #         abort(409, message= "A book with that book name didn't exists.")
    
@blp.route("/page/<int:page_id>")
class Page(MethodView):
    
    @blp.response(200, PageSchema)
    def get(self, page_id):
        item = PageModel.query.get_or_404(page_id)
        return item
    
    
    @blp.response(202,
                  description="Deletes a page.",
                  example={"message": "Page deleted"}
                  )
    @blp.alt_response(404, description="Page not found.")
    # @blp.alt_response(400,
    #                   description="Returned if the book is assigned to one or more pages. In this case, the book is not deleted."
    #                   )
    def delete(self, page_id):
        Page = PageModel.query.get_or_404(page_id)
        user_id= get_jwt_identity()  
        if Page.user_id != user_id:
            abort(401,
              message="Signature verification failed. Make sure the book is belong to the user."
              )
        db.session.delete(Page)
        db.session.commit()
        return {"message": "Page deleted"}
    
    @jwt_required()
    @blp.arguments(PageUpdateSchema)
    @blp.response(200, PageSchema)
    def put(self, page_data, page_id):
        Page = PageModel.query.get_or_404(page_id)
        user_id= get_jwt_identity()  
        if Page.user_id != user_id:
            abort(401,
              message="Signature verification failed. Make sure the page is belong to the user."
              )
        if Page:
            Page.text = page_data["text"]
            Page.image_url = page_data["image_url"]
        db.session.add(Page)
        db.session.commit()
        return Page
    
    @blp.route("/book/<int:book_id>/page")
    class PageInBook(MethodView):
        @jwt_required()
        @blp.response(200, PageSchema(many=True)) # get book all page
        def get(self,book_id):
            # user_id= get_jwt_identity()
            Book = BookModel.query.get_or_404(book_id)
            return Book.pages