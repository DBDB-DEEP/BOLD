from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def main_page(request):
    return render(request, 'DEEPDB/main_page.html', {})

def quiz_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'DEEPDB/quiz_page.html', {'post': post})