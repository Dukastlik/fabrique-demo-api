# fabrique-demo-api
Демонстрационное api на djangorestframework
Позволяет хранить и получать статистику о вакансиях рамещенных на сайте https://fabrique.studio
## Запуск сервиса 
Клонировать проект:  
```git clone https://github.com/Dukastlik/fabrique-demo-api```  
Перейти в директорию fabrique-demo-api:  
```cd avito-statistic-trainee```  
Запустить проект с помощью `docker-compose up`

## Интерфейс
Сервис каждые пол часа обновляет статистику о вакансиях размещенных на сайте https://fabrique.studio и добавляет их в postgresql.
Чтобы получить статистику объявлений за временной промежуток, нужно отправить по адресу http://localhost:8080/api `GET` запрос со словарем вида:
```
{
  "stime": <strating_time>
  "etime": <ending_time>
}
```  
Границы временного промежутка передавать в формате: `YYYY-MM-DD`  
