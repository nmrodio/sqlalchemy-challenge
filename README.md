# **sqlalchemy-challenge** #

--------

## **Project Goal** ##
This project leverages Python to explore and analyze climate data for Honolulu, Hawaii, with a focus on facilitating informed vacation planning. Overall, this project demonstrates the creation of a climate analysis toolkit and a corresponding API, empowering users to make data-driven decisions for their Honolulu vacation.

**Key Functionalities:**

* **Data Acquisition:** Establish a connection to a SQLite database containing climate information using SQLAlchemy.
* **Data Exploration:** Utilize SQLAlchemy's Object-Relational Mapping (ORM) queries to delve into the climate data.
* **Data Manipulation** and Analysis: Employ Pandas for data wrangling and insightful analysis.
* **Data Visualization:** Generate informative visualizations with Matplotlib to better understand climate patterns.
* **API Development:** Construct a Flask application to provide access to processed climate data via well-defined routes.

--------
## **climate_starter.ipynb Graph Results** ##


![Screenshot 2024-04-14 123257](https://github.com/nmrodio/sqlalchemy-challenge/assets/157527614/f7b8d460-d85c-460c-8bc5-fcc618c38f4d)



![Screenshot 2024-04-14 123315](https://github.com/nmrodio/sqlalchemy-challenge/assets/157527614/fd314d45-28cf-46cc-a023-359077cbe840)



## **app.py API Routes Preview** ##

**Homepage:** http://127.0.0.1:5000/

![Screenshot 2024-04-14 123551](https://github.com/nmrodio/sqlalchemy-challenge/assets/157527614/483c4b4f-58f3-453c-aea6-f56c9e425fe6)

**Precipitation:** http://127.0.0.1:5000/api/v1.0/precipitation

![Screenshot 2024-04-14 123619](https://github.com/nmrodio/sqlalchemy-challenge/assets/157527614/3206e1d7-bf85-489f-8bbd-8fd4b1a5916a)

**Stations:** http://127.0.0.1:5000/api/v1.0/stations

![Screenshot 2024-04-14 123648](https://github.com/nmrodio/sqlalchemy-challenge/assets/157527614/feb83dfc-7ac1-4819-9ab2-0504423ae5b7)

**Tobs:** http://127.0.0.1:5000/api/v1.0/tobs

![Screenshot 2024-04-14 123707](https://github.com/nmrodio/sqlalchemy-challenge/assets/157527614/3ff69a28-70fe-483f-8b38-0d09af02670b)

**Start Date:** http://127.0.0.1:5000/api/v1.0/start

![Screenshot 2024-04-14 123743](https://github.com/nmrodio/sqlalchemy-challenge/assets/157527614/3a500d6d-6314-4fd0-bfb9-2b4882c31a31)

**Start\End Date:** http://127.0.0.1:5000/api/v1.0/start/end

![Screenshot 2024-04-14 123834](https://github.com/nmrodio/sqlalchemy-challenge/assets/157527614/3769e5c4-a9d7-4b7e-be44-2cace537c48b)
