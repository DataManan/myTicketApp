# from enum import unique
from ..database import db

class Shows(db.Model):
    tablename = 'shows'
    show_id = db.Column(db.String, unique=True, primary_key=True)
    show_name = db.Column(db.String, unique=True, nullable=False)
    release_date = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Numeric(precision=3, scale=1))
    tags = db.Column(db.String)
    show_description = db.Column(db.String)
    cast = db.Column(db.String)

  

