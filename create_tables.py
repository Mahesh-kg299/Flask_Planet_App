from app import app
from db import db
from models.Planet import Planet

with app.app_context():
    db.create_all()