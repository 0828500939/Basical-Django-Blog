from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='blog'),  # Đường dẫn cho trang danh sách
    path('<int:id>/', views.post, name='post'),
]