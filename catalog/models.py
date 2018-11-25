from django.db import models
import uuid
class Gener(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_dead = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    summary = models.CharField(max_length=1000, help_text="kholase i az ketab")
    gener = models.ManyToManyField(Gener,help_text="yek gener baraye ketam khood entekhab konid")
    isbn= models.CharField('ISBN',max_length=13, help_text= "13 character <a href= ")





    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="dadane 'id' be yek ketaab khas ")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_book = models.DateTimeField(null=True, blank=True)

    LOAN_STATUS=(
        ("m", "Maintenance"),
        ("o", "Onloan"),
        ("a", "Availbale"),
        ("r", "Reversed")
    )
    status=models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, help_text="yek vaziat baraye ketab mored nazar entekhab konid")

    class Meta:
        ordering= ["due_book"]

        def __str__(self):
            return '%s, %s' % (self.id, self.book.title)
