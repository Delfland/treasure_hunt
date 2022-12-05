from flask import render_template, redirect, Blueprint
from repositories import games_repository

from app import app

games_blueprint = Blueprint("games", __name__)

# NEW
# POST '/games/new'


# SHOW LOCATIONS FOR INDIVIDUAL GAME
# GET '/games/<id>/locations'

# CREATE NEW LOCATION FOR INDIVIDUAL GAME
# POST '/games/<id>/locations/new'

# DELETE
# POST '/games/<id>'

# EDIT
# POST '/games/<id>/edit'