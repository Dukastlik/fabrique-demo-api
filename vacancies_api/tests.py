from vacancies_api.serializers import VacancySerializer
from vacancies_api.models import Vacancy
from rest_framework import status
from rest_framework.test import APITestCase


class VacancyTest(APITestCase):
    def test_create_vacancy(self):
        url = ('http://localhost:8080/api/')
        data = {
            'title': "Python developer",
            'vacancy_type': "Разработчик",
            'desqription': "тестовое описание",
            'location': "Москва",
            'min_salary': 120000,
            'max_salary': 150000,
        }
        Vacancy.objects.update_or_create(
            title=data['title'],
            vacancy_type=data['vacancy_type'],
            description=data['description'],
            location=data['location'],
            min_salary=data['min_salary'],
            max_salary=data['max_salary']
        )
        data = {
            'stime': "2021-01-11-10",
            'etime': "2021-01-15-10",
        }
        response = self.cliesnt.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vacancy.objects.count(), 1)
        self.assertEqual(response.body.json()[0]['title'], data['title'])
