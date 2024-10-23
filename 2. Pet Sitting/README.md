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

### 3.3.  Pet Species by Hours Watched

The query calculates the total amount of hours that each pet species is watched. Then, it calculates the percentage of hours each pet species is watched, so the company can examine what types of pets the business relies on.

```
SELECT   DISTINCT
      pet.pet_species,
      hours_by_species.hours_watched,
      (hours_by_species.hours_watched / total_watched.total_hours) as perc_of_hours_watched
FROM pet
      INNER JOIN (
        SELECT pet_species,
          SUM((time_to_sec(timediff(schedule_end_time, schedule_start_time))/3600)) as
          hours_watched
      FROM pet
          INNER JOIN `schedule`
          ON pet.pet_id = `schedule`.pet_id
          INNER JOIN booking
          ON `schedule`.schedule_id = booking.schedule_id
      GROUP BY pet_species
) hours_by_species
  INNER JOIN (
    SELECT SUM((time_to_sec(timediff(schedule_end_time, schedule_start_time))/3600)) as
      total_hours
    FROM pet
      INNER JOIN `schedule`
      ON pet.pet_id = `schedule`.pet_id
      INNER JOIN booking
      ON `schedule`.schedule_id = booking.schedule_id
) as total_watched
WHERE hours_by_species.pet_species = pet.pet_species
ORDER BY perc_of_hours_watched DESC;
```

![image](https://github.com/user-attachments/assets/d77a1641-1bb4-45fb-9c8d-acbf93fee078)


### 3.4.  The Dogs Being Watched the Most

The SQL query sums up the number of hours each pet is watched and returns the pets in order of highest number of hours. It allows the company to see the dogs that are continuing to use the service or their top clients.

```
SELECT pet.pet_id,
    pet.pet_name,
    SUM((time_to_sec(timediff(schedule_end_time, schedule_start_time))/3600)) as hours_watched
FROM pet
    INNER JOIN `schedule`
    ON pet.pet_id = `schedule`.pet_id
    INNER JOIN booking
    ON `schedule`.schedule_id = booking.schedule_id
WHERE pet_species like '%Dog%'
GROUP BY pet.pet_id
ORDER BY hours_watched DESC
LIMIT 10;
```

![image](https://github.com/user-attachments/assets/5f2a2497-de60-4f7f-abb7-dc8917e2b974)


### 3.5.  Sitters with the Highest Ratings

The query uses the average and count function to return the sitters who have the highest average rating, and it only includes sitters who have more than one rating. This query could be used by customers to find the best sitters for their pets or for the company to find the top performing employees.

```
SELECT sitter.sitter_id,
    sitter.sitter_firstname,
    sitter.sitter_lastname,
    AVG(review.review_rating) as average_rating,
    COUNT(review.review_id) as number_of_reviews
FROM sitter
    INNER JOIN review
    ON sitter.sitter_id = review.sitter_id
GROUP BY sitter.sitter_id
HAVING COUNT(review.review_id) > 1
ORDER BY average_rating DESC, number_of_reviews DESC
LIMIT 10;
```

![image](https://github.com/user-attachments/assets/7c755b26-55e1-4d1c-9f3f-7129f4b26409)

