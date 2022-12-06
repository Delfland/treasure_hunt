from flask import render_template, redirect, request, Blueprint
from repositories import games_repository
from repositories import users_repository
from repositories import locations_repository
from models.game import Game
from models.user import User

games_blueprint = Blueprint("games", __name__)

#ALL GAMES
# GET '/games'
@games_blueprint.route("/games")
def all_games():
    games = games_repository.select_all() # NEW
    return render_template("games/index.html", all_games = games)

# NEW
# GET '/games/new'
@games_blueprint.route("/games/new", methods=['POST'])
def new_game():
    all_users = users_repository.select_all()
    return render_template("games/new.html", users_list = all_users)

# SAVE
# POST '/games/new'
@games_blueprint.route("/games",  methods=['POST'])
def save_game():
    name = request.form['name']
    game_user = request.form['user']
    game = Game(name, game_user.id)
    games_repository.save(game)
    return redirect('/games')


# SHOW INDIVIDUAL GAME
# GET '/games/<id>'
@games_blueprint.route("/games/<id>", methods=['GET'])
def show_game(id):
    game = games_repository.select_by_id(id)
    locations = games_repository.locations_by_game(game)
    return render_template('games/game.html', my_game = game, all_locations = locations)

# CREATE NEW LOCATION FOR INDIVIDUAL GAME
# POST '/games/<id>/locations/new'

# DELETE
# POST '/games/<id>/delete'


# EDIT
# POST '/games/<id>/edit'