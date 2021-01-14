import requests, re
from bs4 import BeautifulSoup


link = "https://fabrique.studio/vacancies/"


def get_vacanies_data(link: str) -> list:
    '''
    Parsing vacancy data from fabrique website
    returning list of Vacancy models 
    '''

    resp = requests.get(link)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    test = soup.find('div', {"class":"vacancy__content"})

    vacancies = []

    for vac in test.children:
        vac_title = vac.find(class_="vacancy__block-title").string
        vac_group = vac['group']
        vac_salaries = re.findall(r'\d+ \d+', vac.find(class_="vacancy__block-price").string)
        vac_minsalry = int(vac_salaries[0].replace(' ', ''))
        vac_maxsalary = int(vac_salaries[1].replace(' ', ''))
        vac_description = vac.p.string
        vac_location = vac.find_all('span')[1].string
        v = {"title": vac_title,
             "vacancy_type": vac_group,
             "description": vac_description,
             "location": vac_location,
             "min_salary": vac_minsalry,
             "max_salary": vac_maxsalary,
        }
        vacancies.append(v)
    return vacancies
