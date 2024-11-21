# Задача "Имитация работы с БД"

# Импорт необходимых библиотек
from fastapi import FastAPI

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Инициализация словаря пользователей
users = {'1': 'Имя: Example, возраст: 18'}

# Создаем маршрут к главной странице
@app.get("/")
async def access_root():
    return "MAIN"


# GET запрос для получения всех пользователей
@app.get("/users")
async def get_users():
    return users


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int):
    # Находим максимальный ключ в словаре
    new_id = str(max(map(int, users.keys()), default=0) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


# PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    del users[user_id]
    return f"User {user_id} deleted"

