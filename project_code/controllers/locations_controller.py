from flask import render_template, redirect, Blueprint
from repositories import locations_repository

locations_blueprint = Blueprint("locations", __name__)

# SHOW
# GET '/locations/<id>'
@locations_blueprint.route("/locations/<id>", methods=['GET'])
def show_location(id):
    location = locations_repository.select_by_id(id)
    return render_template('locations/location.html', my_location = location)

# DELETE
# POST '/locations/<id>'


# EDIT
# POST '/locations/<id>/edit'