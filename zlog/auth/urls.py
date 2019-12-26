from django.urls import path
from .views import auth_view_test

urlpatterns = [
    path('test', auth_view_test, name='test_page'),
]
