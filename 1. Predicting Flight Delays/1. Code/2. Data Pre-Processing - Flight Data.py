
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

################################
#1. Loading the data
################################

#Data sets used in thie file can be downloaded using Seattle University email account from
#https://redhawks-my.sharepoint.com/:f:/g/personal/yso1_seattleu_edu/EinYTJ-7CdRKkTtXgMQjRgQBiY4eEkGgkFytrsZD7Xto3A?e=okv4Bl

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data from DOT"
os.chdir(new_directory)

#Loading the dataset
df = pd.read_csv('flight data 2018_2020.csv')
#Loading the dataset containing airport ID and airport full names
df_ori_airport = pd.read_csv('L_AIRPORT.csv')
#Loading the dataset containing airline ID and airline full names
df_airline = pd.read_csv('L_UNIQUE_CARRIERS.csv')


################################
#2. Merging the data
################################

#Make of a copy of the dataset
df_Dest_airport = df_ori_airport.copy()

#Create new column names
new_column_names = {
    'Code': 'Reporting_Airline',
    'Description': 'Airline_name'
}
# Renaming columns using the rename() function
df_airline.rename(columns=new_column_names, inplace=True)

#Create new column names
new_column_names = {
    'Code': 'Origin',
    'Description': 'Ori_Airport_name'
}
# Renaming columns using the rename() function
df_ori_airport.rename(columns=new_column_names, inplace=True)

new_column_names = {
    'Code': 'Dest',
    'Description': 'Dest_Airport_name'
}
# Renaming columns using the rename() function
df_Dest_airport.rename(columns=new_column_names, inplace=True)

# Merging the two datasets so that we have airport full names and airline full names in df 
df = pd.merge(df, df_airline, on='Reporting_Airline', how='left')
df = pd.merge(df, df_ori_airport, on='Origin', how='left')
df = pd.merge(df, df_Dest_airport, on='Dest', how='left')


# #Select only relevant columns
df2 = df[['Year','Month','DayofMonth', 'FlightDate','DayOfWeek', 'Airline_name', 'Ori_Airport_name', 'Dest_Airport_name', 'DepTimeBlk', 'ArrTimeBlk', 'DepDel15','ArrDel15','ArrDelayMinutes','Diverted']]

###Count the number of nulls for each column
df2.isnull().sum(axis=0)
#If a flight is Diverted, then change the value of ArrDel15 to 1.
df2.loc[(df2['ArrDel15'].isnull()) & (df2['Diverted'] == 1), 'ArrDel15'] = 1
#Drop all rows with null values
df2.dropna(axis=0, how='any',inplace=True)
df2.isnull().sum(axis=0)

################################
#3. Exploring the data before selecting airlines
################################

#Create a copy of the data set
df3 = df2.copy()

#Restrict data to only flights with delayed departure
df4 = df3[df3['DepDel15'] == 1]
#Restrict data to only flights with delayed arrival
df5 = df3[df3['ArrDel15'] == 1]

df3['DepDel15'].value_counts()
df3['ArrDel15'].value_counts()


#3.1 Exploring variables

#Calculate number of flights and delayed flights in each Year
df3_Year = df3.groupby('Year').size().reset_index(name='Count')
df5_Year = df5.groupby('Year').size().reset_index(name='Delay Count')
df3_Year = pd.merge(df3_Year, df5_Year, on='Year', how='left')
df3_Year['Year Delay Ratio'] = round(df3_Year['Delay Count'] / df3_Year['Count'],3) 

#Calculate number of flights and delayed flights in each Month
df3_Month = df3.groupby('Month').size().reset_index(name='Count')
df5_Month = df5.groupby('Month').size().reset_index(name='Delay Count')
df3_Month = pd.merge(df3_Month, df5_Month, on='Month', how='left')
df3_Month['Month Delay Ratio'] = round(df3_Month['Delay Count'] / df3_Month['Count'],3) 

#Calculate number of flights and delayed flights in each day of Month
df3_DayofMonth = df3.groupby('DayofMonth').size().reset_index(name='Count')
df5_DayofMonth = df5.groupby('DayofMonth').size().reset_index(name='Delay Count')
df3_DayofMonth = pd.merge(df3_DayofMonth, df5_DayofMonth, on='DayofMonth', how='left')
df3_DayofMonth['DayofMonth Delay Ratio'] = round(df3_DayofMonth['Delay Count'] / df3_DayofMonth['Count'],3) 

#Calculate number of flights and delayed flights in each day of week
df3_dofweek = df3.groupby('DayOfWeek').size().reset_index(name='Count')
df5_dofweek = df5.groupby('DayOfWeek').size().reset_index(name='Delay Count')
df3_dofweek = pd.merge(df3_dofweek, df5_dofweek, on='DayOfWeek', how='left')
df3_dofweek['dofweek Delay Ratio'] = round(df3_dofweek['Delay Count'] / df3_dofweek['Count'],3) 

#Calculate number of flights and delayed flights of each airline
df3_airline = df3.groupby('Airline_name').size().reset_index(name='Count')
df5_airline = df5.groupby('Airline_name').size().reset_index(name='Delay Count')
df3_airline = pd.merge(df3_airline, df5_airline, on='Airline_name', how='left')
df3_airline['airline Delay Ratio'] = round(df3_airline['Delay Count'] / df3_airline['Count'],3) 
df3_airline = df3_airline.sort_values(by='Count', ascending=False)
df3_airline.reset_index(drop=True, inplace=True)
# Calculate the sum of each column and create a new row
sum_row = pd.Series(df3_airline.sum(), name='Total')
# Append the new row to the DataFrame
df3_airline = df3_airline.append(sum_row)

#Calculate number of flights and delayed flights of each Origin airport. Here, we use df4 instead of df5
#because we are counting number of delayed departure, not delayed arrival.
df3_Ori_Airport_name = df3.groupby('Ori_Airport_name').size().reset_index(name='Count')
df4_Ori_Airport_name = df4.groupby('Ori_Airport_name').size().reset_index(name='Delay Count')
df3_Ori_Airport_name = pd.merge(df3_Ori_Airport_name, df4_Ori_Airport_name, on='Ori_Airport_name', how='left')
df3_Ori_Airport_name['Ori_Airport_name Delay Ratio'] = round(df3_Ori_Airport_name['Delay Count'] / df3_Ori_Airport_name['Count'],3) 

#Calculate number of flights and delayed flights of each Destination airport
df3_Dest_Airport_name = df3.groupby('Dest_Airport_name').size().reset_index(name='Count')
df5_Dest_Airport_name = df5.groupby('Dest_Airport_name').size().reset_index(name='Delay Count')
df3_Dest_Airport_name = pd.merge(df3_Dest_Airport_name, df5_Dest_Airport_name, on='Dest_Airport_name', how='left')
df3_Dest_Airport_name['Dest_Airport_name Delay Ratio'] = round(df3_Dest_Airport_name['Delay Count'] / df3_Dest_Airport_name['Count'],3) 

#Calculate number of flights and delayed flights of each time interval. Here, we use df4 instead of df5
#because we are counting number of delayed departure, not delayed arrival.
df3_DepTime = df3.groupby('DepTimeBlk').size().reset_index(name='Count')
df4_DepTime = df4.groupby('DepTimeBlk').size().reset_index(name='Delay Count')
df3_DepTime = pd.merge(df3_DepTime, df4_DepTime, on='DepTimeBlk', how='left')
df3_DepTime['DepTime Delay Ratio'] = round(df3_DepTime['Delay Count'] / df3_DepTime['Count'],3) 

#Calculate number of flights and delayed flights of each time interval
df3_ArrTime = df3.groupby('ArrTimeBlk').size().reset_index(name='Count')
df5_ArrTime = df5.groupby('ArrTimeBlk').size().reset_index(name='Delay Count')
df3_ArrTime = pd.merge(df3_ArrTime, df5_ArrTime, on='ArrTimeBlk', how='left')
df3_ArrTime['ArrTime Delay Ratio'] = round(df3_ArrTime['Delay Count'] / df3_ArrTime['Count'],3) 

################################
#4. Selecting 3 Big Airlines and 3 Local Airlines
################################

################################
#4.1 Big Airlines
################################

#Select only the 3 big airlines
airline_big = df3_airline.head(3)

#Restrict the data to only the 3 big airlines, and count the number of flight by each airports
df6 = df3[df3['Airline_name'].isin(airline_big['Airline_name'])]
df6_ori_airport = df6.groupby('Ori_Airport_name').size().reset_index(name='Ori_Count')
df6_Dest_airport = df6.groupby('Dest_Airport_name').size().reset_index(name='Dest_Count')

#Create new column names to merge the data
new_column_names = {
    'Dest_Airport_name': 'Ori_Airport_name'
}
# Renaming columns using the rename() function
df6_Dest_airport.rename(columns=new_column_names, inplace=True)

#Merging two datasets and count the total number of flights of Origin airports and Destination airports
df6_airport = pd.merge(df6_ori_airport, df6_Dest_airport, on='Ori_Airport_name', how='outer')
df6_airport['Count'] = df6_airport['Ori_Count'] + df6_airport['Dest_Count'] 
df6_airport = df6_airport.sort_values(by='Count', ascending=False)
df6_airport.reset_index(drop=True, inplace=True)

#Select only the biggest 25 airports that the 3 big airlines are using
airport_big = df6_airport.head(25)


################################
#4.2 Local Airlines
################################

#Select only the 3 local airlines
airline_local = df3_airline.iloc[[5, 7, 9]]

#Restrict the data to only the 3 local airlines, and count the number of flight by each airports
df7 = df3[df3['Airline_name'].isin(airline_local['Airline_name'])]
df7_ori_airport = df7.groupby('Ori_Airport_name').size().reset_index(name='Ori_Count')
df7_Dest_airport = df7.groupby('Dest_Airport_name').size().reset_index(name='Dest_Count')

#Create new column names to merge the data
new_column_names = {
    'Dest_Airport_name': 'Ori_Airport_name'
}
# Renaming columns using the rename() function
df7_Dest_airport.rename(columns=new_column_names, inplace=True)

#Merging two datasets and count the total number of flights of Origin airports and Destination airports
df7_airport = pd.merge(df7_ori_airport, df7_Dest_airport, on='Ori_Airport_name', how='outer')
df7_airport['Count'] = df7_airport['Ori_Count'] + df7_airport['Dest_Count'] 
df7_airport = df7_airport.sort_values(by='Count', ascending=False)
df7_airport.reset_index(drop=True, inplace=True)

#Select only the biggest 25 airports that the 3 local airlines are using
airport_local = df7_airport.head(25)

################################
#4.3 Big & Local Airlines
################################

#Dataframe of 3 big airlines and 3 local airlines
airline_big_local = pd.merge(airline_big, airline_local, on=['Airline_name'],how='outer') 
#Dataframe of the 25 biggest airports that the 3 big airlines are using
#and the 25 biggest airports that the 3 local airlines are using .
#Some airports might overlap.
airport_big_local = pd.merge(airport_big, airport_local, on=['Ori_Airport_name'],how='outer') 

#Restrict the data to only airlines and airports in the 2 data frames above.
df8 = df3[df3['Airline_name'].isin(airline_big_local['Airline_name'])]
df8 = df8[df8['Ori_Airport_name'].isin(airport_big_local['Ori_Airport_name'])]
df8 = df8[df8['Dest_Airport_name'].isin(airport_big_local['Ori_Airport_name'])]

# Specify the file name
file_name = 'flight_6al_2018-2020.csv'

# Writing to CSV file using pandas
df8.to_csv(file_name, index=False)

################################
#5. Exploring the data after selecting airlines
################################

#Restrict data to only flights with delayed departure
df9 = df8[df8['DepDel15'] == 1]
#Restrict data to only flights with delayed arrival
df10 = df8[df8['ArrDel15'] == 1]

df8['DepDel15'].value_counts()
df8['ArrDel15'].value_counts()


#5.1 Exploring variables

#Calculate number of flights and delayed flights in each Year
df8_Year = df8.groupby('Year').size().reset_index(name='Count')
df10_Year = df10.groupby('Year').size().reset_index(name='Delay Count')
df8_Year = pd.merge(df8_Year, df10_Year, on='Year', how='left')
df8_Year['Year Delay Ratio'] = round(df8_Year['Delay Count'] / df8_Year['Count'],3) 

#Calculate number of flights and delayed flights in each Month
df8_Month = df8.groupby('Month').size().reset_index(name='Count')
df10_Month = df10.groupby('Month').size().reset_index(name='Delay Count')
df8_Month = pd.merge(df8_Month, df10_Month, on='Month', how='left')
df8_Month['Month Delay Ratio'] = round(df8_Month['Delay Count'] / df8_Month['Count'],3) 
df8_Month = df8_Month.sort_values(by='Month Delay Ratio', ascending=False)
df8_Month.reset_index(drop=True, inplace=True)

#Calculate number of flights and delayed flights in each day of Month
df8_DayofMonth = df8.groupby('DayofMonth').size().reset_index(name='Count')
df10_DayofMonth = df10.groupby('DayofMonth').size().reset_index(name='Delay Count')
df8_DayofMonth = pd.merge(df8_DayofMonth, df10_DayofMonth, on='DayofMonth', how='left')
df8_DayofMonth['DayofMonth Delay Ratio'] = round(df8_DayofMonth['Delay Count'] / df8_DayofMonth['Count'],3) 

#Calculate number of flights and delayed flights in each day of week
df8_dofweek = df8.groupby('DayOfWeek').size().reset_index(name='Count')
df10_dofweek = df10.groupby('DayOfWeek').size().reset_index(name='Delay Count')
df8_dofweek = pd.merge(df8_dofweek, df10_dofweek, on='DayOfWeek', how='left')
df8_dofweek['dofweek Delay Ratio'] = round(df8_dofweek['Delay Count'] / df8_dofweek['Count'],3) 
df8_dofweek = df8_dofweek.sort_values(by='dofweek Delay Ratio', ascending=False)
df8_dofweek.reset_index(drop=True, inplace=True)

# Specify the file name
file_name = 'dataex_dayofweek.csv'

# Writing to CSV file using pandas
df8_dofweek.to_csv(file_name, index=False)

#Calculate number of flights and delayed flights of each airline
df8_airline = df8.groupby('Airline_name').size().reset_index(name='Count')
df10_airline = df10.groupby('Airline_name').size().reset_index(name='Delay Count')
df8_airline = pd.merge(df8_airline, df10_airline, on='Airline_name', how='left')
df8_airline['airline Delay Ratio'] = round(df8_airline['Delay Count'] / df8_airline['Count'],3) 
df8_airline = df8_airline.sort_values(by='airline Delay Ratio', ascending=False)
df8_airline.reset_index(drop=True, inplace=True)

# Specify the file name
file_name = 'dataex_airline.csv'

# Writing to CSV file using pandas
df8_airline.to_csv(file_name, index=False)

#Calculate number of flights and delayed flights of each Origin airport. Here, we use df9 instead of df10
#because we are counting number of delayed departure, not delayed arrival.
df8_Ori_Airport_name = df8.groupby('Ori_Airport_name').size().reset_index(name='Count')
df9_Ori_Airport_name = df9.groupby('Ori_Airport_name').size().reset_index(name='Delay Count')
df8_Ori_Airport_name = pd.merge(df8_Ori_Airport_name, df9_Ori_Airport_name, on='Ori_Airport_name', how='left')
df8_Ori_Airport_name['Ori_Airport_name Delay Ratio'] = round(df8_Ori_Airport_name['Delay Count'] / df8_Ori_Airport_name['Count'],3) 

#Calculate number of flights and delayed flights of each Destination airport
df8_Dest_Airport_name = df8.groupby('Dest_Airport_name').size().reset_index(name='Count')
df10_Dest_Airport_name = df10.groupby('Dest_Airport_name').size().reset_index(name='Delay Count')
df8_Dest_Airport_name = pd.merge(df8_Dest_Airport_name, df10_Dest_Airport_name, on='Dest_Airport_name', how='left')
df8_Dest_Airport_name['Dest_Airport_name Delay Ratio'] = round(df8_Dest_Airport_name['Delay Count'] / df8_Dest_Airport_name['Count'],3) 
df8_Dest_Airport_name = df8_Dest_Airport_name.sort_values(by='Dest_Airport_name Delay Ratio', ascending=False)
df8_Dest_Airport_name.reset_index(drop=True, inplace=True)

#Calculate number of flights and delayed flights of each time interval. Here, we use df9 instead of df10
#because we are counting number of delayed departure, not delayed arrival.
df8_DepTime = df8.groupby('DepTimeBlk').size().reset_index(name='Count')
df9_DepTime = df9.groupby('DepTimeBlk').size().reset_index(name='Delay Count')
df8_DepTime = pd.merge(df8_DepTime, df9_DepTime, on='DepTimeBlk', how='left')
df8_DepTime['DepTime Delay Ratio'] = round(df8_DepTime['Delay Count'] / df8_DepTime['Count'],3) 

#Calculate number of flights and delayed flights of each time interval
df8_ArrTime = df8.groupby('ArrTimeBlk').size().reset_index(name='Count')
df10_ArrTime = df10.groupby('ArrTimeBlk').size().reset_index(name='Delay Count')
df8_ArrTime = pd.merge(df8_ArrTime, df10_ArrTime, on='ArrTimeBlk', how='left')
df8_ArrTime['ArrTime Delay Ratio'] = round(df8_ArrTime['Delay Count'] / df8_ArrTime['Count'],3) 
df8_ArrTime = df8_ArrTime.sort_values(by='ArrTime Delay Ratio', ascending=False)
df8_ArrTime.reset_index(drop=True, inplace=True)


