from django.urls import path
from app1.views import prabhas
app_name='prabhas'
urlpatterns=[
    path('prabhas/',prabhas,name='prabhas')
]