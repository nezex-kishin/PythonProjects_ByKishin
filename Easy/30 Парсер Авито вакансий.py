import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.avito.ru/amurskaya_oblast_blagoveschensk/vakansii'
r = requests.get(url)
soup = bs(r.content, "html.parser")
vacancies_names = soup.find('div', class_='items-items-kAJAg')
zp = soup.find_all('meta',itemprop="price")

i = 0
for name in vacancies_names:
    print(name.a['title'])
    print(f"avito.ru{name.a['href']}")
    if zp[i]['content'] == '0':
        print('Средняя ЗП: Не указано\n')
    elif int(zp[i]['content']) < 10000:
        print('Средняя ЗП:', zp[i]['content'], 'за смену\n')
    else:
        print('Средняя ЗП:',zp[i]['content'],'\n')
    i += 1

