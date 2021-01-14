from django.test import TestCase
from vacancies_api.serializers import VacancySerializer
from vacancies_api.models import Vacancy


class VacancySerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        vacancy = Vacancy()
        serializer = VacancySerializer()
        for field_name in [
            'title', 'vacancy_type', 'description', 'location', 'min_salary', 'max_salary',
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(vacancy, field_name)
            )