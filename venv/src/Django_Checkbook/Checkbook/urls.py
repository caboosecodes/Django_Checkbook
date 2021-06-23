# this urls.py file was created; it was not made automatically like Django_Checkbook\urls.py

from django.urls import path
# . looks within the same directory
from . import views

#
urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction'),
]