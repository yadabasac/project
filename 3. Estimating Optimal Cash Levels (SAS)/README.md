# Estimating Optimal Cash Levels (SAS

## Contents

1. Project Overview
2. Data-Preprocessing
3. Data Exploration and Correlation Analysis
4. Regression Analysis
5. Recommendations
6. References

![Screenshot of a cash level](https://miro.medium.com/v2/resize:fit:828/format:webp/1*bL3IO7qjRrJEBnNUbXwWTA.png)

## 1. Project Overview

According to 'Implications of Insufficient and Excess Cash for Future Performance' by Oler and Picconi (2014), there is an increasing need to understand the impact of cash holdings on future performance and stock returns, as firms report growing cash reserves. The project discusses the static trade-off model, suggesting that each firm's optimal cash level balances the marginal benefits and costs of additional cash holdings. This balance is particularly critical for small corporations, which may lack alternative financing options and depend heavily on their cash reserves for operational continuity, especially during turbulent times like the recent pandemic. Conversely, large corporations, such as Apple, despite holding significant cash reserves for long-term development, face the risk of stunted growth due to potential resource underutilization. This analysis explores the nuanced implications of maintaining an optimal cash level, emphasizing the balance between ensuring liquidity for immediate needs and strategic cash allocation for future growth and stability across businesses of varying scales.

## 2. Data-Preprocessing

In this project, data pre-processing involves pulling data from the website (https://wrds-www.wharton.upenn.edu/), specifically from COMPUSTAT. This process includes cleaning, merging, and removing outliers from the data. Depending on the variables needed, the data extracted will vary. We removed missing values, such as cash, cash equivalents, total assets, net sales, etc. The data spans from 1987 to 2020, compared to the 1989-2008 range in the referenced paper. Companies in the utilities and financial sectors are excluded due to unique regulatory requirements on cash and investments. Firms with stock prices under 2 USD are also omitted. After computing the desired variables from various datasets, we merge them into one table and apply Winsorization at the 1% level to limit the impact of outliers, enhancing the robustness of our statistical inferences. The final dataset includes 116,099 firm-year observations for our cash estimation model, a significant increase from the 64,603 observations in the original paper.

## 3. Data Exploration and Correlation Analysis

In our analysis, cash levels were winsorized at the 1 percent level to mitigate the influence of outliers. Despite this, notable outliers persist, evidenced by a mean of 0.48 and a median of 0.11. Our dataset indicates a median firm size of $270 million and a median age of 12.4 years. 
The analysis reveals a negative correlation of cash levels with variables such as firm size, net working capital, dividend dummy, cash from operations, and firm age. Conversely, there is a positive correlation with capital expenditures, industry sigma, R&D, sales growth, tax burden, and managerial ability. To ensure the robustness of our regression model, all variables were included, as we observed no significant correlation between any pair of variables, thus mitigating concerns of multicollinearity.            

## 4. Regression Analysis

Our regression results align with Oler et al.'s findings regarding firm size, net working capital, capital expenditures, industry sigma, sales growth, R&D, cash from operations, firm age, and tax burden on foreign income. However, our model reveals a significantly negative coefficient for the dividend dummy, in contrast to Oler et al.'s positive coefficient. We added an additional variable, managerial ability, to their model, which yielded a significantly positive coefficient. Our adjusted R-squared is 46.54%, compared to the 48.3% reported by Oler et al.
In summary, our findings indicate that firms tend to hold more cash for higher capital expenditures, R&D, sales growth, and potential extra taxes on foreign income, as well as in response to higher uncertainty in cash flows (indicated by industry sigma). Nevertheless, firms hold less cash when they have easier access to capital or bond markets (proxied by size and age), higher cash inflows from operations, or greater net working capital.

![image](https://github.com/user-attachments/assets/6ca54066-f1b4-4972-b560-a888fb15b284)

## 5. Recommendations

Our model aids management teams in determining a firm's optimal cash level, tailored to its unique structure. For example, if a firm wants to expand its operations, thus expecting higher sales growth, then our model can predict how much a firm should increase its cash level. Similarly, if a firm is expecting more cash inflow from its operations, our model can help them decide how much they should decrease their cash level. 
Despite this, the level of cash in each company should be considered together with the specific economic events in the country, and the specific events in the industry the company is operating. The varying positive and negative coefficients on year and industry dummies in our model indicate that major economic or industry events can also influence the optimal level of cash.

## 6. References

Oler, D. K., and Picconi, M. P. 2014. Implications of Insufficient and Excess Cash for Future Performances. Contemporary Accounting Research Vol. 31 No. 1 (Spring 2014) pp. 253-283. 
