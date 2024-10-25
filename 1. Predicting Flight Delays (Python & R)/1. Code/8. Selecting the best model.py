

##########################################################
# 1. Classification
##########################################################

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import os
import time

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data_Model"
os.chdir(new_directory)

data = pd.read_csv('flight_weather_original_pca.csv')
data_rs = pd.read_csv('flight_weather_pca_random.csv')

# Define target variable for classification
y = data['ArrDel15']
# Select features for classification
X = data.drop(['ArrDel15'], axis=1)

print(f'Original data: {np.unique(y, return_counts=1)}')

# RandomOverSampler

# Define target variable for classification
y_rs = data_rs['ArrDel15']
# Select features for classification
X_rs = data_rs.drop(['ArrDel15'], axis=1)

print(f'Over-sampled data: {np.unique(y_rs, return_counts=1)}')


# Create training data and test data


X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=.3, random_state=1234, stratify=y)

X_rs_train, X_rs_test, y_rs_train, y_rs_test = \
    train_test_split(X_rs, y_rs, random_state=1234, stratify=y_rs)


#######################################################
# 1.1Random Forest
#######################################################

# Create a model (object) for classification
model = RandomForestClassifier()
model_rs = RandomForestClassifier()

# Build a random forest classification model
model.fit(X_train, y_train)
model_rs.fit(X_rs_train, y_rs_train)

# Make predictions using the test data
y_pred = model.predict(X_test)
y_pred_rs = model_rs.predict(X_test)

# Make predictions using the train data
y_pred_train = model.predict(X_train)
y_pred_train_rs = model_rs.predict(X_train)


print('\nClassification Report for training data from original data using Random Forest\n')
print(metrics.classification_report(y_train, y_pred_train))
print('\nClassification Report for test data from original data using Random Forest\n')
print(metrics.classification_report(y_test, y_pred))


print('\nClassification Report for training data from oversampled model using Random Forest\n')
print(metrics.classification_report(y_train, y_pred_train_rs))
print('\nClassification Report for test data from oversampled model using Random Forest\n')
print(metrics.classification_report(y_test, y_pred_rs))

start = time.time()

# Use cross_val_score
model_rs_mean_score = np.mean(cross_val_score(model_rs, X_rs, y_rs, cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for random forest**')
print(f'Mean Score from naive random data: {model_rs_mean_score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
# 1.2 Logistic Regression
#######################################################


# Classification using Logistic Regression
model = LogisticRegression()
model_rs = LogisticRegression()

# Build a logistics regression classification model
model.fit(X_train, y_train)
model_rs.fit(X_rs_train, y_rs_train)

# Make predictions using the test data
y_pred = model.predict(X_test)
y_pred_rs = model_rs.predict(X_test)

# Make predictions using the train data
y_pred_train = model.predict(X_train)
y_pred_train_rs = model_rs.predict(X_train)

print('\nClassification Report for training data from original data using logistic regression\n')
print(metrics.classification_report(y_train, y_pred_train))
print('\nClassification Report for test data from original data using logistic regression\n')
print(metrics.classification_report(y_test, y_pred))

print('\nClassification Report for training data from oversampled model using logistic regression\n')
print(metrics.classification_report(y_train, y_pred_train_rs))
print('\nClassification Report for test data from oversampled model using logistic regression\n')
print(metrics.classification_report(y_test, y_pred_rs))

start = time.time()

# Cross Validation Scores
model_rs_mean_score = np.mean(cross_val_score(model_rs, X_rs, y_rs, cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for Logistic Regression**')
print(f'Mean Score from naive random data: {model_rs_mean_score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
# 1.3 Decision Tree
#######################################################


# Classification using Decision Tree
model = DecisionTreeClassifier()
model_rs = DecisionTreeClassifier()

# Build a decision tree classification model
model.fit(X_train, y_train)
model_rs.fit(X_rs_train, y_rs_train)

# Make predictions using the test data
y_pred = model.predict(X_test)
y_pred_rs = model_rs.predict(X_test)

# Make predictions using the train data
y_pred_train = model.predict(X_train)
y_pred_train_rs = model_rs.predict(X_train)

print('\nClassification Report for training data from original data using Decision Tree\n')
print(metrics.classification_report(y_train, y_pred_train))
print('\nClassification Report for test data from original data using Decision Tree\n')
print(metrics.classification_report(y_test, y_pred))


print('\nClassification Report for training data from oversampled model using Decision Tree\n')
print(metrics.classification_report(y_train, y_pred_train_rs))
print('\nClassification Report for test data from oversampled model using Decision Tree\n')
print(metrics.classification_report(y_test, y_pred_rs))

start = time.time()

# Cross Validation Scores
model_rs_mean_score = np.mean(cross_val_score(model_rs, X_rs, y_rs, cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for Decision Tree**')
print(f'Mean Score from naive random data: {model_rs_mean_score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')

#######################################################
# 1.4 Naive Bayesian
#######################################################


# Classification using Naive Bayesian
model = GaussianNB()
model_rs = GaussianNB()

# Build a NB classification model
model.fit(X_train, y_train)
model_rs.fit(X_rs_train, y_rs_train)

# Make predictions using the test data
y_pred = model.predict(X_test)
y_pred_rs = model_rs.predict(X_test)

# Make predictions using the train data
y_pred_train = model.predict(X_train)
y_pred_train_rs = model_rs.predict(X_train)


print('\nClassification Report for training data from original data using Naive Bayesian\n')
print(metrics.classification_report(y_train, y_pred_train))
print('\nClassification Report for test data from original data using Naive Bayesian\n')
print(metrics.classification_report(y_test, y_pred))


print('\nClassification Report for training data from oversampled model using Naive Bayesian\n')
print(metrics.classification_report(y_train, y_pred_train_rs))
print('\nClassification Report for test data from oversampled model using Naive Bayesian\n')
print(metrics.classification_report(y_test, y_pred_rs))

start = time.time()

# Cross Validation Scores
model_rs_mean_score = np.mean(cross_val_score(model_rs, X_rs, y_rs, cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for Naive Bayesian**')
print(f'Mean Score from naive random data: {model_rs_mean_score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')


####################################
# 1.5 SVM
####################################

scaler = StandardScaler()

Xn_train = scaler.fit_transform(X_train)
Xn_test = scaler.fit_transform(X_test)
Xn_rs_train = scaler.fit_transform(X_rs_train)
Xn_rs_test = scaler.fit_transform(X_rs_test)


start = time.time()

model = SVC(kernel='rbf', C=27.8256, gamma=0.599484,
            random_state=1234).fit(Xn_train, y_train)

end = time.time()
print(f'Total run time for SVM: {(end - start):.2f} seconds')


start = time.time()

model_rs = SVC(kernel='rbf', C=27.8256, gamma=0.599484,
               random_state=1234).fit(Xn_rs_train, y_rs_train)

end = time.time()
print(f'Total run time for SVM: {(end - start):.2f} seconds')

# Make predictions using the test data
y_pred = model.predict(Xn_test)
y_pred_rs = model_rs.predict(Xn_test)

# Make predictions using the train data
y_pred_train = model.predict(Xn_train)
y_pred_train_rs = model_rs.predict(Xn_train)

print('\nClassification Report for training data from original data using SVM\n')
print(metrics.classification_report(y_train, y_pred_train))
print('\nClassification Report for test data from original data using SVM\n')
print(metrics.classification_report(y_test, y_pred))


print('\nClassification Report for training data from oversampled model using SVM\n')
print(metrics.classification_report(y_train, y_pred_train_rs))
print('\nClassification Report for test data from oversampled model using SVM\n')
print(metrics.classification_report(y_test, y_pred_rs))


start = time.time()

# Cross Validation Scores
model_rs = SVC(kernel='rbf', C=27.8256, gamma=0.599484, random_state=1234)
model_rs_mean_score = np.mean(cross_val_score(model_rs, X_rs, y_rs, cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for SVM**')
print(f'Mean Score from naive random data: {model_rs_mean_score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')


####################################
# 1.6 Neural Network
####################################


scaler = StandardScaler()

Xn_train = scaler.fit_transform(X_train)
Xn_test = scaler.fit_transform(X_test)
Xn_rs_train = scaler.fit_transform(X_rs_train)
Xn_rs_test = scaler.fit_transform(X_rs_test)

model = MLPClassifier(hidden_layer_sizes=(125, 150), activation='tanh',
                      max_iter=21000, random_state=1234)
model_rs = MLPClassifier(hidden_layer_sizes=(125, 150), activation='tanh',
                         max_iter=21000, random_state=1234)

start = time.time()

# Build a random forest classification model
model.fit(Xn_train, y_train)

end = time.time()
print(f'Total run time for SVM: {(end - start):.2f} seconds')

start = time.time()

# Build a random forest classification model
model_rs.fit(Xn_rs_train, y_rs_train)

end = time.time()
print(f'Total run time for SVM: {(end - start):.2f} seconds')

# Make predictions using the test data
y_pred = model.predict(Xn_test)
y_pred_rs = model_rs.predict(Xn_test)

# Make predictions using the train data
y_pred_train = model.predict(Xn_train)
y_pred_train_rs = model_rs.predict(Xn_train)

print('\nClassification Report for training data from original data using NN\n')
print(metrics.classification_report(y_train, y_pred_train))
print('\nClassification Report for test data from original data using NN\n')
print(metrics.classification_report(y_test, y_pred))


print('\nClassification Report for training data from oversampled model using NN\n')
print(metrics.classification_report(y_train, y_pred_train_rs))
print('\nClassification Report for test data from oversampled model using NN\n')
print(metrics.classification_report(y_test, y_pred_rs))

start = time.time()

# Cross Validation Scores
model_rs_mean_score = np.mean(cross_val_score(model_rs, X_rs, y_rs, cv=5))

# Print the scores
print('**\n Mean Scores (Accuracies) for SVM**')
print(f'Mean Score from naive random data: {model_rs_mean_score:.4f}')

end = time.time()
print(f'Total run time: {(end - start):.2f} seconds')
