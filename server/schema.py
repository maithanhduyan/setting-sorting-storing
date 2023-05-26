from flask_marshmallow import Marshmallow

ma = Marshmallow()

class AssetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'code', 'price', 'website', 'description','asset_type_id')

asset_schema = AssetSchema()
assets_schema = AssetSchema(many=True)