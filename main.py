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
    '''
    root
    '''
    return {'data':123} ##FileResponse('index.html')


@app.get("/first/{quant}")
async def func_first(quant:int):
    '''тестовая функция'''
    return {'param':quant**2}


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
