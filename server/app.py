from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from db import db, db_uri
from models.asset import Asset
from models.user import User
from models.asset_type import AssetType
from routes.asset_route import asset_blueprint 

# create the app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

# initialize the app with the extension
db.init_app(app)

# ------- Routes ---------
CORS(app)  # Kích hoạt Flask-CORS

# app.register_blueprint(home_blueprint)
app.register_blueprint(asset_blueprint)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Create sqlite DB
with app.app_context():
    db.create_all()


# Khởi tạo cơ sở dữ liệu SQLite và chạy ứng dụng trên cổng 5000
if __name__ == '__main__':
    app.run(port=5000)
