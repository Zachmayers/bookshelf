from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    shelves = db.relationship('Shelf')

class Shelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    added_date = db.Column(db.DateTime(timezone=True), default=func.now())
    category = name = db.Column(db.String(10000))
    items = db.relationship('Item')
    user_ID = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Name %r>' % self.name

# class ShelfList(db.Model):
#     child_id = db.Column(db.Integer, primary_key=True)
#     parent_id = db.Column(db.Integer, db.ForeignKey('Shelf.id'))


class Item(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelf.id'))
    title     = db.Column(db.String(10000))
    release_year = db.Column(db.Integer, default='2000')
    creator = db.Column(db.String(10000))



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # item_id = db.Column(db.Integer, db.ForeignKey('Item.id'))



# class music():
#     name = str()
#     artist = str()
#     releaseYear = int()
#     label = str()
#     genre = str()
#     upc = int()


# class cd():
#     name = str()
#     artist = str()
#     releaseYear = int()
#     numTracks = int()
#     label = str()
#     compilation = bool()
#     genre = str()
#     mediaCondition = str()
#     upc = int()


# class cassette():
#     name = str()
#     artist = str()
#     releaseYear = int()
#     numTracks = int()
#     label = str()
#     compilation = bool()
#     noiseReduction = str()
#     tapeType = str()
#     genre = str()
#     mediaCondition = str()
#     upc = int()


# class lp():
#     name = str()
#     artist = str()
#     releaseYear = int()
#     numTracks = int()
#     numRecords = int()
#     label = str()
#     compilation = bool()
#     genre = str()
#     mediaCondition = str()
#     sleeveCondition = str()
#     upc = int()
