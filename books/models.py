from django.db import models


class Genre(models.Model):
    title_of_genre = models.CharField('Жанр', max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Author(models.Model):
    full_name = models.CharField('ФИО автора', max_length=120)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    title_of_book = models.CharField('Название', max_length=120)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
