# Import the dependencies
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import desc
from datetime import datetime

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///C:\\Users\\Qazi Fabia Hoq\\OneDrive\\Desktop\\module10-sql alchemy\\Starter_Code\\Resources\\hawaii.sqlite")



# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create session from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a dictionary using date as the key and prcp as the value."""
    # The last 12 months of precipitation data
    start_date = '2016-08-23'
    end_date = '2017-08-23'

    # Perform the query to retrieve the precipitation data for the specified date range
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()

    # Convert the query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)


@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    # Perform the query to retrieve the list of stations
    results = session.query(Station.station).all()

    # Convert the query results to a list
    station_list = [station[0] for station in results]

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Query the dates and temperature observations of the most-active station for the previous year of data."""
    # Specify the start and end date for the last 12 months of temperature observation (TOBS) data
    start_date = '2016-08-23'
    end_date = '2017-08-23'

    # Find the most active station based on the number of observations
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()

    if most_active_station:
        most_active_station_id = most_active_station[0]

        # Perform the query to retrieve the last 12 months of TOBS data for the most-active station
        results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date >= start_date).\
            filter(Measurement.date <= end_date).\
            filter(Measurement.station == most_active_station_id).all()

        # Convert the query results to a list of dictionaries
        tobs_data = [{"date": date, "tobs": tobs} for date, tobs in results]

        return jsonify(tobs_data)
    else:
        return jsonify({"error": "No data found"}), 404


@app.route("/api/v1.0/start")
def start():
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date."""
    # Specify the start date
    start_date = '2016-08-23'

    # Perform the query to calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

    # Convert the query results to a list
    temperature_stats = {"TMIN": results[0][0], "TAVG": results[0][1], "TMAX": results[0][2]}

    return jsonify(temperature_stats)




@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start-end date range."""
    # Find the most active station based on the number of observations
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()

    if most_active_station:
        most_active_station_id = most_active_station[0]

        # Perform the query to calculate TMIN, TAVG, and TMAX for the specified start-end date range
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).\
            filter(Measurement.station == most_active_station_id).all()

        # Convert the query results to a list
        temperature_stats = {"TMIN": results[0][0], "TAVG": results[0][1], "TMAX": results[0][2]}

        return jsonify(temperature_stats)
    else:
        return jsonify({"error": "No data found"}), 404


# Showing:
if __name__ == '__main__':
    app.run(debug=True)


