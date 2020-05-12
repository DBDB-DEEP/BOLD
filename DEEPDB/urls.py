from django.urls import path    # 장고 함수
from . import views             # 애플리케이션에서 사용할 모든 view 포함

# 누군가가 http://127.0.0.1:8000/ 주소로 들어오면 views.post_list를 보여줌
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('post/<int:pk>/', views.quiz_page, name='quiz_page'),
]
