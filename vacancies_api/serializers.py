from vacancies_api.models import Vacancy, Timestamp
from rest_framework import serializers


class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = ('title',
                  'vacancy_type',
                  'description',
                  'location',
                  'min_salary',
                  'max_salary',
                  )


class TimestampSerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(read_only=True, many=True)

    class Meta:
        model = Timestamp
        fields = ('timestamp', 'vacancies')
