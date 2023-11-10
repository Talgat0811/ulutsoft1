from django.contrib import admin
from django.urls import path

import chat.views
from chat.views import index
from chat.views import save_text_to_database

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('save_text_to_database/', save_text_to_database, name='save_text_to_database'),
]
