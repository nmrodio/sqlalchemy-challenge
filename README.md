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

---------------------------

## **How does the code work?** ##
## **climate_starter.ipynb** ##

1) Importing necessary dependencies
2) Creating engine to allow python to connect with the "hawaii.sqlite" database
3) Using automap_base() to define column data types ==> then telling the "connection" to prepare the data and "autoload" the the data from the database using the "engine" connection to the database
4) Using .classes.keys() to visually see all tables that are found in the database => Then saving references for each table as variables (measurement & station)
5) Creating the session (link) from Python to the database
6) First query "most_recent_date" retrieves the last (most recent) date found in the database
7) Next the date one year prior is calculated using datetime as dt functions
8) Second query "one_calendar_year_date_prcp_data" retrieves ALL the data and precipitation scores of only days that are greater than the "previous_year_date" found above
9) Results from "one_calendar_year_date_prcp_data" query are then converting into a pandas dataframe called "hawaii_dates_prcp_data_df" and columns are renamed to "Date" and "Precipitation" respectively ==> Then the dataframe is sorted by "Date" in descending order and ".reset_index(drop=True)" is used to reset and drop the index for a cleaner and more intuitive dataframe
10) The x and y-axis are defined as "Date" and "Precipitation" respectively ==> df.plot method is using to create the plot and labels, title, and a grid are added for better readability
12) "hawaii_dates_prcp_data_df.describe" is then used to calculate and show the summary statistics for the precipitation data
13) The third query "total_stations" retrieves the counts of all UNIQUE stations found in the table "station" using func.count
14) The fourth query "station_activity" is then used to list the stations and their counts in descending order to find the most active stations
15) The fifth query "most_active_station_temp_stats" is used calculate the most active stations's lowest, highest, and average temperature using "func.min", "func.max", and "func.avg"
16) The sixth query "top_station_last_year_temp" retrieves the "tobs" (temperature) for the past year of the most active station ==> The date used to find this data is the results of the query "previous_year_date" defined above
17) Results from "top_station_last_year_temp" query are then converting into a pandas dataframe called "top_station_last_year_temp" and column is renamed to "Temperature"
18) The histogram is then created using "top_station_last_year_temp.hist" method and 12 bins are created for 12 months in a year => Black edges are added to each bin on the histogram and labels, title, gridlines, and a legend are added for better readability
19) The session is finally closed using "session.close()"

## **app.py** ##

