from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from datetime import datetime
import sys
from vacancies_api.parser import get_vacanies_data
from vacancies_api.models import Timestamp, Vacancy


def update_vacancies_data():
    '''
    Retrieving vacancies from fabrique.studio,
    updating vacancy if already exists, or creating a new one
    '''
    link = settings.FABRIQUE_LINK

    # retrieving data from website
    vacancies = get_vacanies_data(link)
    # creating a timestamp model
    current_time = datetime.now()
    timestamp = Timestamp.objects.create(timestamp=current_time)
    # updating or creating vacancy model
    for v in vacancies:
        vacancy, created = Vacancy.objects.update_or_create(
            title=v['title'],
            vacancy_type=v['vacancy_type'],
            description=v['description'],
            location=v['location'],
            min_salary=v['min_salary'],
            max_salary=v['max_salary']
        )
        timestamp.vacancies.add(vacancy)


def start():
    scheduler = BackgroundScheduler()
    # run this job every hour
    scheduler.add_job(update_vacancies_data,
                      'interval',
                      seconds=10,
                      name='update vacancies data',
                      jobstore='default')

    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
