# Задача "Модель пользователя"

# Импорт необходимых библиотек
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Инициализация пустого списка пользователей
users = []

# Создаем класс User, наследованный от BaseModel, который будет содержать поля id, username, age
class User(BaseModel):
    id: int
    username: str
    age: int


# GET запрос по маршруту '/users' возвращает список users
@app.get("/users", response_model=List[User])
async def get_users():
    return users


# POST запрос добавляет в список users объект User
@app.post("/user/{username}/{age}", response_model=User)
async def add_user(username: str, age: int):

    # id объекта User будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1
    new_id = (users[-1].id + 1) if users else 1

    # Все остальные параметры объекта User - переданные в функцию username и age соответственно
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)

    # Возвращаем созданного пользователя
    return new_user


# PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, username: str, age: int):

    # Обновляем username и age пользователя, если пользователь с таким user_id есть в списке users и возвращаем его
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    # В случае отсутствия пользователя, выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404
    raise HTTPException(status_code=404, detail="User was not found")


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    # Удаляем пользователя, если пользователь с таким user_id есть в списке users и возвращаем его
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user

    # В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404
    raise HTTPException(status_code=404, detail="User was not found")



