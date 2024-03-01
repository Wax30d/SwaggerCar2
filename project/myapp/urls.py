from .views import ProductApi
from django.urls import path
urlpatterns = [
    path('api', ProductApi.as_view()),
]