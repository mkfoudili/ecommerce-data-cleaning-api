from db import db

class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column('category-id', db.Integer, primary_key=True)
    category = db.Column(db.Text)

    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'goods'
    product_id = db.Column('goods-id', db.Integer, primary_key=True)
    product_title = db.Column('goods-title', db.Text)
    price = db.Column(db.Float)
    discount = db.Column(db.Integer)
    color_count = db.Column('color-count', db.Float)
    rank_title = db.Column('rank-title', db.Integer)
    rank_sub = db.Column('rank-sub', db.Text)
    selling_proposition = db.Column('selling-proposition', db.Float)
    category_id = db.Column('category-id', db.Integer, db.ForeignKey('categories.category-id'))