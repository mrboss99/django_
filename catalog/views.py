from django.shortcuts import render

from .models import *


def index(reguest):
    num_books = Book.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status="a").count()
    num_authors = Author.objects.count()


    return render(reguest, 'catalog/index.html',
        context={
            'num_books ': num_books,
            'num_instance_available': num_instance_available,
            'num_author s': num_authors,
        }
    )