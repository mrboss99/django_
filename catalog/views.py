from django.shortcuts import render
from django.views import generic
from .models import *


#CLASS BASE VIEW

class Index(generic.TemplateView):

    template_name = "catalog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] =Book.objects.all().count()
        context['num_instance_available '] =BookInstance.objects.filter(status="a").count()
        context['num_authors '] =Author.objects.count()


class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/book_list.html"


class BoolDetailView(generic.DeleteView):
    model = Book

    template_name = "catalog/book_detail.html"










#FUNCTION BASE VIEW


#def index(reguest):
#  num_books = Book.objects.all().count()
#    num_instance_available = BookInstance.objects.filter(status="a").count()
#    num_authors = Author.objects.count()


#    return render(reguest, 'catalog/index.html',
#        context={
#            'num_books ': num_books,
#            'num_instance_available': num_instance_available,
#            'num_author s': num_authors,
#        }
#    )