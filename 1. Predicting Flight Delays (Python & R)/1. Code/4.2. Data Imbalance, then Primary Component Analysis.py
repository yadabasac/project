

# Import the relevant libaries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os
import pandas as pd

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
#PCA Using Original Data
##################################################

# z_score normalize the data
scaler = StandardScaler()
Xn = scaler.fit_transform(X)

# Create an instance PCA and build the model using Xn.
# We start from the same number of components as the number of original
# features.
pca_prep = PCA().fit(Xn)
pca_prep.n_components_

# We want to find out how many components
# we want to use without losing much information.
pca_prep.explained_variance_
pca_prep.explained_variance_ratio_

# Well, those numbers are difficult to understand.  A scree plot would be 
# effective. Find an "elbow" or an inflection point on the plot.
plt.plot(pca_prep.explained_variance_ratio_)
plt.xlabel('k number of components')
plt.ylabel('Explained variance')
plt.grid(True)
plt.show()
# Alternative plot using cumulative ratios
plt.plot(np.cumsum(pca_prep.explained_variance_ratio_))
plt.xlabel('k number of components')
plt.ylabel('cumulative explained variance')
plt.grid(True)
plt.show()

#50 seems to be the elbow point. So, we select 50 components.
n_pc = 50
pca = PCA(n_components= n_pc).fit(Xn)

Xp = pca.transform(Xn)
print(f'After PCA, we use {pca.n_components_} components.\n')

Xp = pd.DataFrame(Xp)
df = pd.concat([y, Xp], axis=1, ignore_index=False)

# Specify the file name
file_name = 'flight_weather_original_pca.csv'

# Writing to CSV file using pandas
df.to_csv(file_name, index=False)

# Split the data into training and testing subsets.

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =.2,
                                             random_state=1234,stratify=y)

Xp_train, Xp_test, yp_train, yp_test = train_test_split(Xp,y,test_size =.2,
                                        random_state=1234,stratify=y)


# Create two random forest models: one using the original and the other using
# the transformed data.

rfcm = RandomForestClassifier().fit(X_train, y_train)
rfcm_p = RandomForestClassifier().fit(Xp_train, yp_train)

# Predict the flight delay using the train data.
y_train_pred = rfcm.predict(X_train)
y_train_pred_p = rfcm_p.predict(Xp_train)

# Predict the flight delay using the test data.
y_pred = rfcm.predict(X_test)
y_pred_p = rfcm_p.predict(Xp_test)


# Compare the performance of each model.
report_original_train = classification_report(y_train, y_train_pred)
report_pca_train = classification_report(yp_train, y_train_pred_p)

report_original = classification_report(y_test, y_pred)
report_pca = classification_report(yp_test, y_pred_p)

print(f'Classification Report - original - train\n{report_original_train}')
print(f'Classification Report - original - test\n{report_original}')

print(f'Classification Report - pca - train\n{report_pca_train}')
print(f'Classification Report - pca - test\n{report_pca}')

##################################################
#PCA Using Naive Random Over-Sampling Data
##################################################

# z_score normalize the data
scaler = StandardScaler()
Xn = scaler.fit_transform(X_rs)

# Create an instance PCA and build the model using Xn.
# We start from the same number of components as the number of original
# features.
pca_prep = PCA().fit(Xn)
pca_prep.n_components_

# We want to find out how many components
# we want to use without losing much information.
pca_prep.explained_variance_
pca_prep.explained_variance_ratio_

# Well, those numbers are difficult to understand.  A scree plot would be 
# effective. Find an "elbow" or an inflection point on the plot.
plt.plot(pca_prep.explained_variance_ratio_)
plt.xlabel('k number of components')
plt.ylabel('Explained variance')
plt.grid(True)
plt.show()
# Alternative plot using cumulative ratios
plt.plot(np.cumsum(pca_prep.explained_variance_ratio_))
plt.xlabel('k number of components')
plt.ylabel('cumulative explained variance')
plt.grid(True)
plt.show()

#50 seems to be the elbow point. So, we select 50 components.
n_pc = 50
pca = PCA(n_components= n_pc).fit(Xn)

Xp = pca.transform(Xn)
print(f'After PCA, we use {pca.n_components_} components.\n')

Xp = pd.DataFrame(Xp)
df = pd.concat([y_rs, Xp], axis=1, ignore_index=False)

# Specify the file name
file_name = 'flight_weather_random_pca.csv'

# Writing to CSV file using pandas
df.to_csv(file_name, index=False)

# Split the data into training and testing subsets.

X_train, X_test, y_train, y_test = train_test_split(X_rs,y_rs,test_size =.2,
                                             random_state=1234,stratify=y_rs)

Xp_train, Xp_test, yp_train, yp_test = train_test_split(Xp,y_rs,test_size =.2,
                                        random_state=1234,stratify=y_rs)


# Create two random forest models: one using the original and the other using
# the transformed data.  Of course, you can use other algorithms.

rfcm = RandomForestClassifier().fit(X_train, y_train)
rfcm_p = RandomForestClassifier().fit(Xp_train, yp_train)

# Predict the delay using the train data.
y_train_pred = rfcm.predict(X_train)
y_train_pred_p = rfcm_p.predict(Xp_train)

# Predict the delay using the test data.
y_pred = rfcm.predict(X_test)
y_pred_p = rfcm_p.predict(Xp_test)


# Compare the performance of each model.
report_original_train = classification_report(y_train, y_train_pred)
report_pca_train = classification_report(yp_train, y_train_pred_p)

report_original = classification_report(y_test, y_pred)
report_pca = classification_report(yp_test, y_pred_p)

print(f'Classification Report - original - train\n{report_original_train}')
print(f'Classification Report - original - test\n{report_original}')

print(f'Classification Report - pca - train\n{report_pca_train}')
print(f'Classification Report - pca - test\n{report_pca}')
    

##################################################
#PCA Using SMOTE Data
##################################################

# z_score normalize the data
scaler = StandardScaler()
Xn = scaler.fit_transform(X_sm)

# Create an instance PCA and build the model using Xn.
# We start from the same number of components as the number of original
# features.
pca_prep = PCA().fit(Xn)
pca_prep.n_components_

# We want to find out how many components
# we want to use without losing much information.
pca_prep.explained_variance_
pca_prep.explained_variance_ratio_

# Well, those numbers are difficult to understand.  A scree plot would be 
# effective. Find an "elbow" or an inflection point on the plot.
plt.plot(pca_prep.explained_variance_ratio_)
plt.xlabel('k number of components')
plt.ylabel('Explained variance')
plt.grid(True)
plt.show()
# Alternative plot using cumulative ratios
plt.plot(np.cumsum(pca_prep.explained_variance_ratio_))
plt.xlabel('k number of components')
plt.ylabel('cumulative explained variance')
plt.grid(True)
plt.show()

#50 seems to be the elbow point. So, we select 50 components.
n_pc = 50
pca = PCA(n_components= n_pc).fit(Xn)

Xp = pca.transform(Xn)
print(f'After PCA, we use {pca.n_components_} components.\n')

Xp = pd.DataFrame(Xp)
df = pd.concat([y_sm, Xp], axis=1, ignore_index=False)

# Specify the file name
file_name = 'flight_weather_smote_pca.csv'

# Writing to CSV file using pandas
df.to_csv(file_name, index=False)

# Split the data into training and testing subsets.

X_train, X_test, y_train, y_test = train_test_split(X_sm,y_sm,test_size =.2,
                                             random_state=1234,stratify=y_sm)

Xp_train, Xp_test, yp_train, yp_test = train_test_split(Xp,y_sm,test_size =.2,
                                        random_state=1234,stratify=y_sm)


# Create two random forest models: one using the original and the other using
# the transformed data.  Of course, you can use other algorithms.

rfcm = RandomForestClassifier().fit(X_train, y_train)
rfcm_p = RandomForestClassifier().fit(Xp_train, yp_train)

# Predict the delay using the train data.
y_train_pred = rfcm.predict(X_train)
y_train_pred_p = rfcm_p.predict(Xp_train)

# Predict the delay using the test data.
y_pred = rfcm.predict(X_test)
y_pred_p = rfcm_p.predict(Xp_test)

# Compare the performance of each model.
report_original_train = classification_report(y_train, y_train_pred)
report_pca_train = classification_report(yp_train, y_train_pred_p)

report_original = classification_report(y_test, y_pred)
report_pca = classification_report(yp_test, y_pred_p)

print(f'Classification Report - original - train\n{report_original_train}')
print(f'Classification Report - original - test\n{report_original}')

print(f'Classification Report - pca - train\n{report_pca_train}')
print(f'Classification Report - pca - test\n{report_pca}')
    
        
    
