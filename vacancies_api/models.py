from django.db import models


class Vacancy(models.Model):

    title = models.CharField(max_length=120, unique=True)
    vacancy_type = models.CharField(max_length=120)
    description = models.TextField()
    location = models.CharField(max_length=120)
    min_salary = models.IntegerField(blank=True)
    max_salary = models.IntegerField(blank=True)

    def __str__(self):
        return self.title


class Timestamp(models.Model):

    timestamp = models.DateTimeField()
    vacancies = models.ManyToManyField(Vacancy, related_name="vacancy")

    def __str__(self):
        return str(self.timestamp)