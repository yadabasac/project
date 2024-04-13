# Predicting Flight Delays in the United States

## Contents

1. Project Overview
2. Data
3. Code Structure
4. Results and Evaluation
5. Future Work
6. References

![Screenshot of a information board](https://i.cdn.newsbytesapp.com/images/l69220240116183655.jpeg?tr=w-720)

## 1. Project Overview

This project focuses on predicting flight delays for six major US airlines using machine learning models. Delayed aircraft are estimated to have cost the airlines several billion dollars in additional expense. Delays also drive the need for extra gates and ground personnel and impose costs on airline customers (including shippers) in the form of lost productivity, wages and goodwill. Results indicate the models' ability to accurately forecast delays, with improvements noted through data balancing and feature reduction. Such insights are pivotal for crafting more effective air traffic management strategies, curbing delays, and their economic ramifications. 

## 2. Data
## 2.1 Data Source

The dataset utilized for this project comprises flight data sourced from the U.S. Department of Transportation. Due to computational constraints, a smaller sample dataset (containing 53,413 rows) focusing on flight data from six major airlines: Southwest, Delta, American Airlines, Republic, JetBlue, and Alaska, spanning January 2018 to December 2020. Flight data from Department of Transportation can be downloaded [here.](https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr/)

Additionally, weather data from the Integrated Surface Database (ISD) of the National Oceanic and Atmospheric Administration (NOAA) was integrated. Weather data can be downloaded [here.](https://www.ncei.noaa.gov/access/search/data-search/global-hourly/)

## 2.2 Data Dictionary

The target variable is Arrival Delay, which is set to 1 if a flight is delayed 15 minutes or more or 0 otherwise.
List of attributes used in this study is as follows:

**Table 1:**
| Attribute  | Description |
| ------------- | ------------- |
| 1. Year  | Year of flight departure date  |
| 2. Month  | Month of flight departure date  |
| 3. Day of Month  | Day of month of flight departure date  |
| 4. Day of Week  | Day of week of flight departure date  |
| 5. Airline  | Airline name  |
| 6. Origin Airport  | Name of departure airport  |
| 7. Destination Airport  | Name of arrival airport  |
| 8. Departure Time Bulk  | Departure time block, hourly intervals  |
| 9. Arrival Time Bulk  | Arrival time block, hourly intervals  |
| 10. Windspeed  | Windspeed at both departure and arrival airports  |
| 11. Cloud height  | Cloud height at both departure and arrival airports  |
| 12. Visibility  | The horizontal distance at which an object can be seen and identified at both airports  |
| 13. Temperature  | The temperature of the air at both airports  |
| 14. Rain  |  The depth of rain measured at both airports |
| 15. Snow  | The depth of snow measured at both airports  |


## 2.3 Exploratory Data Analysis


**Graph 1:**

![image](https://github.com/yadabasac/project/assets/129697541/078eceb4-8ce6-4412-b203-06d2447d0eca)

Graph 1 reveals American Airlines as the leading carrier in terms of flight volume, with Delta Airlines demonstrating the lowest delay percentage, while JetBlue struggles the most with delays.

**Graph 2:**
![image](https://github.com/yadabasac/project/assets/129697541/a3aa9619-4083-492e-b964-845b05ceb244)

Analysis of flight volumes by day of the week highlights weekdays as busier periods, with Thursdays and Fridays exhibiting the highest delay percentages.

## 3. Code Structure

## 3.1 Merging the Weather Data with the Flight Data

The data preprocessing phase involved several steps to prepare the datasets for machine learning analysis. Weather data, available for individual airports and years, was merged after being downloaded and cleaned, with missing values imputed using the mode. Similarly, the flight dataset was refined by selecting six major airlines and reducing the number of airports to 39 to alleviate processing burdens. After merging the datasets and converting categorical variables to dummy variables through one-hot encoding, the dataset consisted of 53,413 rows, 178 attributes, and one dependent variable, Arrival Delay. 

## 3.2 Dealing with Data Imbalance and Feature Selection

Due to class imbalance in the dependent variable, two techniques, Naïve Random Over-Sampling and Synthetic Minority Over-Sampling Technique (SMOTE), were employed, increasing the samples with Arrival Delay equaling 1 from 10,095 to 43,318. Further, Principal Component Analysis (PCA) and feature selection were applied to reduce the number of features, with PCA revealing an elbow point at 50 components. Testing showed that datasets with reduced features (50 features) produced comparable accuracy (81%) to the original dataset (178 features) using Random Forests. 

## 3.3 Selecting the Best Dataset

We had many options in selecting the best dataset to run our machine learning algorithms. Should we apply Naive Random Over-Sampling or SMOTE? Should we reduce the number of features by PCA or feature selection? Should we deal with data imbalance first and then reduce the number of features? After running all the possible datasets, we found that reducing the number of features by PCA first, then dealing with the data imbalance by Naive Random produced the best results. These results were produced by combining K-Fold Cross Validation (n=5) with Random Forests.

## 4. Results and Evaluation

The machine learning models were applied to the dataset, including Random Forests, Logistic Regression, Decision Trees, Naïve Bayes, SVM, and Neural Networks. Each model's performance was evaluated based on accuracy, precision, and recall for both training and test data. The computer specifications used for these computations were an 11th Gen Intel(R) Core (TM) i5-1135G7 @ 2.40GHz processor with 8.00 GB Installed RAM. The below summarized the results of each model.

**Table 2:**
| Model  | Accuracy (K-Fold=5) | Computation Time (seconds) | 
| ------------- | ------------- |  ------------- |
| 1. SVM  | 0.9941  | > 10,000 |
| 2. Random Forests  |  0.9852  | 300 |
| 3. Neural Networks  | 0.8953  | 250 |
| 4. Decision Tree  | 0.8867  | 21 |
| 5. Logistic Regression  | 0.6129 | < 1 |
| 6. Naive Bayesian  | 0.6115  | < 1 |

SVM, Random Forests, and Neural Networks emerged as the top-performing models based on mean scores from K-Fold Cross Validation. Random Forests stood out due to its relatively high accuracy and shorter computation time compared to SVM.

## 5. Future Work

Random Forests emerged as the best model for predicting flight delays, balancing accuracy and computational efficiency. Future work could explore predicting flight delays in other countries and leveraging cloud computation for larger datasets from the Department of Transportation.

## 6. References

1.	Kim, Y. J., Choi, S., Briceno, S., & Mavris, D. (2016). A Deep Learning Approach to Flight Delay Prediction. In 35th Digital Avionics Systems Conference (DASC).
2.	Chakrabarty, N. (2019). A Data Mining Approach to Flight Arrival Delay Prediction for American Airlines. In 9th Annual Information Technology, Electromechanical Engineering and Microelectronics Conference (IEMECON).

