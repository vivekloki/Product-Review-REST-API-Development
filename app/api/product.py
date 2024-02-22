import csv

from flask import jsonify, request

from app.api import bp
from app import logging
from app.services.products import load_data,get_top_rated_products,search_products_by_category,\
calculate_average_discount_by_category


@bp.route('/test', methods=["GET"])
def test():
    # print(request.json)
    return jsonify({"message": "Success", "status": 200})


@bp.route('/product', methods=["POST"])
def search_product():
    try:
        data = load_data()
        input_data = request.json.get('product_id')
        if input_data is not None:
            filtered_data = [record for record in data if record['product_id'] == input_data]
            result = filtered_data
            return jsonify({"message": "Success", "status": 200, "data": result})
        else:
            return jsonify({"message": "Product ID not provided", "status": 400})
    except FileNotFoundError:
        return jsonify({"message": "Dataset not found", "status": 404})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}", "status": 500})


@bp.route('/top_rated_products', methods=["GET"])
def top_rated_products():
    try:
        data = load_data()
        top_rated = get_top_rated_products(data)

        return jsonify({"message": "Success", "status": 200, "data": top_rated})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}", "status": 500})


@bp.route('/average_discount_by_category', methods=["GET"])
def average_discount_by_category():
    try:
        data = load_data()
        average_discounts = calculate_average_discount_by_category(data)

        return jsonify({"message": "Success", "status": 200, "data": average_discounts})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}", "status": 500})


@bp.route('/products_by_category', methods=["GET"])
def products_by_category():
    try:
        data = load_data()
        category = request.args.get('category')
        if category is not None:
            products_in_category = search_products_by_category(data, category)
            return jsonify({"message": "Success", "status": 200, "data": products_in_category})
        else:
            return jsonify({"message": "Category not provided", "status": 400})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}", "status": 500})
