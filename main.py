'''
main module!
'''
from fastapi import FastAPI
# from fastapi.responses import JSONResponse, FileResponse
# from mod import ModelName
# import mod

#https://fastapi.xiniushu.com/ru/

# from peewee import SqliteDatabase
# from playhouse.reflection import generate_models, print_model, print_table_sql

# db = SqliteDatabase('chinook.db', pragmas={'foreign_keys': 1})

# models = generate_models(db)
# art = models['artists']

app = FastAPI(title ="This Is FastAPI")

app = FastAPI()

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author


# @app.on_event("startup")
# async def startup():
#     print("Стартует...")

# @app.on_event("shutdown")
# async def shutdown():
#     print("Закрывается...")

@app.get("/")
async def root():
    '''  root  '''
    # b = Book('zz',['xx'])
    # print(b)
    return {'data':123} ##FileResponse('index.html')




@app.get("/first/{quant}")
async def func_first(quant: int):
    '''тестовая функция'''

    if not isinstance(quant, int) or quant < 0:
        return {'error': 'Input must be a non-negative integer.'}
    try:
        b = Book('zz',[99]) #Аннотация типов не препятствует выполнению при неверном типе значения
        # print(b.author)
        if quant > 10:
            raise ValueError('Input is too big, must be 10 or less.')
        return {'param': quant ** 2,"data": b.author}
    except ValueError as e:
        return {'Error': str(e)}
