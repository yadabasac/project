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




## 3. Results and Evaluation

We built two models. Model I estimates house prices based on whether they are located on a typical residential road or four-lane road and other variables. Model II uses traffic counts instead of a dummy variable showing whether a house located on a typical residential road or four-lane road. Variables in our models are chosen because we think that they are important in determining our house prices and they do not show any multicollinearity problems.

### 3.1. Regression Results
**Table 2: Regression Results**
| Description  | Model I Coeff.| Model I Std. error | Model II Coeff.| Model II Std. error | 
| ------------- | ------------- |------------- |------------- |------------- |
| Intercept	 | 86,024.87***	 | 11,194.30	 | 97,122.36***	 | 12,959.83 | 
| One and a half Storey	 | 619.62	 | 8,588.25	 | -1,369.40	 | 8,487.06 | 
| Two Storey	 | 6,556.90	 | 6,979.82	 | 6,227.66	 | 6,827.73 | 
| Area of lot	 | 1.06***	 | 0.24	 | 0.94***	 | 0.24 | 
| Area of frontage	 | 26.48**	 | 10.03	 | 28.16**	 | 9.83 | 
| Average interior condition	 | 10,102.82	 | 7,980.86	 | 9,348.79	 | 7,913.32 | 
| Good interior condition	 | 20,615.00*	 | 8,463.22	 | 20,556.86*	 | 8,406.02 | 
| Excellent interior condition	 | 26,144.93*	 | 9,973.72	 | 26,155.99**	 | 9,895.76 | 
| Four lane road	 | -11,394.39*	 | 5,191.42	 | NA	 | NA | 
| Traffic counts	 | NA	 | NA	 | -0.71*	 | 0.29 | 

**Table 3: Model Fitness**
| Description  | Model I | Model I | 
| ------------- | ------------- |------------- | 
| Sample Size	 | 104	 | 104 |
| F statistics | 9.04*** | 9.32*** |
| Adjusted R2	 | 0.38	 | 0.39 |
| R2	 | 0.43	 | 0.44 |

```
Notes:
*   : 	p < 0.05
**  : 	p < 0.01
*** : 	p < 0.001
```

### 3.2. Explaining Results

For each additional square footage of frontage area, on average it increases the home price by $26.48 holding the house type, area of lot, Interior condition constant in Model I. It raises the price by $28.16 holding the other variables in Model II. If the house is on four lane road in Model I, on average it decreases by $11,394.39 holding the other variables constant. For each additional traffic counts in Model II, on average it decreases by $0.71 controlling for other variables.

In Model I that includes a set of dummy variables for the house type, interior condition, four-lane road. The home price associated with two storeies house cost average $6,556.90 more than a one storey housecontrolling for other variables. In Model II, including a measure of the traffic amount, The home price associated with two storeies house cost average $1,369.40 less. But in both models, interior condition is not statiscally significant. The signs of the interior condition  are intuitive.

As we estimate the home prices in order to come up with reasonable compensation, the R squared from the mutiple regression models table can be use as a measure to determine how well our models make predictions. From the table, not only all the statistically significant variables (area of lot, area of frontage, and dummy variables for the interior condition) increases the home price as anticipated. Our models are also acceptable because R squared in Model I is 0.43 and in Model II is 0.44.

The city can use either Model I (lane sideroad) or Model II (traffic counts) to calculate compensation amounts for the affected homeowners. Model II is used to calculate compensation using data of traffic counts. Since the traffic counts on the newly paved four lane road are expected to reach 33,000 cars per day, the mathematical expression for Model II in calculating compensation can be expressed as below:
 
Compensation (Model II) = 12,000.00 + 28.16 * (Loss frontage) + 0.71 * (33,000 - current traffic counts) 

On the other hand, Model I is different from Model II in that it estimates house prices based on whether they are located on a typical residential road or four-lane road. Thus, mathematical expression in calculating compensation for house currently located on a two-lane road is: 
 
Compensation (Model I) = 12,000.00 + 26.48 * (Loss frontage) + 11,394.39
 
If a house is currently located on a four-lane road, then the following expression should be used.
 
Compensation (Model I) = 12,000.00 + 26.48 * (Loss frontage)

## 4. Code Structure

### 4.1 Importing the dataset
```
#Import Data

#-- Set working directory: Session --> Set Working Directory --> To Source File Location
dat <- read.csv("Springbank Drive Revised2.csv", header=TRUE)  

```

### 4.2 Printing colunm names
```
#Print column names on the screen
colnames(dat) 
```
```
##  [1] "Property.."                         "Address"                           
##  [3] "Sales.Date"                         "HSETYPE"                           
##  [5] "One.and.a.Half.Storey"              "Two.Storey"                        
##  [7] "AGEYR"                              "LOTAREA"                           
##  [9] "LFA"                                "Discurb"                           
## [11] "EXTAMEN"                            "Minor.Exterior.Amenities"          
## [13] "Two.or.Three.Extra.Amenities"       "More.than.Three.Exterior.Amenities"
## [15] "EXTFINFACTOR"                       "Only.Brick"                        
## [17] "GAR"                                "Carport"                           
## [19] "One.Car.Garage"                     "Two.Car.Garage"                    
## [21] "STSCAPE"                            "Average.View"                      
## [23] "Good.View"                          "CENAIR"                            
## [25] "POOL"                               "INTCOND"                           
## [27] "Average.Interior.Condition"         "Good.Interior.Condition"           
## [29] "Excellent.Interior.Condition"       "BSMTFINAREA"                       
## [31] "BI.AMEN.APPL"                       "LANESRD"                           
## [33] "TRAFCOUNT"                          "PRICE"
```

```
#Extract variables to be used in the analyses
PRICE <- dat[,"PRICE"]
One.and.a.Half.Storey <- dat[,"One.and.a.Half.Storey"]
Two.Storey <- dat[,"Two.Storey"]
AGEYR <- dat[,"AGEYR"]
LOTAREA <- dat[,"LOTAREA"]
LFA <- dat[,"LFA"]
Discurb <- dat[,"Discurb"]
Only.Brick <- dat[,"Only.Brick"]
Carport <- dat[,"Carport"]
One.Car.Garage <- dat[,"One.Car.Garage"]
Two.Car.Garage <- dat[,"Two.Car.Garage"]
CENAIR <- dat[,"CENAIR"]
Average.Interior.Condition <- dat[,"Average.Interior.Condition"]
Good.Interior.Condition <- dat[,"Good.Interior.Condition"]
Excellent.Interior.Condition <- dat[,"Excellent.Interior.Condition"]
LANESRD <- dat[,"LANESRD"]
TRAFCOUNT <- dat[,"TRAFCOUNT"]
```

### 4.1 Producing correlation matrix
```
#Generate correlation matrix
cor(cbind(PRICE, One.and.a.Half.Storey, Two.Storey, LOTAREA, LFA, Average.Interior.Condition, Good.Interior.Condition, Excellent.Interior.Condition, LANESRD, TRAFCOUNT)) #cbind creates a matrix
```
```
##                                    PRICE One.and.a.Half.Storey  Two.Storey
## PRICE                         1.00000000           0.040971000 -0.06795999
## One.and.a.Half.Storey         0.04097100           1.000000000 -0.13124359
## Two.Storey                   -0.06795999          -0.131243592  1.00000000
## LOTAREA                       0.46486165          -0.052554087 -0.10011186
## LFA                           0.40025782           0.307324414  0.13879021
## Average.Interior.Condition   -0.21213447           0.064091778  0.04119100
## Good.Interior.Condition       0.24754611          -0.146838801 -0.13449056
## Excellent.Interior.Condition  0.17764607           0.102927733 -0.15399810
## LANESRD                      -0.34800933           0.004206101  0.32776415
## TRAFCOUNT                    -0.39711908          -0.059501520  0.31506234

##                                  LOTAREA         LFA Average.Interior.Condition
## PRICE                         0.46486165  0.40025782                -0.21213447
## One.and.a.Half.Storey        -0.05255409  0.30732441                 0.06409178
## Two.Storey                   -0.10011186  0.13879021                 0.04119100
## LOTAREA                       1.00000000  0.21696083                 0.06249103
## LFA                           0.21696083  1.00000000                -0.16718949
## Average.Interior.Condition    0.06249103 -0.16718949                 1.00000000
## Good.Interior.Condition       0.02431326  0.19742362                -0.64672698
## Excellent.Interior.Condition  0.02855017 -0.03540225                -0.32795043
## LANESRD                      -0.13325383 -0.17802569                 0.27325886
## TRAFCOUNT                    -0.28888552 -0.15172499                 0.15566992

##                              Good.Interior.Condition
## PRICE                                     0.24754611
## One.and.a.Half.Storey                    -0.14683880
## Two.Storey                               -0.13449056
## LOTAREA                                   0.02431326
## LFA                                       0.19742362
## Average.Interior.Condition               -0.64672698
## Good.Interior.Condition                   1.00000000
## Excellent.Interior.Condition             -0.25722086
## LANESRD                                  -0.23608554
## TRAFCOUNT                                -0.15084884

##                              Excellent.Interior.Condition      LANESRD
## PRICE                                          0.17764607 -0.348009325
## One.and.a.Half.Storey                          0.10292773  0.004206101
## Two.Storey                                    -0.15399810  0.327764146
## LOTAREA                                        0.02855017 -0.133253829
## LFA                                           -0.03540225 -0.178025693
## Average.Interior.Condition                    -0.32795043  0.273258862
## Good.Interior.Condition                       -0.25722086 -0.236085539
## Excellent.Interior.Condition                   1.00000000 -0.187542875
## LANESRD                                       -0.18754287  1.000000000
## TRAFCOUNT                                     -0.16136359  0.735844388

##                                TRAFCOUNT
## PRICE                        -0.39711908
## One.and.a.Half.Storey        -0.05950152
## Two.Storey                    0.31506234
## LOTAREA                      -0.28888552
## LFA                          -0.15172499
## Average.Interior.Condition    0.15566992
## Good.Interior.Condition      -0.15084884
## Excellent.Interior.Condition -0.16136359
## LANESRD                       0.73584439
## TRAFCOUNT                     1.00000000
```

### 4.3 Model 1
```
#Regress price on lanesrd and others
mod.1 <- lm(PRICE ~ One.and.a.Half.Storey + Two.Storey + LOTAREA + LFA + Average.Interior.Condition + Good.Interior.Condition + Excellent.Interior.Condition + LANESRD)
#Present Parameter Estimates, Coefficient of Determination, etc.
summary(mod.1)
```
```
## 
## Call:
## lm(formula = PRICE ~ One.and.a.Half.Storey + Two.Storey + LOTAREA + 
##     LFA + Average.Interior.Condition + Good.Interior.Condition + 
##     Excellent.Interior.Condition + LANESRD)
## 
## Residuals:
##    Min     1Q Median     3Q    Max 
## -49134 -12851  -2744   8373 105800 
## 

## Coefficients:
##                                Estimate Std. Error t value Pr(>|t|)    
## (Intercept)                   8.602e+04  1.119e+04   7.685 1.38e-11 ***
## One.and.a.Half.Storey         6.196e+02  8.588e+03   0.072   0.9426    
## Two.Storey                    6.557e+03  6.980e+03   0.939   0.3499    
## LOTAREA                       1.060e+00  2.382e-01   4.448 2.35e-05 ***
## LFA                           2.649e+01  1.003e+01   2.640   0.0097 ** 
## Average.Interior.Condition    1.010e+04  7.981e+03   1.266   0.2087    
## Good.Interior.Condition       2.062e+04  8.463e+03   2.436   0.0167 *  
## Excellent.Interior.Condition  2.614e+04  9.974e+03   2.621   0.0102 *  
## LANESRD                      -1.139e+04  5.191e+03  -2.195   0.0306 *  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 21770 on 95 degrees of freedom
## Multiple R-squared:  0.4323, Adjusted R-squared:  0.3844 
## F-statistic: 9.041 on 8 and 95 DF,  p-value: 3.722e-09
```
### 4.4 Model 2
```
#Regress price on traffic and others
mod.2 <- lm(PRICE ~ One.and.a.Half.Storey + Two.Storey + LOTAREA + LFA + Average.Interior.Condition + Good.Interior.Condition + Excellent.Interior.Condition + TRAFCOUNT)
#Present Parameter Estimates, Coefficient of Determination, etc.
summary(mod.2)
```
```
## 
## Call:
## lm(formula = PRICE ~ One.and.a.Half.Storey + Two.Storey + LOTAREA + 
##     LFA + Average.Interior.Condition + Good.Interior.Condition + 
##     Excellent.Interior.Condition + TRAFCOUNT)
## 
## Residuals:
##    Min     1Q Median     3Q    Max 
## -49147 -11454  -4083   8775 107709 
## 
## Coefficients:
##                                Estimate Std. Error t value Pr(>|t|)    
## (Intercept)                  97122.3644 12959.8305   7.494 3.45e-11 ***
## One.and.a.Half.Storey        -1369.4012  8487.0637  -0.161 0.872159    
## Two.Storey                    6227.6593  6827.7330   0.912 0.364018    
## LOTAREA                          0.9439     0.2434   3.878 0.000194 ***
## LFA                             28.1570     9.8275   2.865 0.005132 ** 
## Average.Interior.Condition    9348.7954  7913.3229   1.181 0.240393    
## Good.Interior.Condition      20556.8588  8406.0192   2.445 0.016307 *  
## Excellent.Interior.Condition 26155.9874  9895.7640   2.643 0.009608 ** 
## TRAFCOUNT                       -0.7103     0.2869  -2.476 0.015046 *  
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 21630 on 95 degrees of freedom
## Multiple R-squared:  0.4396, Adjusted R-squared:  0.3924 
## F-statistic: 9.316 on 8 and 95 DF,  p-value: 2.098e-09
```

