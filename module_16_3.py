# Задача "Имитация работы с БД"

# Импорт необходимых библиотек
from fastapi import FastAPI
from typing import Annotated
from fastapi import Path

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Инициализация словаря пользователей
users = {'1': 'Имя: Example, возраст: 18'}

# GET запрос для получения всех пользователей
@app.get("/users")
async def get_users():
    return users

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def add_user(
    username: Annotated[str, Path(description="Enter username")],
    age: Annotated[int, Path(description="Enter age")]):

    # Находим максимальный ключ в словаре
    new_id = str(max(map(int, users.keys()), default=0) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


# PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path(description="Enter user ID")],
    username: Annotated[str, Path(description="Enter username")],
    age: Annotated[int, Path(description="Enter age")]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is update"


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(description="Enter user ID")]):
    del users[user_id]
    return f"User {user_id} has been deleted"

