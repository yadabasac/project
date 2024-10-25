

##########################################################
#1. Classification
##########################################################

import numpy as np
import pandas as pd
import os
import time 

new_directory = "C:/Users/yada/Documents/3. School/Classses/11. Capstone/Project/Dataset/Data_Model"
os.chdir(new_directory)

data_rs = pd.read_csv('flight_weather_pca_random.csv')


#RandomOverSampler

# Define target variable for classification
y_rs = data_rs['ArrDel15']
# Select features for classification
X_rs = data_rs.drop(['ArrDel15'], axis=1)

print(f'Over-sampled data: {np.unique(y_rs, return_counts=1)}')


#######################################################
## SVM with Random Search
#######################################################

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import RandomizedSearchCV     

###Naive Random Over-Sampling Data

scaler = StandardScaler()
Xn_rs = scaler.fit_transform(X_rs)

# You can change the C_vals and g_vals as you see fit.
C_vals = np.logspace(-3,2,10)
g_vals = np.logspace(-3,2,10)
params = dict(gamma=g_vals, C=C_vals, kernel=['poly','sigmoid','rbf'])
kfolds = StratifiedKFold(n_splits=5)

start = time.time()

svc = SVC()

rand_src = RandomizedSearchCV(estimator= svc, param_distributions = params, cv=kfolds, n_iter=10, verbose=3)

rand_src.fit(Xn_rs, y_rs)

end = time.time()
print(f'Total run time for SVM: {(end - start):.2f} seconds')

# svcm can be used for predictions or others.
print(f'Best score is {rand_src.best_score_:.4f}')
print(rand_src.best_params_)
results = pd.DataFrame(rand_src.cv_results_)
svc = rand_src.best_estimator_
# {'kernel': 'rbf', 'gamma': 0.046415888336127795, 'C': 2.1544346900318843}
# {'kernel': 'rbf', 'gamma': 0.599484, 'C': 27.8256}, score = 0.9687

