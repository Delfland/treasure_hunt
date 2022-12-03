from models.user import User

import repositories.users_repository as users_repository

user1 = User("Delphine")
users_repository.save(user1)
user2 = User("Eden")
users_repository.save(user2)
user3 = User("Mamie")
users_repository.save(user3)