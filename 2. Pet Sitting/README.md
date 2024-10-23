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

The data used in our project were generated from [Mockaroo.](https://www.mockaroo.com/) 

## 3. Running SQL Queries
### 3.1.  Top 10 Highest Earning Sitters

This SQL query retrieves the sitters who have earned the most money by summing up their transaction amounts in the booking table. It can be used for payroll to determine the highest paid employees.

```
SELECT sitter.sitter_id,
  sitter.sitter_firstname,
  sitter.sitter_lastname,
SUM(booking.transaction_amount) as total_earned
FROM sitter
INNER JOIN booking
ON sitter.sitter_id = booking.sitter_id
GROUP BY sitter.sitter_id
ORDER BY total_earned desc
LIMIT 10;
```
![image](https://github.com/user-attachments/assets/5fa8ae10-7ea3-4193-a823-3adefb5b4163)

### 3.2.  Owners with Unpaid Bills
This SQL query pulls the owners who have unpaid bills. It lists the owners in order of who has the largest outstanding amounts due, so the billing department can determine who should be contacted to pay their outstanding bills.

```
SELECT o.owner_id,
  o.owner_firstname,
  o.owner_lastname,
  SUM(b.transaction_amount) as amount_due
FROM `owner` as o
INNER JOIN booking as b
ON o.owner_id = b.owner_id
INNER JOIN `schedule` as s
ON b.schedule_id = s.schedule_id
WHERE b.transaction_status = 'UNPAID'
AND s.schedule_end_time < NOW()
GROUP BY owner_id
ORDER BY amount_due DESC
LIMIT 10;
```

![image](https://github.com/user-attachments/assets/1c650ce1-3698-4d0c-b50e-b5fe60c1306f)

