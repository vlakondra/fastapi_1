'''
main module!
'''
from fastapi import FastAPI
# from fastapi.responses import JSONResponse, FileResponse
# from mod import ModelName
# import mod

# from peewee import SqliteDatabase
# from playhouse.reflection import generate_models, print_model, print_table_sql

# db = SqliteDatabase('chinook.db', pragmas={'foreign_keys': 1})

# models = generate_models(db)
# art = models['artists']

app = FastAPI(title ="This Is FastAPI")

app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     print("Стартует...")

# @app.on_event("shutdown")
# async def shutdown():
#     print("Закрывается...")

@app.get("/")
async def root():
    '''  root  '''
    return {'data':123} ##FileResponse('index.html')


@app.get("/first/{quant}")
async def func_first(quant: int):
    '''тестовая функция'''
    if not isinstance(quant, int) or quant < 0:
        return {'error': 'Input must be a non-negative integer.'}
    try:
        if quant > 10:
            raise ValueError('Input is too big, must be 10 or less.')
        return {'param': quant ** 2}
    except ValueError as e:
        return {'Error': str(e)}
