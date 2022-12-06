from db.run_sql import run_sql

from models.game import Game
from models.user import User
from models.location import Location
import repositories.users_repository as users_repository


def save(game):
    sql = "INSERT INTO games (name, user_id) VALUES (%s, %s) RETURNING id"
    values = [game.name, game.user.id]
    results = run_sql(sql, values)
    game.id = results[0]["id"]
    return game


def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)


def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        user = users_repository.select_by_id(row['user_id'])
        game = Game(row['name'], user)
        games.append(game)
    return games


def select_by_id(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        game = Game(result["name"], result["user_id"], result["id"])
    return game

def delete_by_id(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(game):
    sql = "UPDATE games SET (name, user_id) = (%s, %s) WHERE id = %s"
    values = [game.name, game.user.id, game.id]
    print(values)
    run_sql(sql, values)

def locations_by_game(game):
    locations = []

    sql = "SELECT * FROM locations WHERE game_id = %s"
    values = [game.id]
    results = run_sql(sql, values)

    for row in results:
        location = Location(row['name'], row['clue'], row['user_id'], row['game_id'], row['id'] )
        locations.append(location)
    return locations
