'''
main module!
'''

import json
from typing import List, Dict

#Модули FastApi
from fastapi import FastAPI
from fastapi.responses import  FileResponse

#Модули PeeWee
from peewee import SqliteDatabase
from playhouse.reflection import generate_models#, print_model, print_table_sql

#Инициализация базы данных
db = SqliteDatabase('chinook.db', pragmas={'foreign_keys': 1})
models = generate_models(db)

app = FastAPI(title ="This Is FastAPI")

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

#События инициализации FastApi
@app.on_event("startup")
async def startup():
    print("Стартует...")

@app.on_event("shutdown")
async def shutdown():
    print("Закрывается...")

@app.get("/")
async def root():
    '''  Основной маршрут  '''
    return  {'data':123}

@app.get("/students/")
async def stud_data():
    '''Возвращает данные о студентах'''
    with open('data/studs.json', 'r', encoding='utf-8') as file:
        json_str = file.read()
        dict_list = json.loads(json_str)

    return dict_list


@app.get("/findart/")
async def find_art():
    '''Возвращает интерактивный HTML-файл для поиска исполнителей'''
    return FileResponse('index.html')

@app.get("/artists/{firsts}")
async def art_data(firsts:str) -> List[Dict]:
    '''Возвращает найденных Исполнителей'''
    art = models['artists']
    query = (art
           .select()
           .where(art.name.startswith(firsts))
           .dicts()
    )
    return list(query)

@app.get("/first/{quant}")
async def func_first(quant: int):
    '''тестовая функция'''

    if not isinstance(quant, int) or quant < 0:
        return {'error': 'Параметр должен быть положительным целым числом.'}
    try:
        b = Book('Толстой',[99]) #Аннотация типов не препятствует выполнению при неверном типе значения

        if quant > 10:
            raise ValueError('Значение параметра не должно превышать 10')
        return {'param': quant ** 2,"data": b.author}
    except ValueError as e:
        return {'Error': str(e)}
