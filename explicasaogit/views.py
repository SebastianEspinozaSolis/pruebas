from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/explicasaogit/primerosPasos/">Primeros Pasos</a><br></br>
                        <a href="http://127.0.0.1:8000/explicasaogit/vistasApps/">Para crear apps y vistas funcionales</a>''')

def vista1(request):
    html = """
    <h1>para crear proyecto</h1>
    <p>en caso que este todo instalado. django-admin startproject nombreproyecto Para crear el proyecto</p>
    <p>luego para comenzar con git, agregar un archivo .gitignore, donde se colocara *.pyc y *.sqlite3</p>
    <p>con eso añadido, se procede en consola colocar un git init, seguido de un git add .</p>
    <h1>Github</h1>
    <p>Se crea un proyecto en github, se copia el link y se procede con un git remote add origin {link/}</p>
    <p> se usa eso para asegurarse que sea rama main, git branch -m main, y posteriormente se traen los archivos del repositorio con git pull origin main --allow-unrelated-histories</p>
    <p>nuevamente se hace git add . y ahora un git commit -m 'nombre de version'. ahora si se puede subir al respositorio</p>
    <p>eso sera con git push origin main</p>
    <br></br>
    <h1>ahora, para ramas o cambiar de ellas</h1>
    <p>para directamente crear una y cambiar a ella git checkout -b nombre-de-la-rama. pero si se tiene una hecha y solo se quiere cambiar es con git checkout nombre</p>
    <p>con git branch se ven las ramas que hay, en cual se esta, si se le añade un nombre al final se creara una rama con ese nombre</p>
    <p>y para guardar cambios es como antes git commit -m 'nombre version'</p>
    """
    return HttpResponse(html)
def vista2(request):
    html = """
    <h1>Configurar todo y crear apps</h1>
    <p>para hacer andar todo se usa python manage.py runserver. y tocando en el 127.0.0.1:8000 abrira la web</p>
    <p>luego para crear una app hace falta de python manage.py startapp nombreapp</p>
    <p>ahora para conectar eso: en settings de la base colocar 'nombreapp', bajo el ultimo. en urls.py from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('nombreapp/', include('nombreapp.urls')),
    path('admin/', admin.site.urls),
    ]</p>
    <p>Y por parte de la app creada, hay que añadir un archivo llamado urls.py, en el cual se añadira from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('comoSeVeraEnUrl/', views.nombreDeLaVista),
]
</p>
    <p>con eso estara perfe para anclar, ahora, para que en la web se vean titulos o demas sera desde view</p>
    <p>from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, mundo. Esta es la página de inicio de nombreapp.")</p>
    <p>asi debera verse view, siendo  index el nombre de la vista, y en HttpResponse  el argumento en html que se vera, puede ser como esta ahi, o todo metido antes en una variable</p>
    """
    return HttpResponse(html)