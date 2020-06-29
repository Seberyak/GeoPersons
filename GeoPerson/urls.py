from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('API.urls')),
    path('',  views.index)
]
