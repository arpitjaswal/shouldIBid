import requests

from bs4 import BeautifulSoup


data=requests.get("https://www.investorgain.com/report/live-ipo-gmp/331/current/?sort=GMP%28%E2%82%B9%29desc&page=1")

soup = BeautifulSoup(data.content,'lxml')
table= soup.find('table')


data=[]
for row in table.find_all('tr'):
    columns=row.find_all('td')
    for col in columns:
        row_data=col.get_text(strip=True)
        print(row_data)
        data.append(row_data)

print("Following IPO are currently Open or Upcoming: ")

for row in data:
    print(row)
    if row[0]:name=row[0];
    if row[7]:open_date=row[7]
    print("{name} {open_date}")
    

