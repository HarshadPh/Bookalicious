from django.urls import path, re_path, include
from Book import views as book_view
from django.conf import settings
from django.conf.urls.static import static
from .views import PostDetailView
from django.views.static import serve

urlpatterns = [
    path('', book_view.home, name='book-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='book-detail'),
    path('search', book_view.search, name='search'),
    re_path(r'^download/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
