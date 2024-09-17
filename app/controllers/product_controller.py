from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

product_bp = Blueprint('product', __name__)

product_service = ProductService()

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = product_service.create_product(data)
    return jsonify(product), 201

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product_by_id(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({'message': 'Product not found'}), 404
