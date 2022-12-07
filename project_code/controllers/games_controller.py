from flask import render_template, redirect, request, Blueprint
from repositories import games_repository
from repositories import users_repository
from repositories import locations_repository
from models.game import Game
import pdb

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
    user = request.form["user_id"]
    return render_template("games/new.html", user_id=user )

# SAVE
# POST '/games/new'
@games_blueprint.route("/games",  methods=['POST'])
def save_game():
    name = request.form['name']
    game_user = request.form['user_id']
    user = users_repository.select_by_id(game_user)
    game = Game(name, user)
    games_repository.save(game)
    return redirect(f'/users/{game_user}')


# SHOW INDIVIDUAL GAME
# GET '/games/<id>'
@games_blueprint.route("/games/<id>", methods=['GET'])
def show_game(id):
    game = games_repository.select_by_id(id)
    locations = games_repository.locations_by_game(game)
    return render_template('games/game.html', my_game = game, all_locations = locations)

# DELETE
# POST '/games/<id>/delete'
@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_game(id):
    game = games_repository.select_by_id(id)
    games_repository.delete_by_id(id)
    return redirect(f'/users/{game.user}')

#START GAME
@games_blueprint.route("/games/<id>/play")
def play_game(id):
    game = games_repository.select_by_id(id)
    game_locations = games_repository.locations_by_not_found(game)
    next_location = game_locations[0]
    return render_template('games/play.html', clue = next_location.clue, id = id)

#NEXT CLUE
@games_blueprint.route('/games/<id>/play/next')
def next_clue(id):
    game = games_repository.select_by_id(id)
    game_locations = games_repository.locations_by_not_found(game)
    locations_repository.found(game_locations[0])
    # pdb.set_trace()
    game_locations = games_repository.locations_by_not_found(game)
    
    if len(game_locations) >= 1:
        next_location = game_locations[0]
        return render_template('games/play.html', clue = next_location.clue, id = id)
    else:
        return render_template('games/win.html', id = id)

#WIN GAME
@games_blueprint.route('/games/<id>/win')
def win_game(id):
    game = games_repository.select_by_id(id)
    locations_repository.not_found()
    return redirect(f"/users/{id}")