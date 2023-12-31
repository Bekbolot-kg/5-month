from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.authorization_view),
    path('register/', views.register_view),
    path('confirm/', views.confirm_user, name='confirm'),
]
