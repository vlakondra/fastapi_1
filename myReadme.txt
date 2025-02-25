Темы для обсуждения
1. Параметры пути и параметры запросы



#https://fastapi.xiniushu.com/ru/


git init
git branch -m master main
git remote add origin https://github.com/vlakondra/fastapi_0.git
git add .
git commit -m "Первый коммит"
git push -u origin main
?? git pull origin main --allow-unrelated-histories


======from blackbox========
cd /путь/к/вашему/проекту
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip freeze > requirements.txt
echo "#environments" > .gitignore ##Создаем файл . gitignore c 1 строкой 
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "*.pyo" >> .gitignore
echo "*.pyd" >> .gitignore
echo ".DS_Store" >> .gitignore
git init
git remote add origin URL_вашего_репозитория
git add .
git commit -m "Первый коммит"
git push -u origin main  # или git push -u origin master

=========from github=========
echo "# fastapi_1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/vlakondra/fastapi_1.git
git push -u origin main



+++++++++++++++++++++++++++++++




# grp = ['иванов','петров','сидоров']

# @app.get("/artists/{quant}/{firstchar}")
# async def myroot(quant:int,firstchar:str):
#     query = (
#         art
#         .select()
#         .where(art.name.startswith(firstchar))
#         .limit(quant)
#         .dicts()
#         )
#     return tuple(query)


# #аннотация типов аргументов функции в обычном PY-коде не вызывает ошибок,
# #если типы паретров не совпадают с типом объявленных аргуметов


# @app.get("/models/{model_name}")
# async def get_model(model_name: mod.ModelName):
#     if model_name is mod.ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


import json

# Load JSON data from the file
with open('data/studs.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

# Now 'students' variable contains the list of dictionaries
print(students)  # This will display the list of dictionaries

============================
как в приложении FastApi избежать использования глобальных переменных?

BLACKBOXAI

В приложении FastAPI можно избежать использования глобальных переменных,
 применяя различные подходы, такие как использование зависимостей, классов, 
 контекстов или баз данных. Вот несколько способов, как это можно сделать:

1. Использование зависимостей
FastAPI поддерживает систему зависимостей, которая позволяет инъектировать 
зависимости в ваши маршруты. Это позволяет избежать глобальных переменных и 
делает код более чистым и тестируемым.

Copy code
from fastapi import FastAPI, Depends

app = FastAPI()

# Пример зависимости
def get_items():
    return ["item1", "item2", "item3"]

@app.get("/items")
def read_items(items: list = Depends(get_items)):
    return {"items": items}
2. Использование классов
Вы можете создать класс для хранения состояния и использовать его в качестве зависимости. 
Это позволяет инкапсулировать состояние и методы, связанные с ним.

python

Verify
Run
Copy code
from fastapi import FastAPI, Depends

app = FastAPI()

class ItemManager:
    def __init__(self):
        self.items = ["item1", "item2", "item3"]

    def get_items(self):
        return self.items

item_manager = ItemManager()

@app.get("/items")
def read_items(manager: ItemManager = Depends(lambda: item_manager)):
    return {"items": manager.get_items()}
3. Использование контекста
Вы можете использовать контекстные менеджеры для управления состоянием. 
Это может быть полезно, если вам нужно управлять ресурсами, 
такими как соединения с базой данных.

Copy code
from fastapi import FastAPI, Depends

app = FastAPI()

class Database:
    def __enter__(self):
        # Инициализация соединения с БД
        self.connection = "Database connection"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Закрытие соединения с БД
        pass

    def get_data(self):
        return ["data1", "data2"]

@app.get("/data")
def read_data(db: Database = Depends(lambda: Database())):
    return {"data": db.get_data()}

4. Использование базы данных
Если ваше приложение требует хранения состояния, рассмотрите возможность 
использования базы данных. Это позволит вам избежать глобальных переменных 
и обеспечит постоянство данных.

python

Verify
Run
Copy code
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    # Используйте db для выполнения запросов к базе данных
    return {"items": ["item1", "item2", "item3"]}

5. Использование состояния приложения
FastAPI позволяет хранить состояние приложения с помощью объекта app.state. 
Это может быть полезно для хранения конфигураций или других данных, 
которые должны быть доступны во всем приложении.

Copy code
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def startup_event():
    app.state.items = ["item1", "item2", "item3"]

@app.get("/items")
def read_items():
    return {"items": app.state.items}


Заключение
Избегание глобальных переменных в FastAPI может значительно улучшить структуру и 
тестируемость вашего кода. Выбор подхода зависит от ваших конкретных требований 
и архитектуры приложения.

=================================
Запуск
1. uvicorn main:app --reload
2. fastapi dev main.py