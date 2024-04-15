from flask import Blueprint, render_template, request, redirect 
from db import db
from models.Planet import Planet

root = Blueprint('root', __name__, template_folder='templates')

@root.route('/')
def home():
    return render_template("index.html")

@root.route('/planet')
def planets():
    planets = Planet.query.all()
    return render_template("planets.html", planets = planets)

@root.route('/add_planet', methods=['GET', 'POST'])
def add_planet():
    if request.method == "POST":
        name = request.form['name']
        mr_unit = request.form['mr_unit']
        mass = request.form['mass']
        radius = request.form['radius']
        distance = request.form['distance']

        if mr_unit == 'none':
            return redirect("/planet")

        planet = Planet(
            name = name,
            mr_unit = mr_unit,
            mass = mass,
            radius = radius,
            distance = distance
        )
        db.session.add(planet)
        db.session.commit()
        return redirect("/planet")
    return render_template("add_planet.html")


@root.route('/delete_planet/<pid>')
def delete_planet(pid):
    planet = Planet.query.filter_by(p_id= pid).first()
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return redirect("/planet")
    else:
        return "No planet with that name"


@root.route('/update_planet/<pid>', methods = ['GET', "POST"])
def update_planet(pid):
    planet = Planet.query.filter_by(p_id= pid).first()
    if request.method == "POST":
        if request.form['mr_unit'] == 'none':
            return redirect("/planet")        

        planet.name = request.form['name']
        planet.mr_unit = request.form['mr_unit']
        planet.mass = request.form['mass']
        planet.radius = request.form['radius']
        planet.distance = request.form['distance']

        db.session.commit()
        return redirect("/planet")
    return render_template("update_planet.html", planet = planet)