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

To come up with reasonable compensations for residential properties, we decided to use the multiple regression model. It gives the most accurate numbers by using a formula to calculate prices while the traditional methods allow different evaluators to say different prices.

Generally, the price of a home is based on different factors and owners’ decisions. For example, house size, lot size, home features, interior or exterior condition, location, etc. 

## 3. Code Structure
```
#Import Data
#-- Set working directory: Session --> Set Working Directory --> To Source File Location
dat <- read.csv("Springbank Drive Revised2.csv", header=TRUE)  

#Print column names on the screen
colnames(dat) 
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

#Generate correlation matrix
cor(cbind(PRICE, One.and.a.Half.Storey, Two.Storey, LOTAREA, LFA, Average.Interior.Condition, Good.Interior.Condition, Excellent.Interior.Condition, LANESRD, TRAFCOUNT)) #cbind creates a matrix
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
#Regress price on lanesrd and others
mod.1 <- lm(PRICE ~ One.and.a.Half.Storey + Two.Storey + LOTAREA + LFA + Average.Interior.Condition + Good.Interior.Condition + Excellent.Interior.Condition + LANESRD)
#Present Parameter Estimates, Coefficient of Determination, etc.
summary(mod.1)
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
#Extract standardized residuals and predicted values
standardized.residual1 = rstandard(mod.1)
predicted.saleprice1 <- predict(mod.1)

plot(predicted.saleprice1,standardized.residual1)

```

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


