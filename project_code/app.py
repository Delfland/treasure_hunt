from flask import Flask, render_template


from controllers.users_controller import users_blueprint
from controllers.games_controller import games_blueprint
from controllers.locations_controller import locations_blueprint

app = Flask(__name__)

app.register_blueprint(users_blueprint)
app.register_blueprint(games_blueprint)
app.register_blueprint(locations_blueprint)


@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)