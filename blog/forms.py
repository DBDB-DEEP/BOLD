from django import forms

from .models import Post

# 폼 이름 (ModelForm)
class PostForm(forms.ModelForm):

    class Meta: # 폼을 만들기 위해 어떤 모델이 사용되는지 알림
        model = Post
        fields = ('title', 'text',)