from django.http import Http404

from .models import Post
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
    queryset = Post.objects.all()  # 모든 퀴즈 문제
    pk_url_kwargs = 'article_id'

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        return queryset.filter(pk=pk).first()  # pk로 검색된 데이터가 있다면 그 중 첫번째 데이터 없다면 None 반환

    def get(self, request, *args, **kwargs):
        problem = self.get_object()
        if not problem:
            raise Http404('invalid id. plz check id')  # 검색된 데이터가 없다면 에러 발생

        ctx = {
            'view': self.__class__.__name__,  # 인스턴스 클래스 명
            'data': problem
        }  # 템플릿에 전달할 데이터

        return self.render_to_response(ctx)


class LearnSQLView(TemplateView):  # SQL 학습 뷰
    template_name = 'learn_sql.html'

    def get(self, request, *args, **kwargs):
        ctx = {}  # 템플릿에 전달할 데이터
        return self.render_to_response(ctx)

# def quiz_page(request, pk):
#   post = get_object_or_404(Post, pk=pk)
#  return render(request, 'DEEPDB/quiz_page.html', {'post': post})
