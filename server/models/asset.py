from db import db

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    website = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)    
    asset_type_id = db.Column(db.String(200), nullable=False)    

    def __init__(self, name, code, price, website, description):
        self.name = name
        self.code = code
        self.price = price
        self.website = website
        self.description = description
