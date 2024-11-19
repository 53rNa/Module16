# Задача "Начало пути"

# Импорт необходимых библиотек
from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
from fastapi import Query

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Создаем маршрут к главной странице
@app.get("/")
async def home_page():
    return "Главная страница"

# Создаем маршрут к странице администратора
@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

# Создаем маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
async def user_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

# Создаем маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user")
async def user_page_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

