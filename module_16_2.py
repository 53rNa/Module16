# Задача "Аннотация и валидация"

# Импорт необходимых библиотек
from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from fastapi import Query
from fastapi import Path
from typing import Annotated

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Создаем маршрут к главной странице
@app.get("/")
async def access_root():
    return "Главная страница"

# Создаем маршрут к странице администратора
@app.get("/user/admin")
async def access_admin():
    return "Вы вошли как администратор"

# Создаем маршрут к страницам пользователей с параметром в пути и валидацией
@app.get("/user/{user_id}")
async def read_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]):
    return f"Вы вошли как пользователь № {user_id}"

# Создаем маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

