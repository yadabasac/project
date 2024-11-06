
import pandas as pd
import os

################################
#1. Loading the data
################################

#Data sets used in thie file can be downloaded using Seattle University email account from
#https://redhawks-my.sharepoint.com/:f:/g/personal/yso1_seattleu_edu/EinYTJ-7CdRKkTtXgMQjRgQBiY4eEkGgkFytrsZD7Xto3A?e=okv4Bl


#Change directory to where we will stote the weather data files.
new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data from NOAA"
os.chdir(new_directory)

df0 = pd.read_csv('weather_2018-2023_full data set.csv')

df = df0.copy()

df.isnull().sum(axis=0)

#Replacing null values in Windspeed by 0.
df['Windspeed'] = df['Wind'].str[8:12]
df_wind = df.groupby('Windspeed').size().reset_index(name='Count')
df['Windspeed'] = df['Windspeed'].astype(int)
df.loc[df['Windspeed'] == 9999, 'Windspeed'] = 0
df_wind2 = df.groupby('Windspeed').size().reset_index(name='Count')
df['Windspeed'].isnull().sum(axis=0)

#Replacing null values in Cloudheight by 22000 because this is the mode of cloudheight.
df['Cloudheight'] = df['Cloud'].str[0:5]
df_cloud = df.groupby('Cloudheight').size().reset_index(name='Count')
df['Cloudheight'] = df['Cloudheight'].astype(int)
df.loc[df['Cloudheight'] == 99999, 'Cloudheight'] = 22000
df_cloud2 = df.groupby('Cloudheight').size().reset_index(name='Count')
df['Cloudheight'].isnull().sum(axis=0)

#Replacing null values in Visibility by 16093 because this is the mode of visibility.
df['Visible Distance'] = df['Visibility'].str[0:6]
df_visible = df.groupby('Visible Distance').size().reset_index(name='Count')
df['Visible Distance'] = df['Visible Distance'].astype(int)
df.loc[df['Visible Distance'] == 999999, 'Visible Distance'] = 16093
df_visible2 = df.groupby('Visible Distance').size().reset_index(name='Count')
df['Visible Distance'].isnull().sum(axis=0)

#Replacing null values in air temperature by 228 because this is the mode.
df['Temperate'] = df['Air Temp'].str[0:5]
df_temp = df.groupby('Temperate').size().reset_index(name='Count')
df['Temperate'] = df['Temperate'].astype(int)
df.loc[df['Temperate'] == 9999, 'Temperate'] = 228
df_temp2 = df.groupby('Temperate').size().reset_index(name='Count')
df['Temperate'].isnull().sum(axis=0)

#Replacing null values in rain by 0 because this is the mode.
df.isnull().sum(axis=0)
df2 = df[df['Rain'].isnull()]
df2['Rain2'] = None

df1 = df.dropna(subset=['Rain'])
df1.isnull().sum(axis=0)
df1['Rain2'] = df1['Rain'].str[3:7]
df1_rain = df1.groupby('Rain2').size().reset_index(name='Count')
df1['Rain2'] = df1['Rain2'].astype(int)
df1.loc[df1['Rain2'] == 9999, 'Rain2'] = 0
df1_rain2= df1.groupby('Rain2').size().reset_index(name='Count')
df1['Rain2'].isnull().sum(axis=0)

df = pd.concat([df1, df2], axis=0, ignore_index=True)
df.loc[df['Rain2'].isnull(), 'Rain2'] = 0
df['Rain2'].isnull().sum(axis=0)

#Replacing null values in snow by 0 because this is the mode.
df.isnull().sum(axis=0)
df2 = df[df['Snow'].isnull()]
df2['Snow2'] = None

df1 = df.dropna(subset=['Snow'])
df1.isnull().sum(axis=0)
df1_Snow = df1.groupby('Snow').size().reset_index(name='Count')
df1.loc[df1['Snow'] == 0, 'Snow2'] = 0
df1.loc[df1['Snow'] != 0, 'Snow2'] = df1['Snow'].str[:4]
df1_Snow = df1.groupby('Snow2').size().reset_index(name='Count')
df1['Snow2'] = df1['Snow2'].astype(int)
df1.loc[df1['Snow2'] == 9999, 'Snow2'] = 0
df1_Snow2= df1.groupby('Snow2').size().reset_index(name='Count')
df1['Snow2'].isnull().sum(axis=0)

df = pd.concat([df1, df2], axis=0, ignore_index=True)
df.loc[df['Snow2'].isnull(), 'Snow2'] = 0
df['Snow2'].isnull().sum(axis=0)

#Convert date to Year.
df['date2']=pd.to_datetime (df['DATE'])
df['Year']=df['date2'].dt.year

######################################
#Select only data in 2018, 2019 and 2020 and drop data in 2021, 2022 and 2023
######################################

#Select only 2018, 2019, and 2020.
df1 = df[df['Year'].isin([2018,2019,2020])]

#Obtain date and hour from the original column.
df1['ymd']=df1['date2'].dt.date
df1['HourofDay']=df1['date2'].dt.hour

#Names of airports in the weather data and names of airports in the flight data are different.
#The following csv file tell us the difference in names. 
df_airport = pd.read_csv('weather_airport.csv')

#Merger the weather data with the airport name data.
df1 = pd.merge(df1, df_airport, on='NAME', how='left')

#Create a variable called "AirportTime" containing airport name, data and hour for merging 
#with the flight data later.
df1['AirportTime'] = df1['Ori_Airport_name'] + '_' +  df1['ymd'].astype(str) +  '_' + df1['HourofDay'].astype(str)

# Find rows where values in the AirportTime column are duplicates
df1['duplicate'] = df1.duplicated(subset='AirportTime', keep='first')
df1.loc[df1['duplicate'] == True, 'duplicate'] = None

###Count the number of nulls for each column
df1.isnull().sum(axis=0)
df1 = df1.dropna(subset=['duplicate'])

df1.isnull().sum(axis=0)

#Select only relevant column 
df2= df1[['AirportTime','Windspeed','Cloudheight','Visible Distance','Temperate','Rain2','Snow2']]

df2.isnull().sum(axis=0)

# Specify the file name
file_name = 'weather_2018-2020_v2.csv'

# Writing to CSV file using pandas
df2.to_csv(file_name, index=False)


