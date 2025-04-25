from flask import Flask, Blueprint, jsonify, request
from flasgger import Swagger
from db import db
from models import Product, Category
from schemas import ProductSchema,CategorySchema

bp = Blueprint('api', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
category_schema = CategorySchema()
categories_schemas = CategorySchema(many=True)

app = Flask(__name__)
swagger = Swagger(app)

@bp.route('/products', methods=['GET'])
def get_all_products():
    """
    Get all products.
    This endpoint returns a list of all products in the database.

    ---
    responses:
      200:
        description: A list of products
        content:
          application/json:
            schema:
              type: array
              items: ProductSchema
    """
    products = Product.query.all()
    return products_schema.jsonify(products)

@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Get a specific product by its ID.
    This endpoint returns the details of a single product based on the provided product_id.

    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: The ID of the product to retrieve
    responses:
      200:
        description: A single product
        content:
          application/json:
            schema:
              type: object
              properties:
                product:
                  type: object
                  items: ProductSchema
      404:
        description: Product not found
    """
    product = Product.query.get_or_404(product_id)
    return product_schema.jsonify(product)

@bp.route('/categories', methods=['GET'])
def get_all_categories():
    """
    Get all categories.
    This endpoint returns a list of all categories in the database.

    ---
    responses:
      200:
        description: A list of categories
        content:
          application/json:
            schema:
              type: array
              items: CategorySchema
    """
    categories = Category.query.all()
    return categories_schemas.jsonify(categories)

@bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """
    Get a specific category by its ID.
    This endpoint returns the details of a single category based on the provided category_id.

    ---
    parameters:
      - name: category_id
        in: path
        type: integer
        required: true
        description: The ID of the category to retrieve
    responses:
      200:
        description: A single category
        content:
          application/json:
            schema:
              type: object
              properties:
                category:
                  type: object
                  items: CategorySchema
      404:
        description: Category not found
    """
    category = Category.query.get_or_404(category_id)
    return category_schema.jsonify(category)

@bp.route('/categories/<int:category_id>/products', methods=['GET'])
def get_products_by_category(category_id):
    """
    Get all products by category ID.
    This endpoint returns a list of products belonging to the category specified by category_id.

    ---
    parameters:
      - name: category_id
        in: path
        type: integer
        required: true
        description: The ID of the category whose products to retrieve
    responses:
      200:
        description: A list of products in the given category
        content:
          application/json:
            schema:
              type: array
              items: ProductSchema
    """
    products = Product.query.filter_by(category_id=category_id).all()
    return products_schema.jsonify(products)

@bp.route('/products', methods=['POST'])
def create_product():
    """
    Create a new product.
    This endpoint allows you to add a new product to the database.

    ---
    requestBody:
      description: The data for the new product
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              product_title:
                type: string
              price:
                type: number
                format: float
              discount:
                type: integer
              color_count:
                type: number
                format: float
              rank_title:
                type: integer
              rank_sub:
                type: string
              selling_proposition:
                type: number
                format: float
              category_id:
                type: integer
    responses:
      201:
        description: Product created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                product:
                  type: object
                  items: ProductSchema
    """
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
    """
    Update an existing product.
    This endpoint allows you to modify an existing product in the database.

    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: The ID of the product to update
    requestBody:
      description: The data to update the product
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              product_title:
                type: string
              price:
                type: number
                format: float
              discount:
                type: integer
              color_count:
                type: number
                format: float
              rank_title:
                type: integer
              rank_sub:
                type: string
              selling_proposition:
                type: number
                format: float
              category_id:
                type: integer
    responses:
      200:
        description: Product updated successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                product:
                  type: object
                  items: ProductSchema
      404:
        description: Product not found
    """
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
    """
    Delete a product by ID.
    This endpoint allows you to delete a product from the database by its ID.

    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: The ID of the product to delete
    responses:
      200:
        description: Product deleted successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Product deleted successfully
      404:
        description: Product not found
    """
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})