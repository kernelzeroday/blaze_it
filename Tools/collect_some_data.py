#import requests, beautifulsoup4, pandas, numpy, matplotlib, seaborn, sklearn
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import time
import random

# Get the data from the website
url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get the table
table = soup.find('table', {'id': 'per_game_stats'})

# Get the headers
headers = [th.getText() for th in table.findAll('tr', limit=2)[0].findAll('th')]
headers = headers[1:]

#download a bunch of different csv files and then combine them
urls = [ 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2018_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2017_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2016_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2015_per_game.html',
        'https://www.basketball-reference.com/leagues/NBA_2014_per_game.html',
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'per_game_stats'})
    headers = [th.getText() for th in table.findAll('tr', limit=2)[0].findAll('th')]
    headers = headers[1:]
    rows = table.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]
    stats = pd.DataFrame(player_stats, columns = headers)
    stats.to_csv('nba_stats_' + url[-12:-5] + '.csv', index=False)
    time.sleep(random.randint(1,5))

# Combine the csv files
nba_2019 = pd.read_csv('nba_stats_2019.html')
nba_2018 = pd.read_csv('nba_stats_2018.html')
nba_2017 = pd.read_csv('nba_stats_2017.html')
nba_2016 = pd.read_csv('nba_stats_2016.html')
nba_2015 = pd.read_csv('nba_stats_2015.html')
nba_2014 = pd.read_csv('nba_stats_2014.html')

nba_stats = pd.concat([nba_2019, nba_2018, nba_2017, nba_2016, nba_2015, nba_2014], ignore_index=True)

# Clean the data

# Remove the rows with missing values
nba_stats = nba_stats.dropna()

# add random values into random rows in the data
nba_stats['PTS'] = nba_stats['PTS'].astype(float)
nba_stats['PTS'] = nba_stats['PTS'].apply(lambda x: x + random.randint(0, 10))

# Save the data
nba_stats.to_csv('nba_stats.csv', index=False)
