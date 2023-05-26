from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

db_path = os.path.join(os.path.dirname(__file__), 'db', 'database.sqlite')
print('DB Path: '+db_path)
db_uri = 'sqlite:///{}'.format(db_path)