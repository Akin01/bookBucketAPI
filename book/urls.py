from django.urls import path
from . import views

urlpatterns = [
    path("", views.allBook, name="all-book-list"),
    path("book/<str:pk>",views.Book, name="get-book"),
    path("edit-book/<str:pk>", views.editBook, name="edit-book"),
]
