from main import User, UserService

user = UserService()

# user_sevice = User(name="abu", email="abu@gmail.com", age=18)
# user.add_user(user_service)

# find= user.find_user_by_email("abu@gmail.com")
# if find:
#     print(f"пользователь {find.name}, {find.email}, {find.age} найден")

delete = user.delete_user_by_email("abu@gmail.com")