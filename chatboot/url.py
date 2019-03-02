from django.contrib import admin
from django.urls import path

from chatboot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name="index"),
    path('',views.chat,name="chat"),
    path('chat/', views.chat, name="chat"),
]
