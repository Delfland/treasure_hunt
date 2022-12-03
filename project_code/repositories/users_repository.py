from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING *"
    values = [user.name] 
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user

# define function delete_all
# set sql variable equal to delete from users
# run the sql function on the sql variable