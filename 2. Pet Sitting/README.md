# Implementation of Pet Sitting Database

## Contents

1. Project Overview
2. Data
3. Code Structure
4. Results and Evaluation
5. Future Work
6. References

![overnight-pet-sitting 2205201856012](https://github.com/user-attachments/assets/86aadcd1-0255-44f5-997f-6414fd619736)


## 1. Project Overview

In today’s fast-paced world, pet ownership is on the rise, with more individuals and families welcoming pets into their homes but struggling to have quality time with their pets. Thus, there comes a growing need for reliable and efficient pet care services. Pet Sitters recognizes this market opportunity and aims to capitalize on it by building a pet sitting database to pair professional pet sitters with households requiring pet sitting services. This report outlines the rationale behind this project and highlights the benefits it will bring to the company.

A pet sitting database will enable us to offer a more personalized and tailored experience to our customers. By maintaining comprehensive profiles of each pet and their respective owners, we can capture important details such as dietary preferences, and behavioral traits. This information will enable our pet sitters to provide customized care that meets the unique needs of every pet, fostering stronger relationships with both pets and their owners. Additionally, the database will enable us to track and analyze customer feedback, allowing us to continuously improve the quality of our services and revise our training programs of professional pet sitters.

## 2. Data-Driven Decision Making

The flow chart diagram below shows the design of our database architecture. From our discussions with Pet Sitters, we understand that the company has its on-premises enterprise resource planning (ERP) systems that help it manage its day-to-day business activities, such as accounting, finance, procurement, and human resources. The human resources systems help the company manage its employees, pet sitters and the review related to each pet sitter. In addition, the company is also using customer relationship management (CRM) systems to support its front-office business functions, such as marketing, sales, advertising, and customer service related to pet owners.

![image](https://github.com/user-attachments/assets/0b3e62cb-b035-4659-9f15-dd69680878ab)

As the number of pets requiring pet sitting increases, there is a strong need to integrate their CRM, ERP, and other systems to effectively share data, rather than maintaining several separate sets of data. With a centralized data warehouse, it will be convenient for the company’s analysts to generate reports that can help the management team to make informed decisions. For example, we can find owner cities with the most open schedules for sitters to sign up. We can also show the best rated sitters each year on a dashboard. Moreover, historical data will be stored in our BI system, so trends over time can be presented in reports, such as the top earning sitters or the top watched pets.

Here is our ER model.

![image](https://github.com/user-attachments/assets/2f908533-5c56-4271-931a-2029adb15fc3)


## 3. Populating The Database

The data used in our project were generated from [Mockaroo.](https://www.mockaroo.com/) 

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

