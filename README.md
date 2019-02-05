<img src='https://img.shields.io/badge/django2--blue.svg'/><img src='https://img.shields.io/badge/Ajax--red.svg'/><img src='https://img.shields.io/badge/Django%20Rest%20Framework--brightgreen.svg'/>
# Simplest Django Ajax
In this project I am trying to show the simplest MVP to create a backend with drf and consume it with ajax.
With this project, you are avoiding to refresh page to load the posts. 

## Getting Started
* $ git clone https://github.com/victor-s-santos/simplest-django-ajax.git # to clone the repository
* cd simplest-django-ajax # to get in the new directory
* python -m venv .venv # to create the virtual environment
* pip install -r requirements.txt # to install all dependences
* python manage.py migrate # to migrate the models to database
* python manage.py runserverver # to run your local server

### Prerequisites
Python 3.X

## Simple Project Runtime scheme
A little, about the commun way that we develop a rest API and consume it(the idea behind this). 
* ### BackEnd:
	* Install Django and Django Rest Framework;
	* Register in settings.py every apps that you create and register 'rest_framework';
	* Add to project/urls.py:
		* path('api/', views.Get_Perguntas_List.as_view()),
	* In core app, create serializers.py, to 'convert' the model's object in a json(which is a dictionary);
	* In view we use a class based views to make possible to call this serialized data;
	* Locking for https://www.django-rest-framework.org/tutorial/1-serialization/ - to understand serialization; https://www.django-rest-framework.org/api-guide/generic-views/ - to understand how to write the views.py. And, many others important things, like viewsets and routers can be learned reading this wonderful documentation. This is the simplest django ajax system that I could imagine.

* ### FrontEnd:
	* We should use javascript to consume our json format responses. So, it is important know how the data dictionary structure works.
	* In the javascript, we use ajax to make asynchro request. The ajax received principly the url and dataType.  

## Authors 
* **Victor Santos Silva** *

I am looking for make it better in a future as well increment the test system.

