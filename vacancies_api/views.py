from vacancies_api.models import Vacancy, Timestamp
from vacancies_api.serializers import TimestampSerializer, VacancySerializer

from rest_framework import status, viewsets


class AddVacancySet(viewsets.ModelViewSet):
    '''
    Returns Timestamp json response for given time period
    '''
    queryset = Timestamp.objects.all()
    serializer_class = TimestampSerializer

    def get_queryset(self):
        '''
        Restricts query by filtering against the datetime range
        '''
        queryset = Timestamp.objects.all()
        start_time = self.request.query_params.get('stime', None)
        end_time = self.request.query_params.get('etime', None)
        if start_time is not None:
            start_time = start_time.title()
            queryset = queryset.filter(timestamp__range=[start_time, end_time])
        return queryset
