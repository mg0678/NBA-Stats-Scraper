from bs4 import BeautifulSoup
import requests
import pandas as pd
from functions import perGameOrTotal, pickStat, teamSelection

again = 'y'
while again != 'n':
    url = perGameOrTotal()

    data = requests.get(url,verify=False).text
    soup = BeautifulSoup(data, 'html.parser')

    table = soup.find('table', class_='stats_table')

    data_list = []

    selected_stat = pickStat()

    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')

        if columns != []:
            Player = columns[0].text.strip()
            Tm = columns[3].text.strip()

            if selected_stat == 'AST':
                stat_value = columns[23].text.strip()
            elif selected_stat == 'REB':
                stat_value = columns[22].text.strip()
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

    byTeam = 0
    while byTeam not in ['1','2']:
       byTeam = input('1. Team Leaders:\n2. League Leaders:\n')

    # Reset Index to start at 1
    df = df.reset_index(drop=True)
    df.index += 1

    if byTeam == '1':
        print(df.loc[df['Tm'] == teamSelection()])
    else:
       print(df.head(20))

    again = input("Search again? [y/n]:")
    again = again.lower()
    while again not in ['y','n']:
        print('Invalid input\n')
        again = input("Search again? [y/n]:")
        again = again.lower()
