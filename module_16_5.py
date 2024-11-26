# Задача "Список пользователей в шаблоне"

# Импорт необходимых библиотек
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Создаем объект Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Инициализация пустого списка пользователей
users = []


# Создаем класс User, наследованный от BaseModel, который будет содержать поля id, username, age
class User(BaseModel):
    id: int
    username: str
    age: int


# Создаем несколько пользователей при запуске приложения
@app.on_event("startup")
async def startup_event():
    users.append(User(id=1, username="UrbanUser", age=24))
    users.append(User(id=2, username="UrbanTest", age=22))
    users.append(User(id=3, username="Capybara", age=60))


# GET запрос для получения всех пользователей и отображение их на главной странице
@app.get("/")
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


# GET запрос для получения информации о конкретном пользователе по ID
@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    return templates.TemplateResponse("users.html", {"request": request, "user": user, "users": users})


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
async def add_user(username: str, age: int):
    # Генерация нового ID
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
