
from django.urls import path
from .views import blog_view
from .views import blog_view2
urlpatterns = [
    path('posts/', blog_view, name='blog_posts'),
    path('page2', blog_view2, name='test'),
]
