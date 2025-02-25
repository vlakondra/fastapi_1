'''
main module!
'''

import json
from typing import List, Dict, Union
from pydantic import BaseModel

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

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

lst = [1,2,3,4,5]
#События инициализации FastApi
# @app.on_event("startup")
# async def startup() -> None:
#     print("Стартует...")

# @app.on_event("shutdown")
# async def shutdown():
#     print("Закрывается...")

@app.get("/")
async def root():
    ''' Основной маршрут '''
    # print('myid')  # Removed commented out code for better readability
    return 123 #{'data': 123}


def hook(dct):
    d={}
    d['Фамилия'] = dct['fam']
    d['Имя'] = dct['name']
    return d

@app.get("/iterate/{index}")
async def get_item(index: int):
    """
    Получение элемента по индексу с цикличным поведением
    """
    if not lst:
        return {'error': 'Список пуст'}
    actual_index = index % len(lst)
    return {'data': lst[actual_index]}


@app.get("/students/")
async def stud_data():
    '''Возвращает данные о студентах'''
    with open('data/studs.json', 'r', encoding='utf-8') as file:
        json_str = file.read()
        dict_list = json.loads(json_str,object_hook=hook)

    return dict_list


@app.get("/findart/")
async def find_art():
    '''Возвращает интерактивный HTML-файл для поиска исполнителей'''
    return FileResponse('index.html')

@app.get("/artists/{lett}")
async def art_data(lett:str) -> List[Dict]:
    '''Возвращает найденных Исполнителей'''
    art = models['artists']
    query = (art
           .select()
           .where(art.name.startswith(lett))
           .dicts()
    )
    return query

@app.get("/first/{quant}")
async def func_first(quant: int):
    '''тестовая функция'''

    if not isinstance(quant, int) or quant < 0:
        return {'error': 'Параметр должен быть положительным целым числом.'}
    try:
        b = Book('Толстой', 'Author Name')

        if quant > 10:
            raise ValueError('Значение параметра не должно превышать 10')
        return {'param': quant ** 2,"data": b.author}
    except ValueError as e:
        return {'Error': str(e)}

