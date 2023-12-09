

##########################################################
#Data Imbalance
##########################################################

from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
import numpy as np
import pandas as pd
import os

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data_Model"
os.chdir(new_directory)

data = pd.read_csv('flight_weather_original_pca.csv')

# Define target variable for classification
y = data['ArrDel15']

# Select features for classification
X = data.drop(['ArrDel15'], axis=1)

X.shape
y.shape
print(f'Original data: {np.unique(y, return_counts=1)}')

# Create an instance of RandomOverSampler

ros = RandomOverSampler(random_state=0)
X_rs, y_rs = ros.fit_resample(X, y)

X_rs.shape
y_rs.shape
print(f'Over-sampled data: {np.unique(y_rs, return_counts=1)}')

df_rs = pd.concat([y_rs, X_rs], axis=1, ignore_index=False)

# Specify the file name
file_name = 'flight_weather_pca_random.csv'

# Writing to CSV file using pandas
df_rs.to_csv(file_name, index=False)

# Create an instance of SMOTE

sm = SMOTE(random_state=0)
X_sm, y_sm = sm.fit_resample(X, y)

X_sm.shape
y_sm.shape
print(f'Over-sampled data: {np.unique(y_sm, return_counts=1)}')

df_sm = pd.concat([y_sm, X_sm], axis=1, ignore_index=False)

# Specify the file name
file_name = 'flight_weather_pca_smote.csv'

# Writing to CSV file using pandas
df_sm.to_csv(file_name, index=False)

