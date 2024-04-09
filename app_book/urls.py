from django.urls import path

from .views import BookListView, BookListAPIView

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('api/', BookListAPIView.as_view())
]