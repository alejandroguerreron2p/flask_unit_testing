from marshmallow import Schema, fields

class Book(Schema):
    title = fields.String(required=True)
    author = fields.String(required=True)