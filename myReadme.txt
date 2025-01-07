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