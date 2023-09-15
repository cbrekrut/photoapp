from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('profile/', views.user_profile, name='user_profile'),
    # Добавьте другие маршруты по мере необходимости
]