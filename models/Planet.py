from db import db

class Planet(db.Model):
    p_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable = False)
    mr_unit = db.Column(db.String(1), nullable = False)
    mass = db.Column(db.Float, nullable = False)
    radius = db.Column(db.Float, nullable = False)
    distance = db.Column(db.Float, nullable = False)