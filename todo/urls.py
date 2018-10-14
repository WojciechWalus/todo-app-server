from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentation),
    path('api/user/<str:api_request>/<str:app_key>', views.api_request_users),
    path('api/note/<str:api_request>/<str:app_key>', views.api_request_notes)
]
