from django.contrib import admin
from catalog import models


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', "due_book")


    fieldsets = (
        ('Information',
         {'fields': ('book', 'imprint', 'id')}
         ),

        ('Availability',
         {'fields': ("status", 'due_book')}

         ),
    )

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('date_of_birth', 'date_of_death')
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death') #tarz namayesh nevisandegan
    field = ['first_name','last_name',('date_of_birth', 'date_of_death')] #field = tarz namyesh baraye ADD nevisance