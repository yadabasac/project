

##########################################################
#1. Selecting the best dataset
##########################################################

import numpy as np
import pandas as pd
import os
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import time  

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data_Model"
os.chdir(new_directory)

data_original = pd.read_csv('flight_weather_original.csv')
data_rs = pd.read_csv('flight_weather_random.csv')
data_sm = pd.read_csv('flight_weather_smote.csv')

data_pca = pd.read_csv('flight_weather_original_pca.csv')
data_random_pca = pd.read_csv('flight_weather_random_pca.csv')
data_smote_pca = pd.read_csv('flight_weather_smote_pca.csv')
data_pca_random = pd.read_csv('flight_weather_pca_random.csv')
data_pca_smote = pd.read_csv('flight_weather_pca_smote.csv')

data_fs = pd.read_csv('flight_weather_original_fs.csv')
data_random_fs = pd.read_csv('flight_weather_random_fs.csv')
data_smote_fs = pd.read_csv('flight_weather_smote_fs.csv')
data_fs_random = pd.read_csv('flight_weather_fs_random.csv')
data_fs_smote = pd.read_csv('flight_weather_fs_smote.csv')


#######################################################
##1 Original Data
#######################################################

data = data_original

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##2 Naive Ramdom Dataset
#######################################################

data = data_rs

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from naive random dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')


#######################################################
##3 SMOTE Dataset
#######################################################

data = data_sm

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from smote dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##4 Original PCA Dataset
#######################################################

data = data_pca

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from original PCA dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##5 Naive Random, then PCA Dataset
#######################################################

data = data_random_pca

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from naive random, then PCA dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##6 SMOTE, then PCA Dataset
#######################################################

data = data_smote_pca

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from smote, then PCA dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##7 PCA, then Naive Random Dataset
#######################################################

data = data_pca_random

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from PCA, then naive random dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##8 PCA, then smote Dataset
#######################################################

data = data_pca_smote

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from PCA, then smote dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##9 Original FS dataset
#######################################################

data = data_fs

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from original FS dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##10 Naive Random, then FS dataset
#######################################################

data = data_random_fs

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from naive random, then FS dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##11 SMOTE, then FS dataset
#######################################################

data = data_smote_fs

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from smote, then FS dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##12 FS, then naive random dataset
#######################################################

data = data_fs_random

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from FS, then naive random dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
##13 FS, then smote dataset
#######################################################

data = data_fs_smote

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)
   
# Create a model (object) for classification
model = RandomForestClassifier()

start = time.time()

# Use cross_val_score
# The default scoring value is accuracy.
score = np.mean(cross_val_score(model,X,y,cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from FS, then smote dataset: {score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

