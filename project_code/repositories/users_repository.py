from db.run_sql import run_sql

from models.user import User

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

#define function select_by_id with id value as parameter
def select_by_id(id):
    #set user variable equal to None
    user = None
    # set sql variable equal to select all from users table where id = placeholder
    sql = "SELECT * FROM users WHERE id = %s"
    #set values variable equal to id dictionary key
    values = [id]
    # set results variable equal to run function run_sql with parameters sql and values
    results = run_sql(sql, values)
    # if statement on results = trues:
    if results:
    #   result variable is the first index position of results variable
        result = results[0]
    #   user variable equals instance of user class with result[attributes]
        user = User(result['name'], result['id'])
    #return user variable
    return user