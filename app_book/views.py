from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# from .forms import BookNameFilterForm
from .serializers import BookSerializer
from app_book.models import Book
from app_book.filters import BookFilter


# Create your views here.
def index(request):
    # name = request.GET.get('name')
    # books = Book.objects.all()
    # if name:
    #     books = books.filter(name__icontains=name)
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = {
        'form': book_filter.form,
        'books': book_filter.qs,
    }
    return render(request,'index.html', context)


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
