# schema，可以讓輸入進的資料跟輸出進的資料格式轉成我們想要的
from marshmallow import Schema, fields

class PlainPageSchema(Schema):
    id = fields.Str(dump_only=True)
    # tag = fields.Str(required = True)
    # book_name = fields.Str(required = True)
    page_number = fields.Int(required = True)
    text = fields.Str(required = True)
    image_url = fields.Str(required = True)

    # store_id = fields.Str(required = True) 

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required = True)
    password = fields.Str(required=True,
                          load_only=True
                          )
    
class PlainBookSchema(Schema):
    id = fields.Int(dump_only=True)
    book_name = fields.Str(required = True)
    thumb = fields.Str(dump_only=True)
    tag = fields.Str(required = True)

class PageUpdateSchema(Schema):
    text = fields.Str(required = True)
    image_url = fields.Str(required = True)



class PageSchema(PlainPageSchema):
    user_id = fields.Int(dump_only = True)
    book_id = fields.Int(required = True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)
    book = fields.Nested(PlainBookSchema(), dump_only=True)

class UserSchema(PlainUserSchema):
    pages = fields.List(fields.Nested(PlainPageSchema()), dump_only = True)
    books = fields.List(fields.Nested(PlainBookSchema()), dump_only = True)


class BookSchema(PlainBookSchema):
    user_id = fields.Int(dump_only = True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)
    pages = fields.List(fields.Nested(PlainPageSchema()), dump_only = True)


class BlockListSchema(Schema):
    id = fields.Int(dump_only=True)
    expired = fields.Str(dump_only=True)