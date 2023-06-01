from django.urls import path
from app2.views import pawan
app_name='pawan'
urlpatterns=[
    path('pawan/',pawan,name='pawan')
]