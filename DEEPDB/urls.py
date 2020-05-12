from django.urls import path
from .views import QuizView, MainPageView, LearnSQLView

# view에 정의된 함수를 불러 오는 곳
# 누군가가 http://127.0.0.1:8000/ 주소로 들어오면 views.post_list를 보여줌

urlpatterns = [
    path('learn/', LearnSQLView.as_view(), name='learnSQL'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('', MainPageView.as_view(), name='home'),
    path('home/', MainPageView.as_view(), name='home'),
]
