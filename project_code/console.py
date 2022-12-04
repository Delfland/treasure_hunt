from models.user import User

import repositories.users_repository as users_repository

users_repository.delete_all()

user1 = User("Delphine")
users_repository.save(user1)
user2 = User("Eden")
users_repository.save(user2)
user3 = User("Mamie")
users_repository.save(user3)

all_users = users_repository.select_all()
for user in all_users:
    print(user.name)

userbyid1 = users_repository.select_by_id(47)
print(userbyid1.name)