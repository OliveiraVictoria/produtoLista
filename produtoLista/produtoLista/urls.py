from produtoLista import views
from django.urls import path

urlpatterns = [
    path('Hello/', views.hello_world),
]