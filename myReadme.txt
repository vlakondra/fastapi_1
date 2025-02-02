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