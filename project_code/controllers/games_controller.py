from flask import render_template, redirect, Blueprint
from repositories import games_repository

games_blueprint = Blueprint("games", __name__)

# NEW
# POST '/games/new'
@games_blueprint.route("/games/new",  methods=['POST'])
def new_game():
    #some code to help select user id
    return render_template("books/new.html", all_authors = authors)

# SHOW LOCATIONS FOR INDIVIDUAL GAME
# GET '/games/<id>/locations'

# CREATE NEW LOCATION FOR INDIVIDUAL GAME
# POST '/games/<id>/locations/new'

# DELETE
# POST '/games/<id>'

# EDIT
# POST '/games/<id>/edit'