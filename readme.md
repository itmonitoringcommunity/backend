##INSTALL VISUALSTUDIO CODE
Configure system environment on Windows OS
Download Pyhton from visualstudio code extensions

## Tricks [on Windows OS]

```
-- backend folder right click open in terminal

python -m pip install --upgrade pip

pip list
pip install pep8
pip install autopep8
pip install pylint
pip install django
pip install djangorestframework

PS D:\AdminPanel\backend> . env/Scripts/activate.bat

PS D:\AdminPanel\backend> django-admin startproject djreact
--change backend\djreact => backend\src
--create .vscode folder and set settings.json

-- backend/src folder right click open in terminal
python manage.py runserver
python manage.py migrate
python manage.py runserver
http://127.0.0.1:8000/
python manage.py startapp articles

--backend/src/djreact/settings.py
INSTALLED_APPS = [ 
    'rest_framework',
    'articles'
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

--backend/src/djreact/urls.py
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls)
]

python src/manage.py runserver

--backend/src/articles/models.py
class Artical(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

python manage.py makemigrations
python manage.py migrate

--backend/src/articles/admin.py
from .models import Article
admin.site.Register(Article)

python manage.py createsuperuser
admin
admin
python manage.py runserver
http://127.0.0.1:8000/admin/login/
