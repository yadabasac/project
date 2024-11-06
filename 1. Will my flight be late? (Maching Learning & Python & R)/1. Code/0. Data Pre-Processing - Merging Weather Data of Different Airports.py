
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

#We can only download weather data for one airport for one year at a time so there are more than
#200 weather files since we have more than 30 airports and we downloaded the data for 6 years.
#Read the data from the first weather file and select only relevant columns.
df = pd.read_csv('Weather (1).csv')
df = df[['DATE','NAME','WND','CIG','VIS','TMP','DEW','SLP','AA1','AJ1']]
n_rows = len(df)

#Read weather files one by one and concatenate them together.
for i in range(2,259):
    filename = 'Weather '+'('+str(i)+').csv'
    print (filename)
    df_m=pd.read_csv(filename)
    n_rows = n_rows + len(df_m)
    #Some files have no AJ1 column (snow information).
    try:
        df_m = df_m[['DATE','NAME','WND','CIG','VIS','TMP','DEW','SLP','AA1','AJ1']]
    #When there is no snow information column "AJ1" in the weather file, then we create
    #"AJ1" column and set it to 0.      
    except:
        df_m = df_m[['DATE','NAME','WND','CIG','VIS','TMP','DEW','SLP','AA1']]
        df_m['AJ1'] = 0
    df = pd.concat([df, df_m], axis=0, ignore_index=True)
    
#Create new column names
new_column_names = {
    'WND': 'Wind',
    'CIG': 'Cloud',
    'VIS': 'Visibility',
    'TMP': 'Air Temp',
    'DEW': 'Air Temp2',
    'SLP': 'Atmosphere',
    'AA1': 'Rain',
    'AJ1': 'Snow'
}    

# Renaming columns using the rename() function
df.rename(columns=new_column_names, inplace=True)

# Specify the file name
file_name = 'weather_2018-2023_full data set.csv'
# Writing to CSV file using pandas
df.to_csv(file_name, index=False)