from django.conf.urls import url
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UsersViewSet, basename="users")


app_name = 'todos'

urlpatterns = [
    path('todos/', views.HomeView.as_view()),
    path('task-list/', views.HomeView.as_view()),
    url('', include(router.urls))
]
