from django.db import models


class Book(models.Model):
    class GenreChoices(models.TextChoices):
        CRIME = 'C'
        NON_FICTION = 'N'
        OTHER = 'O'
        SCI_FI = 'S'

    name = models.CharField(max_length=100)
    price = models.FloatField()
    number_in_stock = models.PositiveIntegerField(default=0)
    genre = models.CharField(max_length=1, choices=GenreChoices.choices)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'