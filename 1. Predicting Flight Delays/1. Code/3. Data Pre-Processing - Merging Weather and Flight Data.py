import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

################################
#6. Merging with the weather dataset
################################

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data from DOT"
os.chdir(new_directory)

#Loading the flight dataset
df8 = pd.read_csv('flight_6al_2018-2020.csv')

#Create a new variable "AirportTime" so that we can use it to merge with the weather data.
df8['FlightDate2'] = pd.to_datetime(df8['FlightDate'])
df8['DepHour'] = df8['DepTimeBlk'].str[:2]
df8['DepHour'] = df8['DepHour'].astype(int)
df8['Depymd']=df8['FlightDate2'].dt.date
df8['AirportTime'] = df8['Ori_Airport_name'] + '_' +  df8['Depymd'].astype(str) +  '_' + df8['DepHour'].astype(str)


new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data from NOAA"
os.chdir(new_directory)

#Loading the weather dataset.
df_weather = pd.read_csv('weather_2018-2020_v2.csv')

#Create new column names
new_column_names = {
    'Windspeed': 'Ori_Windspeed',
    'Cloudheight': 'Ori_Cloudheight',
    'Visible Distance': 'Ori_Visible Distance',
    'Temperate': 'Ori_Temperature',
    'Rain2': 'Ori_Rain',
    'Snow2': 'Ori_Snow'
}
# Renaming columns using the rename() function
df_weather.rename(columns=new_column_names, inplace=True)

#Merging the two datasets to get weather information at the origin airports.
df11 = pd.merge(df8, df_weather, on='AirportTime', how='left')

df11.isnull().sum(axis=0)

#Getting weather data for destination airports
#Create a new variable "AirportTime" so that we can use it to merge with the weather data.
df11['ArrHour'] = df11['ArrTimeBlk'].str[:2]
df11['ArrHour'] = df11['ArrHour'].astype(int)
df11['Arrymd']=df11['FlightDate2'].dt.date
#If arrival hour is ealier than departure hour then arrival data must be the next day.
df11.loc[df11['ArrHour'] >= df11['DepHour'], 'Arrymd'] = df11['Arrymd']
df11.loc[df11['ArrHour'] < df11['DepHour'], 'Arrymd'] = df11['Arrymd'] + timedelta(days=1)
df11['AirportTime'] = df11['Dest_Airport_name'] + '_' +  df11['Arrymd'].astype(str) +  '_' + df11['ArrHour'].astype(str)

#Loading the weather dataset again.
df_weather = pd.read_csv('weather_2018-2020_v2.csv')
#Create new column names
new_column_names = {
    'Windspeed': 'Dest_Windspeed',
    'Cloudheight': 'Dest_Cloudheight',
    'Visible Distance': 'Dest_Visible Distance',
    'Temperate': 'Dest_Temperature',
    'Rain2': 'Dest_Rain',
    'Snow2': 'Dest_Snow'
}
# Renaming columns using the rename() function
df_weather.rename(columns=new_column_names, inplace=True)

#Merging the two datasets to get weather information at the destination airports.
df11 = pd.merge(df11, df_weather, on='AirportTime', how='left')

#Select only relevant column 
df11= df11[['Year','Month','DayofMonth', 'DayOfWeek', 'Airline_name', 'Ori_Airport_name', 'Dest_Airport_name', 'DepTimeBlk', 
          'ArrTimeBlk', 'ArrDelayMinutes','ArrDel15','Ori_Windspeed','Ori_Cloudheight','Ori_Visible Distance','Ori_Temperature',
          'Ori_Rain','Ori_Snow','Dest_Windspeed','Dest_Cloudheight','Dest_Visible Distance','Dest_Temperature','Dest_Rain','Dest_Snow']]

df11.isnull().sum(axis=0)

df12 = df11[df11.isnull().any(axis=1)]

#Drop all rows with null values
df11.dropna(axis=0, how='any',inplace=True)

df11.isnull().sum(axis=0)

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data_Model"
os.chdir(new_directory)

# Specify the file name
file_name = 'flight_weather_2018-2020.csv'

# Writing to CSV file using pandas
df11.to_csv(file_name, index=False)
