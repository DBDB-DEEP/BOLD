from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


# Create your views here.
# template_name을 정의하면 장고에서는 자동으로 앱 디렉토리의 templates 디렉토리를 참조한다고 한다
class MainPageView(TemplateView):  # 메인페이지
    template_name = 'main_page.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)


class QuizView(TemplateView):  # 게시글 목록
    template_name = 'quiz_page.html'
    # queryset = Post.objects.all()  # 모든 퀴즈 문제

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)


class LearnSQLView(TemplateView):  # SQL 학습 뷰
    template_name = 'learn_sql.html'
    
    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)

# def quiz_page(request, pk):
#   post = get_object_or_404(Post, pk=pk)
#  return render(request, 'DEEPDB/quiz_page.html', {'post': post})
