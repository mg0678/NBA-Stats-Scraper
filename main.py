from bs4 import BeautifulSoup
import requests
import pandas as pd

def perGameOrTotal():
    stat_pg_tot = 0
    while stat_pg_tot not in ['1','2']:
        stat_pg_tot = input('Get Stats\n1. Per Game\n2. Season Totals\n')
    if stat_pg_tot == '1':
        url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'
    else:
        url = 'https://www.basketball-reference.com/leagues/NBA_2024_totals.html'
    return url

url = perGameOrTotal()

data = requests.get(url,verify=False).text
soup = BeautifulSoup(data, 'html.parser')

table = soup.find('table', class_='stats_table')

stat = 'x'

def pickStat(stat,answer):
    while answer not in ['1', '2', '3', '4']:
        answer = input('Pick a stat\n1. AST\n2. STL\n3. BLK\n4. PTS\n')
    
    if answer == '1':
        stat = 'AST'
    elif answer == '2':
        stat = 'STL'    
    elif answer == '3':
        stat = 'BLK'
    else:
        stat = 'PTS'
    return stat

data_list = []

selected_stat = pickStat(stat, answer=0)

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')

    if columns != []:
        Player = columns[0].text.strip()
        Tm = columns[3].text.strip()

        if selected_stat == 'AST':
            stat_value = columns[23].text.strip()
        elif selected_stat == 'STL':
            stat_value = columns[24].text.strip()
        elif selected_stat == 'BLK':
            stat_value = columns[25].text.strip()
        else:
            stat_value = columns[28].text.strip()

        data_list.append({'Player': Player, 'Tm': Tm, selected_stat: stat_value})

df = pd.DataFrame(data_list)

# Convert the selected_stat column to numeric and sort
df[selected_stat] = pd.to_numeric(df[selected_stat])
df = df.sort_values(by=selected_stat, ascending=False)

# Reset Index to start at 1
df = df.reset_index(drop=True)
df.index += 1

# Print top 20
print(df.head(20))
