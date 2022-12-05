from flask import render_template, redirect, Blueprint
from repositories import locations_repository

from app import app

locations_blueprint = Blueprint("locations", __name__)

# SHOW
# GET '/locations/<id>'


# DELETE
# POST '/locations/<id>'


# EDIT
# POST '/locations/<id>/edit'