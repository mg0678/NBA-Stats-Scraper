from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2024_totals.html'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

table = soup.find('table', class_='stats_table')

data_list = []

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')

    if columns != []:
        Player = columns[0].text.strip()
        Tm = columns[3].text.strip()
        PTS = columns[28].text.strip()

        data_list.append({'Player': Player, 'Tm': Tm, 'PTS': PTS})

df = pd.DataFrame(data_list)

print(df.head())
