import requests
import pandas as pd
from bs4 import BeautifulSoup



# URL page we will scraping (see image above)
url = "https://www.baseball-reference.com/players/b/bettsmo01.shtml"
# this is the HTML from the given URL
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#id = 'batting_standard'
standard_batting_table = soup.find('table', attrs = {'id' : 'batting_standard'})

for years in standard_batting_table.find_all('tbody'):
    year_array = []
    age_array = []
    team_array = []
    #print(years)
    rows = years.find_all('tr')
    #print(rows)
    for row in rows:
        year_array.append(row.find('th').text)
        age_array.append(row.find('td').text)
        team_array.append(row.find('td', attrs = {'data-stat' : 'team_ID'}).text)
        #print(yr, age, team)

# Create dataframe
final_array = []
for y, a, t in zip(year_array,age_array,team_array):
    final_array.append({'Year': y, 'Age': a, 'Team': t})

df = pd.DataFrame(final_array)
print(df)
