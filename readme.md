## backend

This application includes web api of bulletin with django rest-framework. It is possible to integrate different development platforms.

## FIRST

* Configure system environment on Windows OS
* Download Pyhton from visualstudio code extensions
* Download npm from visualstudio code extensions

## SECOND

```
-- backend folder right click open in terminal

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python -m venv env
. env/Scripts/activate.bat

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
admin
admin

python manage.py dumpdata --indent=4 > dumped_data.json
python manage.py loaddata < dumped_data.json

python manage.py runserver
http://127.0.0.1:8000/admin/login/

http://127.0.0.1:8000/api/
http://127.0.0.1:8000/mails/
http://127.0.0.1:8000/types/
http://127.0.0.1:8000/priorities/
http://127.0.0.1:8000/states/
http://127.0.0.1:8000/bulletins/
http://127.0.0.1:8000/agents/



```


## FORTH

```

docker build -t backend .
docker run -it backend
docker rmi backend .

```
