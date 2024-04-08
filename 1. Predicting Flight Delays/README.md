# Predicting Flight Delays in the United States Using Machine Learning Algorithms (Still in progress)

## Contents
1. Project Overview
2. Data
3. Code Structure
4. Results and Evaluation
5. Future Work

## 1. Introduction

Flight delays pose significant economic challenges to the aviation industry, necessitating efficient air traffic management strategies. This project focuses on predicting flight delays for six major US airlines using machine learning models. By assessing data balancing techniques and feature reduction, the study aims to enhance predictive performance. Results indicate the models' ability to accurately forecast delays, with improvements noted through data balancing and feature reduction. Such insights are pivotal for crafting more effective air traffic management strategies, curbing delays, and their economic ramifications. Accurate predictions empower airlines to preemptively mitigate delays' impact on passengers and industry. The study sourced flight data from major US airlines and employed machine learning algorithms for prediction, evaluating performance using various metrics. Overall, the research underscores machine learning's potential in predicting flight delays and optimizing air traffic management. These findings offer actionable insights for airlines and industry stakeholders to inform decisions aimed at reducing delays and associated costs. Leveraging datasets like the US Bureau of Transportation Statistics' Reporting Carrier On-Time Performance Dataset enables precise estimation of flight punctuality probabilities.

## 2. Datasets


The dataset utilized for this project comprises flight data sourced from the U.S. Department of Transportation. Due to computational constraints, a smaller sample dataset provided by IBM was chosen, focusing on flight data from six major airlines: Southwest, Delta, American Airlines, Republic, JetBlue, and Alaska, spanning January 2018 to December 2020. Additionally, weather data from the Integrated Surface Database (ISD) of the National Oceanic and Atmospheric Administration (NOAA) was integrated, considering attributes such as windspeed, cloud height, visibility, temperature, rain, and snow at both departure and arrival airports. The primary classification variable is arrival delay, categorized as 1 for delays exceeding 15 minutes and 0 otherwise. Graphical analysis reveals American Airlines as the leading carrier in terms of flight volume, with Delta Airlines demonstrating the lowest delay percentage, while JetBlue struggles the most with delays. Analysis of flight volumes by day of the week highlights weekdays as busier periods, with Thursdays and Fridays exhibiting the highest delay percentages. Furthermore, there's an observed increase in flight activity during winter months, notably January and March, and a concentration of delays around the 18th to 20th days of the month, suggesting potential areas for advanced planning by both passengers and airlines.

## 3. Data Preprocessing

The data preprocessing phase involved several steps to prepare the datasets for machine learning analysis. Weather data, available for individual airports and years, was merged after being downloaded and cleaned, with missing values imputed using the mode. Similarly, the flight dataset was refined by selecting six major airlines and reducing the number of airports to 39 to alleviate processing burdens. After merging the datasets and converting categorical variables to dummy variables through one-hot encoding, the dataset consisted of 53,413 rows, 178 attributes, and one dependent variable, Arrival Delay. Due to class imbalance in the dependent variable, two techniques, Naïve Random Over-Sampling and Synthetic Minority Over-Sampling Technique (SMOTE), were employed, increasing the samples with Arrival Delay equaling 1 from 10,095 to 43,318. Further, Principal Component Analysis (PCA) and feature selection were applied to reduce the number of features, with PCA revealing an elbow point at 50 components. Testing showed that datasets with reduced features (50 features) produced comparable accuracy (81%) to the original dataset (178 features) using Random Forests. Combining K-Fold Cross Validation (n=5) with Random Forests, various dataset combinations were tested, with the 5th dataset (PCA followed by Naïve Random Over-Sampling) exhibiting similar performance to the 7th dataset. Consequently, the 5th dataset was chosen for selecting the best machine learning algorithms. This dataset combination strategy ensures improved model performance while mitigating class imbalance and computational burdens.

## 4. Results and Evaluation

The machine learning models were applied to the dataset, including Random Forests, Logistic Regression, Decision Trees, Naïve Bayes, SVM, and Neural Networks. Each model's performance was evaluated based on accuracy, precision, and recall for both training and test data. The computer specifications used for these computations were an 11th Gen Intel(R) Core (TM) i5-1135G7 @ 2.40GHz processor with 8.00 GB Installed RAM.

Random Forests:

When using the dataset with PCA only, the model showed poor recall (1%) without data balancing. However, with the balanced dataset (PCA first, followed by Naïve Random), significant improvement was observed, with a recall of 97% for the test data.

Decision Trees:

Overfitting was observed with the model trained on the dataset with PCA only, resulting in an accuracy of 70% for the test data. However, when using the balanced dataset, the accuracy improved to 86%.

Logistic Regression:

Both balanced and imbalanced datasets produced similar accuracy (81%) for the test data. However, when using the balanced dataset, precision and recall for the minority class (Arrival Delay = 1) decreased compared to the imbalanced dataset.

Naïve Bayes:

Similar to Logistic Regression, Naïve Bayes showed higher accuracy (80%) with the imbalanced dataset compared to the balanced dataset (62%).

SVM:

The SVM model exhibited high accuracy (99%) with a long training time, showing the model's ability to generalize well to new data. Using the balanced dataset, the model produced an accuracy of over 99%.

Neural Networks:

Various configurations were tested, with the optimal configuration achieving a cross-validated score of 0.89. The model utilized the balanced dataset, showcasing its effectiveness in classifying new data.

Top 3 Performing Models:

SVM, Random Forests, and Neural Networks emerged as the top-performing models based on mean scores from K-Fold Cross Validation. Random Forests stood out due to its relatively high accuracy and shorter computation time compared to SVM.

Methodological Contributions:

Balancing the dataset using Naïve Random Over-Sampling significantly improved results, especially recall values. Primary Component Analysis proved slightly better than feature selection for reducing the number of features. The order of preprocessing steps did not affect the results significantly.

Conclusions:

Random Forests emerged as the best model for predicting flight delays, balancing accuracy and computational efficiency. Future work could explore predicting flight delays in other countries and leveraging cloud computation for larger datasets from the Department of Transportation.
