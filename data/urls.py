from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = "index"),
    path('create', views.create, name = "create"),
    path('update/<str:id>', views.update, name = "update"),
    path('delete/<str:id>', views.delete, name = "delete")
]