from flask import render_template, request, redirect, Blueprint
from repositories import locations_repository
from repositories import users_repository
from repositories import games_repository
from models.location import Location

locations_blueprint = Blueprint("locations", __name__)

# SHOW
# GET '/locations/<id>'
@locations_blueprint.route("/locations/<id>", methods=['GET'])
def show_location(id):
    location = locations_repository.select_by_id(id)
    return render_template('locations/location.html', my_location = location)

# NEW
# GET '/locations/new'
@locations_blueprint.route("/locations/new", methods=['POST'])
def new_location():
    game = request.form["game_id"]
    user = request.form["user_id"]
    return render_template("locations/new.html", user_id=user, game_id = game)

# SAVE
# POST '/locations/new'
@locations_blueprint.route("/locations",  methods=['POST'])
def save_game():
    name = request.form['name']
    clue = request.form['clue']
    location_user = request.form['user_id']
    location_game = request.form['game_id']
    user = users_repository.select_by_id(location_user)
    game = games_repository.select_by_id(location_game)
    location = Location(name, clue, user, game)
    locations_repository.save(location)
    return redirect('/games/{{"game_id"}}')

# DELETE
# POST '/locations/<id>'


# EDIT
# POST '/locations/<id>/edit'