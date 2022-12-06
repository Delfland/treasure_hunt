from models.user import User
from models.game import Game
from models.location import Location

import repositories.users_repository as users_repository
import repositories.games_repository as games_repository
import repositories.locations_repository as locations_repository

users_repository.delete_all()
games_repository.delete_all()
locations_repository.delete_all()

user1 = User("Delphine")
users_repository.save(user1)
user2 = User("Eden")
users_repository.save(user2)
user3 = User("Mamie")
users_repository.save(user3)

game1 = Game("Farm animals", user1)
games_repository.save(game1)
game2 = Game("Gruffalo Characters", user3)
games_repository.save(game2)
game3 = Game("Farm vehicles", user1)
games_repository.save(game3)

location1 = Location("Cow", "Goes Moooo!", user1, game1, False)
locations_repository.save(location1)
location2 = Location("Duck", "Goes Quack Quack", user1, game1, False)
locations_repository.save(location2)
location3 = Location("Deep Dark Woods", "The mouse likes to stroll there", user3, game2, False)
locations_repository.save(location3)
location4 = Location("Logpile House", "The snake likes to feast there", user3, game2, False)
locations_repository.save(location4)


