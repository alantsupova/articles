from django.db import models


class Magazine(models.Model):
    "Модель журнал"
    title = models.CharField(max_length=250)
    website = models.URLField()
    year = models.IntegerField()
    tom = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.surname} {self.name}'


class KeyWords(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.word}'


class Article(models.Model):
    title = models.CharField(max_length=255)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    pages = models.IntegerField()
    keywords = models.ManyToManyField(KeyWords, related_name='article')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'





