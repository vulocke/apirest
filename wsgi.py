# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort, request
import itertools
import json

app = Flask(__name__)

PRODUCTS = {
	1: { 'id': 1, 'name': 'Skello' },
	2: { 'id': 2, 'name': 'Socialive.tv' },
	3: { 'id': 3, 'name': 'Product3' }
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=["GET"])
def read_all_products():
	return jsonify(list(PRODUCTS.values())), 200

@app.route('/api/v1/products/<int:id>', methods=["GET"])
def read_one_product(id):
	product = PRODUCTS.get(id)
	if product is None:
		abort(404)
	return jsonify(product), 200

@app.route('/api/v1/products/<int:id>', methods=["DELETE"])
def delete_one_product(id):
	product = PRODUCTS.pop(id, None)
	if product is None:
		abort(404)
	return jsonify(product),204

@app.route('/api/v1/products', methods=["POST"])
def create_one_product():
	START_INDEX = len(PRODUCTS) + 1
	IDENTIFIER_GENERATOR = itertools.count(START_INDEX)
	id = next(IDENTIFIER_GENERATOR)

	# request.get_data : get body json
	# json.loads : convert bytes to json
	body = json.loads(request.get_data())
	product = {id : {'id' : id, 'name' : body.get('name')}}
	PRODUCTS.update(product)
	return jsonify(product), 201

@app.route('/api/v1/products/<int:id>', methods=["PATCH"])
def update_one_product(id):
	# request.get_data : get body json
	# json.loads : convert bytes to json
	body = json.loads(request.get_data())
	# name for update
	name = body.get('name')
	product = {id : {'id' : id, 'name' : name}}
	PRODUCTS.update(product)
	return jsonify(product), 204
