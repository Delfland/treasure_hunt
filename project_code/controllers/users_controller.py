from flask import Flask, render_template, request, redirect, Blueprint
from repositories import users_repository
from models.user import User

users_blueprint = Blueprint("users", __name__)

# INDEX
# GET '/users'
@users_blueprint.route("/users")
def users():
    users = users_repository.select_all()
    return render_template("users/index.html", all_users = users)

# NEW
# POST '/users'
@users_blueprint.route("/users",  methods=['POST'])
def save_user():
    name = request.form['name']
    new_player = User(name)
    users_repository.save(new_player)
    return redirect('/users')

# SHOW
# GET '/users/<id>'
@users_blueprint.route("/users/<id>", methods=['GET'])
def show_user(id):
    player = users_repository.select_by_id(id)
    games = users_repository.games_by_user(player)
    return render_template('users/user.html', player_games = games, user = player)

# DELETE
# POST '/users/<id>/delete'
@users_blueprint.route("/users/<id>/delete", methods=['POST'])
def delete_user(id):
    users_repository.delete_by_id(id)
    return redirect('/users')
