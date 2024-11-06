# Are financial institution providing mortgages biased against some races? (R Programming)

## Contents

1. Project Overview
2. Methodology
3. Data
4. Results and Evaluation
5. Code Structure

![2](https://github.com/user-attachments/assets/3a03aba1-ce77-46e4-b59c-bb55f67e2341)


## 1. Project Overview

In this project, we aim to use data gathered in Boston in 1990 to determine whether mortgage lenders discriminate against some races. The question we seek to answer is: Can we conclude that financial institutions providing mortgages show bias against races? In summary, our findings indicate that minorities are subject to discrimination, which we will dive into further below.


## 2. Methodology

Our main purpose is to assess whether mortgage lending institutions discriminate against minorities. We use both logistic and probit regressions to predict the probability of mortgage loan approval for each race: Whites, Blacks, and Hispanics. The formula for our regression is:

![Screenshot (223)](https://github.com/user-attachments/assets/9cf3e556-2fc2-4108-ae8b-0f1962a7ee83)


The abbreviations of the above independent variables are defined as below:
MARRIED = 1 if married, = 0 otherwise
GDLIN = 1 if credit history meets guidelines, = 0 otherwise
OBRAT = other obligations as a percent of total income
BLACK = 1 if black, = 0 otherwise
HISPAN = 1 if Hispanic, = 0 otherwise
LOANPRC = loan amount/purchase price

Maximum likelihood estimation is used to obtain the coefficients of each model. Thus, our estimated coefficients maximize the log-likelihood of each regression. To evaluate the goodness-of-fit of each model, we report the pseudo R-squared. There are various ways of calculating pseudo R-squared but we use the following formula: 1 – Lur / L0, where Lur is the log-likelihood function for the estimated model and L0 is the log-likelihood function in the model with only an intercept.   
We also calculate the probability for each applicant using the estimated coefficients of each model. Then, we define the independent variable, mortgage lending decision, as ‘Approved’ if the predicted probability is at least .5, and ‘Disapproved’ otherwise. We report the percentage correctly predicted using this way of calculation.

## 3. Data
The dataset used in this project can be downloaded [here.](https://github.com/yadabasac/project/blob/main/5.%20Are%20financial%20institutions%20providing%20mortgages%20biased%20against%20some%20races%3F%20(R%20Programming)/1.%20Dataset.csv)

**Table 1: Descriptive Statistics for Quantitative Variables**
| Variables	| Minimum	| Maximum	| Mean	| Median	| Standard Deviation |
| ------------- | ------------- |------------- |------------- |------------- |------------- | 
| Loan amount/purchase price (%)	|2.11  	|100	|76.08	|80.00	|16.76
|Other obligations as a percent of total income (%)	|0.00	|95.00	|32.37	|33.00	|8.25

**Table 2: Descriptive Statistics for Qualitative Variables**
| Variable	| Proportion |
| ------------- | ------------- |
|Race (%) |	|
|   ---White	| 84.70|
|   ---Black	| 9.90|
|   ---Hispanic	| 5.40|
|Marital Status (%)| |	
|   ---Single	| 34.20|
|   ---Married	| 65.80|
|Approval Rate (%) |	|
|   ---Approved	| 87.90|
|   ---Disapproved	|12.10|
|Credit history meets guidelines (%) | |	
|   ---Yes	| 91.40|
|   ---No	| 8.60|
|Gender (%) |	|
|   ---Male	| 81.40|
|   ---Female	| 18.60|
| Sample Size	| 1,937|

The median Loan-to-Value (LTV) ratio, representing the percentage of the house value financed by the sample population, is 80%. Furthermore, the median of other financial obligations accounts for 33% of total income. Looking at the descriptive statistics for qualitative variables, 84% of applicants identify as white, while 9.9% identify as Black and 5.4% as Hispanic. In terms of marital status, 65.8% of applicants are married, while the remaining 34.2% are single. Examining the approval rate in relation to credit history guidelines, 91% of applicants meet the credit history requirements, yet the approval rate stands at 87.9%, indicating that some applicants with acceptable credit history are still denied approval. Notably, the dataset reveals that 81.4% of applicants are male, while only 18.6% are female.
