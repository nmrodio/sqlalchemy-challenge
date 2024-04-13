# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(autoload_with=engine)

# Save references to each table
# "Measurement" table reference
measurement = base.classes.measurement

# "Station" table reference
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################


######## ------------ HOMEPAGE ROUTE ------------- ###########
# Setting up homepage route that will also list ALL available routes
@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaii Climate App Homepage API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )



######## ------------ PRECIPITATION ROUTE ------------- ###########
@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Retrieve precipitation data for the previous year """

    # Query to find the precipitation data for the previous year
    previous_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= previous_year_date).order_by(measurement.date.desc()).all()

    #Closing "precipitation" session
    session.close()

    # Creating a list of dictionaries [{date: prcp}] from the data found from the query "results"
    precipitation_date_data = []
    for date, prcp in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["prcp"] = prcp
        precipitation_date_data.append(temp_dict)

    # Converting results to JSON
    return jsonify(precipitation_date_data)



######## ------------ STATIONS ROUTE ------------- ###########
@app.route("/api/v1.0/stations")
def stations():
    
    """Retrieve list of stations (ids, names) """

     # Create our session (link) from Python to the DB
    session=Session(engine)

    # Query to find all the station ids(station) and names data
    results = session.query(station.station).all()

    #Closing "stations" session
    session.close()

    # Converting results into a list
    all_stations = list(np.ravel(results))

    # Converting results to JSON
    return jsonify(all_stations)


######## ------------ TOBS ROUTE ------------- ###########
@app.route("/api/v1.0/tobs")
def tobs():
    
    """Retrieve list of tobs for previous year for the most active station"""

     # Create our session (link) from Python to the DB
    session=Session(engine)

    # Query to find the tobs data for the previous year for the most active station
    previous_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(measurement.tobs).\
        filter(measurement.date >= previous_year_date, measurement.station == 'USC00519281').all()

    #Closing "tobs" session
    session.close()

    # Converting results into a list
    previous_year_tobs = list(np.ravel(results))

    # Converting results to JSON
    return jsonify(previous_year_tobs)


######## ------------ SPECIFIC START DATE FOR TEMPS ROUTE ------------- ###########
@app.route("/api/v1.0/<start>")
def start_temp(start):
    
    """Retrieve list of the minimum temperature, average temperature, and maximum temperature for a specified start date"""

    # Converting "start" to datetime format ("%Y%m%d")
    start = dt.datetime.strptime(start, "%Y%m%d")


    # Create our session (link) from Python to the DB
    session=Session(engine)

    # Query to find the the minimum temperature, average temperature, and maximum temperature for a specified start date
    results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
    filter(measurement.date >= start).all()

    # Closing "start_temp" session
    session.close()

    # Converting results into a list
    start_temp_data = list(np.ravel(results))

    # Converting results to JSON
    return jsonify(start_temp_data)


######## ------------ START-END RANGE DATE FOR TEMPS ROUTE ------------- ###########
@app.route("/api/v1.0/<start>/<end>")
def start_end_temp(start,end): 
    
    """Retrieve list of the minimum temperature, average temperature, and maximum temperature for a specified start/end date range"""

    # Create our session (link) from Python to the DB
    session=Session(engine)

    # Converting "start" AND "end" to datetime format ("%Y%m%d")
    start = dt.datetime.strptime(start, "%Y%m%d")
    end = dt.datetime.strptime(end, "%Y%m%d")

    # Query to find the the minimum temperature, average temperature, and maximum temperature for a specified start/end date range
    results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
    filter(measurement.date >= start, measurement.date <= end).all()

    # Closing "start_end_temp" session
    session.close()

    # Converting results into a list
    start_end_temp_data = list(np.ravel(results))

    # Converting results to JSON
    return jsonify(start_end_temp_data)


if __name__ == "__main__":
    app.run(debug=True)
