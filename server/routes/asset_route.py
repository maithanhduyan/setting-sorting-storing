from flask import Blueprint, jsonify, request, redirect
from flask_marshmallow import Marshmallow
from models.asset import Asset
from db import db
from schema import asset_schema, assets_schema


asset_blueprint = Blueprint('asset_blueprint', __name__)
# Định nghĩa route để lấy tất cả các assets


@asset_blueprint.route('/assets', methods=['GET'])
def get_assets():
    all_assets = Asset.query.all()
    result = assets_schema.dump(all_assets)
    return jsonify(result)

# Định nghĩa route để lấy một asset bằng ID


@asset_blueprint.route('/assets/<int:id>', methods=['GET'])
def get_asset(id):
    asset = Asset.query.get(id)
    return asset_schema.jsonify(asset)


# Định nghĩa route để cập nhật một asset bằng ID
@asset_blueprint.route('/assets/<int:id>', methods=['PUT'])
def update_asset(id):
    asset = Asset.query.get(id)

    name = request.json['name']
    code = request.json['code']
    price = request.json['price']
    website = request.json['website']
    description = request.json['description']

    asset.name = name
    asset.code = code
    asset.price = price
    asset.website = website
    asset.description = description

    db.session.commit()

    return asset_schema.jsonify(asset)


# Định nghĩa route để xóa một asset bằng ID
@asset_blueprint.route('/assets/<int:id>', methods=['DELETE'])
def delete_asset(id):
    asset = Asset.query.get(id)
    db.session.delete(asset)
    db.session.commit()

    return asset_schema.jsonify(asset)

# ------- End Routes ---------
