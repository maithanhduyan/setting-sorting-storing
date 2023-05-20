from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import click

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
CORS(app)  # Kích hoạt Flask-CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets.db'  # Đường dẫn đến file SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo đối tượng SQLAlchemy và Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Khởi tạo đối tượng Migrate
migrate = Migrate(app, db)

# Định nghĩa mô hình Asset
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    website = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, name, code, price, website, description):
        self.name = name
        self.code = code
        self.price = price
        self.website = website
        self.description = description


# Định nghĩa lược đồ marshmallow cho Asset
class AssetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'code', 'price', 'website', 'description')


# Khởi tạo schema cho một asset
asset_schema = AssetSchema()
assets_schema = AssetSchema(many=True)


# Định nghĩa route để tạo một asset mới
@app.route('/assets', methods=['POST'])
def add_asset():
    name = request.json['name']
    code = request.json['code']
    price = request.json['price']
    website = request.json['website']
    description = request.json['description']

    new_asset = Asset(name, code, price, website, description)

    db.session.add(new_asset)
    db.session.commit()

    return asset_schema.jsonify(new_asset)


# Định nghĩa route để lấy tất cả các assets
@app.route('/assets', methods=['GET'])
def get_assets():
    all_assets = Asset.query.all()
    result = assets_schema.dump(all_assets)
    return jsonify(result)


# Định nghĩa route để lấy một asset bằng ID
@app.route('/assets/<int:id>', methods=['GET'])
def get_asset(id):
    asset = Asset.query.get(id)
    return asset_schema.jsonify(asset)


# Định nghĩa route để cập nhật một asset bằng ID
@app.route('/assets/<int:id>', methods=['PUT'])
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
@app.route('/assets/<int:id>', methods=['DELETE'])
def delete_asset(id):
    asset = Asset.query.get(id)
    db.session.delete(asset)
    db.session.commit()

    return asset_schema.jsonify(asset)


# Tạo dữ liệu mẫu bằng CLI
@app.cli.command()
@click.option('--count', default=10, help='Số lượng asset cần tạo')
def create_sample_assets(count):
    for i in range(count):
        name = f'Asset {i+1}'
        code = f'A{i+1:03}'
        price = float((i+1) * 10)
        website = f'https://www.example.com/asset{i+1}'
        description = f'This is asset {i+1}'

        new_asset = Asset(name, code, price, website, description)
        db.session.add(new_asset)

    db.session.commit()

    click.echo(f'Đã tạo thành công {count} asset dữ liệu mẫu.')

# Khởi tạo cơ sở dữ liệu SQLite và chạy ứng dụng trên cổng 5000
if __name__ == '__main__':
    app.run(port=5000)
