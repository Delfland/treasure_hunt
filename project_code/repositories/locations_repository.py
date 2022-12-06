from db.run_sql import run_sql

from models.location import Location
import repositories.users_repository as users_repository
import repositories.games_repository as games_repository

def save(location):
    sql = "INSERT INTO locations (name, clue, user_id, game_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [location.name, location.clue, location.user.id, location.game.id]
    results = run_sql(sql, values)
    location.id = results[0]["id"]
    return location

def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)

def select_all():
    locations = []
    sql = "SELECT * FROM locations"
    results = run_sql(sql)
    for row in results:
        user = users_repository.select_by_id(row['user_id'])
        game = games_repository.select_by_id(row['game_id'])
        location = Location(row['name'], row['clue'], user, game, row['found'], row['id'])
        locations.append(location)
    return locations

def select_by_id(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        location = Location(result["name"], result["clue"], result["user_id"], result["game_id"], result['found'], result["id"])
    return location

def delete_by_id(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(location):
    sql = "UPDATE locations SET (name, clue, user_id, game_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [location.name, location.clue, location.user.id, location.game.id, location.id]
    print(values)
    run_sql(sql, values)

def found(location):
    sql = "UPDATE locations SET found = %s WHERE id = %s"
    values = [True, location.id]
    run_sql(sql,values)


