from django.urls import path
from .views import *

app_name = 'notepadapp'


urlpatterns = [
    path('',CustomUserLogin.as_view(),name="login"),
    path('logout/',CustomLogoutView.as_view(),name="logout"),
    path('note_list',Notes_List.as_view(),name="note_list"),
    path('note/create/',Create_Notes.as_view(),name="note_create"),
    path('note/<int:pk>/update/',Update_Notes.as_view(),name="note_update"),
    path('note/<int:pk>/delete/',Delete_Notes.as_view(),name="note_delete"),
    path('note/<int:pk>/',Detail_Notes.as_view(),name="note_detail"),
]
