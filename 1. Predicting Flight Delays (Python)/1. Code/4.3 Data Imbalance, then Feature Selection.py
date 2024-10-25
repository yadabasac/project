# =============================================
# Feature Selection using Feature-Importances
# =============================================

# Import relevant libraries.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn import metrics
import matplotlib.pyplot as plt
import os

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data_Model"
os.chdir(new_directory)

data = pd.read_csv('flight_weather_original.csv')
data_rs = pd.read_csv('flight_weather_random.csv')
data_sm = pd.read_csv('flight_weather_smote.csv')

# Define target variable for classification
y = data['ArrDel15']  # Predicting departure delay
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)

#RandomOverSampler

# Define target variable for classification
y_rs = data_rs['ArrDel15']  # Predicting departure delay
# Select features for classification
X_rs = data_rs.drop(['ArrDel15'], axis=1)

#SMOTE

# Define target variable for classification
y_sm = data_sm['ArrDel15']  # Predicting departure delay
# Select features for classification
X_sm = data_sm.drop(['ArrDel15'], axis=1)

##################################################
#FS Using Original Data
##################################################

fn = X.columns
print(f'Originally, we have {len(fn)} features.')

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =.3, stratify=y)

# Create an instance (object) for classification and build a model.
rfcm = RandomForestClassifier().fit(X_train, y_train)

# Make predictions using the test data
y_pred = rfcm.predict(X_test)

# Show the Classification Report.
print('\nClassification Report\n')
print(metrics.classification_report(y_test,y_pred))

# %matplotlib auto
# %matplotlib inline

importances = rfcm.feature_importances_
np.sum(importances)
plt.barh(fn,importances)

# Draw a bar chart to see the sorted importance values with feature names.
df_importances = pd.DataFrame(data=importances, index=fn, columns=['importance_value'])
df_importances.sort_values(by = 'importance_value', ascending=False, inplace=True)
plt.barh(df_importances.index,df_importances.importance_value)
df_importances50 = df_importances.iloc[0:50,:]

#Select only the most 50 important features
selected_columns = df_importances50.index
X_reduced = X[selected_columns]

df = pd.concat([y, X_reduced], axis=1, ignore_index=False)

# Specify the file name
file_name = 'flight_weather_original_fs.csv'

# Writing to CSV file using pandas
df.to_csv(file_name, index=False)

# Now, we are ready to build a model using those reduced number of features.
X_reduced_train, X_reduced_test, y_reduced_train, y_reduced_test = train_test_split(X_reduced,y,test_size =.3, stratify=y)
                      
# Build a model with the reduced number of features.
rfcm2 = RandomForestClassifier().fit(X_reduced_train, y_reduced_train)
y_reduced_pred = rfcm2.predict(X_reduced_test)

print('\nClassification Report after feature reduction\n')
print(metrics.classification_report(y_reduced_test,y_reduced_pred))



##################################################
#FS Using Naive Random Oversampling Dataset
##################################################

fn = X_rs.columns
print(f'Originally, we have {len(fn)} features.')

X_train, X_test, y_train, y_test = train_test_split(X_rs,y_rs,test_size =.3, stratify=y_rs)

# Create an instance (object) for classification and build a model.
rfcm = RandomForestClassifier().fit(X_train, y_train)

# Make predictions using the test data
y_pred = rfcm.predict(X_test)

# Show the Classification Report.
print('\nClassification Report\n')
print(metrics.classification_report(y_test,y_pred))

# %matplotlib auto
# %matplotlib inline

importances = rfcm.feature_importances_
np.sum(importances)
plt.barh(fn,importances)

# Draw a bar chart to see the sorted importance values with feature names.
df_importances = pd.DataFrame(data=importances, index=fn, columns=['importance_value'])
df_importances.sort_values(by = 'importance_value', ascending=False, inplace=True)
plt.barh(df_importances.index,df_importances.importance_value)
df_importances50 = df_importances.iloc[0:50,:]

#Select only the most 50 important features
selected_columns = df_importances50.index
X_reduced = X_rs[selected_columns]

df = pd.concat([y_rs, X_reduced], axis=1, ignore_index=False)

# Specify the file name
file_name = 'flight_weather_random_fs.csv'

# Writing to CSV file using pandas
df.to_csv(file_name, index=False)

# Now, we are ready to build a model using those reduced number of features.
X_reduced_train, X_reduced_test, y_reduced_train, y_reduced_test = train_test_split(X_reduced,y_rs,test_size =.3, stratify=y_rs)
                      
# Build a model with the reduced number of features.
rfcm2 = RandomForestClassifier().fit(X_reduced_train, y_reduced_train)
y_reduced_pred = rfcm2.predict(X_reduced_test)

print('\nClassification Report after feature reduction\n')
print(metrics.classification_report(y_reduced_test,y_reduced_pred))


##################################################
#FS Using SMOTE Dataset
##################################################

fn = X_sm.columns
print(f'Originally, we have {len(fn)} features.')

X_train, X_test, y_train, y_test = train_test_split(X_sm,y_sm,test_size =.3, stratify=y_sm)

# Create an instance (object) for classification and build a model.
rfcm = RandomForestClassifier().fit(X_train, y_train)

# Make predictions using the test data
y_pred = rfcm.predict(X_test)

# Show the Classification Report.
print('\nClassification Report\n')
print(metrics.classification_report(y_test,y_pred))

# %matplotlib auto
# %matplotlib inline

importances = rfcm.feature_importances_
np.sum(importances)
plt.barh(fn,importances)

# Draw a bar chart to see the sorted importance values with feature names.
df_importances = pd.DataFrame(data=importances, index=fn, columns=['importance_value'])
df_importances.sort_values(by = 'importance_value', ascending=False, inplace=True)
plt.barh(df_importances.index,df_importances.importance_value)
df_importances50 = df_importances.iloc[0:50,:]

#Select only the most 50 important features
selected_columns = df_importances50.index
X_reduced = X_sm[selected_columns]

df = pd.concat([y_sm, X_reduced], axis=1, ignore_index=False)

# Specify the file name
file_name = 'flight_weather_smote_fs.csv'

# Writing to CSV file using pandas
df.to_csv(file_name, index=False)

# Now, we are ready to build a model using those reduced number of features.
X_reduced_train, X_reduced_test, y_reduced_train, y_reduced_test = train_test_split(X_reduced,y_sm,test_size =.3, stratify=y_sm)
                      
# Build a model with the reduced number of features.
rfcm2 = RandomForestClassifier().fit(X_reduced_train, y_reduced_train)
y_reduced_pred = rfcm2.predict(X_reduced_test)

print('\nClassification Report after feature reduction\n')
print(metrics.classification_report(y_reduced_test,y_reduced_pred))

