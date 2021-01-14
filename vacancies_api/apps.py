from django.apps import AppConfig


class VacanciesApiConfig(AppConfig):
    name = 'vacancies_api'

    def ready(self):
        from vacancies_api import scheduler
        scheduler.start()
