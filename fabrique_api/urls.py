from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from vacancies_api import views
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'api', views.AddVacancySet, basename='api')
hema_view = get_schema_view(title='Fabrique vacancies API',
                description='An API to store and retrieve data about fabrique vacancies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
