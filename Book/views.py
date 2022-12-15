from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import DetailView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    posts = list(Post.objects.all())
    posts = [posts[i:i+4] for i in range(0, len(posts), 4)]
    context = {
        'posts': posts
    }
    return render(request, 'Book/home.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as f:
            response = HttpResponse(
                f.read(), content_type='application/File')
            response['Content-Disposition'] = 'attachment; filename' + \
                os.path.basname(file_path)
            return response

    raise Http404


def search(request):
    query = request.GET['query']
    posts = Post.objects.filter(Book_name__icontains=query)
    count = posts.count()
    posts = [posts[i:i+3] for i in range(0, len(posts), 3)]
    context = {
        'posts': posts
    }
    return render(request, 'Book/search.html', context)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
