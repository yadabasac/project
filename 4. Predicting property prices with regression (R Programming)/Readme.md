# Predicting property prices with regression (R Programming)

## Contents

1. Project Overview
2. Data
3. Code Structure
4. Results and Evaluation
5. References

![1](https://github.com/user-attachments/assets/c5881dff-f919-402d-a7b2-827372436b8b)

## 1. Project Overview

A city had a plan to extend a local road from 2 lanes to 4 lanes. However, doing that would affect some of the properties in that area since they would be required to not only give up some of their spaces to the city, but also, they would have to experience the increase in traffic. Therefore, the city asked for help to determine those property prices, as they needed to give compensation to those people who would be affected by the construction. If the city was challenged in court over the compensation claims, we would need to determine the loss of market value for each homeowner and defend our strategy.


## 2. Data

The dataset in this project can be downloaded from  [here.](https://github.com/yadabasac/project/blob/main/4.%20Predicting%20property%20prices%20with%20regression%20(R%20Programming)/1.%20Dataset/Property%20features%20dataset.csv)

Below is the exploratory data analysis of the attributes we will use to predict a property price.
**Table 1:**
| Attribute  | Mean | Standar Deviation |
| ------------- | ------------- |------------- |
| Area of lot (sqft)	 | 11,959.63	 | 9,593.12
| Area of frontage (sqft)	 | 902.63	 | 255.55
| Traffic counts (vehicles per day)	 | 20,221.15	 | 8,368.87
| House type	 | NA	 | NA
| One and a half Stories (%)	 | 0.09	 | 0.28
| Two Stories (%)	 | 0.15	 | 0.36
| Interior condition	 | NA	 | NA
| Average interior condition (%)	 | 0.45	 | 0.5
| Good interior condition (%)	 | 0.34	 | 0.47
| Excellent interior condition (%)	 | 0.12	 | 0.32
| Four lane road	 | 0.33	 | 0.47

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

## 5. References

1.	Kim, Y. J., Choi, S., Briceno, S., & Mavris, D. (2016). A Deep Learning Approach to Flight Delay Prediction. In 35th Digital Avionics Systems Conference (DASC).
2.	Chakrabarty, N. (2019). A Data Mining Approach to Flight Arrival Delay Prediction for American Airlines. In 9th Annual Information Technology, Electromechanical Engineering and Microelectronics Conference (IEMECON).


