#import the usual suspects
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import time
import random
import requests
from bs4 import BeautifulSoup


#download a bunch of different csv files from various locations on the web, as well as various json files

#download csv from national weather service
url = 'https://www.ncei.noaa.gov/orders/cdo/1158039.csv'
response = requests.get(url)
#put it into the first frame of a pandas dataframe
weather = pd.read_csv(url, skiprows=1)
#rename the columns
weather.columns = ['station', 'date', 'latitude', 'longitude', 'elevation', 'name', 'temp', 'dew', 'sea', 'visibility', 'wind', 'gust', 'precip', 'snow', 'fog', 'rain', 'snowfall', 'thunder', 'tornado']
#drop the columns we don't need
weather = weather.drop(['station', 'latitude', 'longitude', 'elevation', 'name', 'dew', 'sea', 'visibility', 'wind', 'gust', 'precip', 'snow', 'fog', 'rain', 'snowfall', 'thunder', 'tornado'], axis=1)
#convert the date column to a datetime object
weather['date'] = pd.to_datetime(weather['date'])
#set the date column as the index
weather = weather.set_index('date')
#resample the data to be daily
weather = weather.resample('D').mean()
#save the data to a csv file
weather.to_csv('weather.csv')


#download csv from national hurricane center
url = 'https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2018-051019.txt'
response = requests.get(url)
#put it into the first frame of a pandas dataframe
hurricanes = pd.read_csv(url, skiprows=1, header=None)
#rename the columns
hurricanes.columns = ['id', 'name', 'date', 'time', 'record', 'status', 'latitude', 'longitude', 'max_wind', 'min_pressure']
#drop the columns we don't need
hurricanes = hurricanes.drop(['record', 'status', 'max_wind', 'min_pressure'], axis=1)
#convert the date column to a datetime object
hurricanes['date'] = pd.to_datetime(hurricanes['date'])
#set the date column as the index
hurricanes = hurricanes.set_index('date')
#resample the data to be daily
hurricanes = hurricanes.resample('D').mean()
#save the data to a csv file
hurricanes.to_csv('hurricanes.csv')


#download csv from national tornado database
url = 'https://www.spc.noaa.gov/wcm/data/1950-2018_torn.csv'
response = requests.get(url)
#put it into the first frame of a pandas dataframe
tornadoes = pd.read_csv(url, skiprows=1, header=None)
#save the data to a csv file
tornadoes.to_csv('tornadoes.csv')


#download csv from national earthquake database
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
response = requests.get(url)
#put it into the first frame of a pandas dataframe
earthquakes = pd.read_csv(url, skiprows=1, header=None)
#save the data to a csv file
earthquakes.to_csv('earthquakes.csv')


#download csv from national wildfire database
url = 'https://rmgsc.cr.usgs.gov/outgoing/GeoMAC/current_year_fire_data/fire_archive_M6_96619.csv'
response = requests.get(url)
#put it into the first frame of a pandas dataframe
wildfires = pd.read_csv(url, skiprows=1, header=None)
#save the data to a csv file
wildfires.to_csv('wildfires.csv')

#download csv from national flood database
url = 'https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=mlrf2&output=csv'
response = requests.get(url)
#put it into the first frame of a pandas dataframe
floods = pd.read_csv(url, skiprows=1, header=None)
#save the data to a csv file
floods.to_csv('floods.csv')

#download csv from national drought database
url = 'https://www.ncdc.noaa.gov/drought/monitor/monitor.csv'
response = requests.get(url)
#put it into the first frame of a pandas dataframe
droughts = pd.read_csv(url, skiprows=1, header=None)
#save the data to a csv file
droughts.to_csv('droughts.csv')

#download csv from national landslide database
url = 'https://www.ngdc.noaa.gov/hazard/landslide_data.shtml'
response = requests.get(url)
#parse the html
soup = BeautifulSoup(response.text, 'html.parser')
#find the table
table = soup.find('table')
#find the rows
rows = table.find_all('tr')
#find the columns
columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]
#put the data into a pandas dataframe
landslides = pd.DataFrame(columns=columns)
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    if len(tds) == 5:
        values = [tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text.replace('\n', '')]
    else:
        values = [td.text.replace('\n', '') for td in tds]
    landslides = landslides.append(pd.Series(values, index=columns), ignore_index=True)
#save the data to a csv file
landslides.to_csv('landslides.csv')

#download csv from national volcanic eruption database
url = 'https://www.ngdc.noaa.gov/hazard/volcano_data.shtml'
response = requests.get(url)
#parse the html
soup = BeautifulSoup(response.text, 'html.parser')
#find the table
table = soup.find('table')
#find the rows  
rows = table.find_all('tr')
#find the columns
columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]
#put the data into a pandas dataframe
volcanoes = pd.DataFrame(columns=columns)
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    if len(tds) == 5:
        values = [tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text.replace('\n', '')]
    else:
        values = [td.text.replace('\n', '') for td in tds]
    volcanoes = volcanoes.append(pd.Series(values, index=columns), ignore_index=True)
#save the data to a csv file
volcanoes.to_csv('volcanoes.csv')

