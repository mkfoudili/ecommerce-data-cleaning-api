from flask import Blueprint, jsonify, request
from db import db
from models import Product, Category
from schemas import ProductSchema,CategorySchema

bp = Blueprint('api', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
category_schema = CategorySchema()
categories_schemas = CategorySchema(many=True)

@bp.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return product_schema.jsonify(product)

@bp.route('/categories', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
    return categories_schemas.jsonify(categories)

@bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get_or_404(category_id)
    return category_schema.jsonify(category)

@bp.route('/categories/<int:category_id>/products', methods=['GET'])
def get_products_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    return products_schema.jsonify(products)

@bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        product_title=data['product_title'],
        price=data['price'],
        discount=data.get('discount', 0),
        color_count=data.get('color_count', 0),
        rank_title=data.get('rank_title', 0),
        rank_sub=data.get('rank_sub', ''),
        selling_proposition=data.get('selling_proposition', 0),
        category_id=data['category_id']
    )
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

@bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()

    product.product_title = data.get('product_title', product.product_title)
    product.price = data.get('price', product.price)
    product.discount = data.get('discount', product.discount)
    product.color_count = data.get('color_count', product.color_count)
    product.rank_title = data.get('rank_title', product.rank_title)
    product.rank_sub = data.get('rank_sub', product.rank_sub)
    product.selling_proposition = data.get('selling_proposition', product.selling_proposition)
    product.category_id = data.get('category_id', product.category_id)

    db.session.commit()
    return product_schema.jsonify(product)

@bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})