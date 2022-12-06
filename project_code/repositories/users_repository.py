from db.run_sql import run_sql

from models.user import User
from models.game import Game
from models.location import Location

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING *"
    values = [user.name] 
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user


def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)


def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row["name"], row["id"])
        users.append(user)
    return users


def select_by_id(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = User(result['name'], result['id'])
    return user

def delete_by_id(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def games_by_user(user):
    games = []

    sql = "SELECT * FROM games WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        game = Game(row['name'], row['user_id'], row['id'] )
        games.append(game)
    return games

def locations_by_user(user):
    locations = []

    sql = "SELECT * FROM locations WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        location = Location(row['name'], row['clue'], row['user_id'], row['game_id'], row['found'], row['id'] )
        locations.append(location)
    return locations