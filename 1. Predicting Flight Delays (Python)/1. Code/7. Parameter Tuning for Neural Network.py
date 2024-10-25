# Neural Network Classification

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
import time
import os

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data_Model"
os.chdir(new_directory)

data_rs = pd.read_csv('flight_weather_pca_random.csv')

X = data_rs.drop('ArrDel15', axis=1)
y = data_rs['ArrDel15']


# Standardize the feature data
scaler = StandardScaler()
Xn = scaler.fit_transform(X)

nnm_r = MLPClassifier()


params = {'hidden_layer_sizes':[(7), (25), (50), (75), (100), (125), (150), (200),
                                (125,7), (125,25),(125,50),(125,75),(125,100),
                                (125,125),(125,150)],
          'activation':['tanh','logistic', 'relu'], 
          'max_iter': [21000]}
    
start_r = time.time()

rand_src = RandomizedSearchCV(estimator= nnm_r, param_distributions = params, cv=5,
                              n_iter=1, verbose= 3)
rand_src.fit(Xn,y)

end_r = time.time()


# Generate a Report

print('\n\n   **Report**')
print(f'The best estimator: {rand_src.best_estimator_}')
print(f'The best parameters:\n {rand_src.best_params_}')
print(f'The best score: {rand_src.best_score_:.4f}')
print(f'Total run time for RandomizedSearchCV: {(end_r - start_r):.2f} seconds')
# Check the details of search
results_rgs = pd.DataFrame(rand_src.cv_results_)
results_rgs


# Split the data into training and testing subsets.

X_train, X_test,y_train, y_test = \
    train_test_split(Xn, y, test_size =.3,random_state=1234, stratify=y)


# Create a model (object) for classification

nnm = MLPClassifier(hidden_layer_sizes=(30), activation='tanh', 
                    max_iter=5000, random_state=1234)

# Build a neural network model
nnm.fit(X_train, y_train)

# Calcuate the probability for each class
nnm.predict_proba(X_test)

# Based on the probabilities, make a prediction 
y_pred = nnm.predict(X_test)

# Calculate the accuracy
score_ = nnm.score(X_test, y_test)
print(f'Accuracy: {score_:.4f}')



