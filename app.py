# Import the dependencies
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import desc
from datetime import datetime
from sqlalchemy.types import DateTime
from flask import request
from json import JSONEncoder


#################################################
# Database Setup
#################################################

engine = create_engine(r"sqlite:///C:\Users\Qazi Fabia Hoq\OneDrive\Desktop\sqlalchemy-challenge\Resources\hawaii.sqlite")

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dt.datetime):
            return obj.isoformat()
        return super().default(obj)


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
app.json_encoder = CustomJSONEncoder
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
    # Convert date strings to datetime objects
    start_date = dt.datetime.strptime('2016-08-23', '%Y-%m-%d')
    end_date = dt.datetime.strptime('2017-08-23', '%Y-%m-%d')

    # Perform the query to retrieve the precipitation data for the specified date range
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()

    # Convert the query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    session.close()  # Close the session
    return jsonify(precipitation_data)



@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    # Perform the query to retrieve the list of stations
    results = session.query(Station.station).all()

    # Convert the query results to a list
    station_list = [station[0] for station in results]
    session.close()  # Close the session
    return jsonify(station_list)



# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    # Find the most active station based on the number of observations
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()

    if most_active_station:
        most_active_station_id = most_active_station[0]

        # Perform the query to retrieve the last 12 months of TOBS data for the most-active station
        results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.station == most_active_station_id).all()

        # Convert the query results to a list of dictionaries without converting date to string
        tobs_data = [{"date": str(date), "tobs": tobs} for date, tobs in results]

        session.close()  # Close the session
        return jsonify(tobs_data), 200, {'Content-Type': 'application/json; charset=utf-8'}
    else:
        session.close()  # Close the session
        return jsonify({"error": "No data found"}), 404




@app.route("/api/v1.0/start")
def start():
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date."""
    # Get the start date from the query parameters
    start_date_str = request.args.get('start')

    if not start_date_str:
        return jsonify({"error": "Start date is required"}), 400

    # Convert the start date string to a datetime object
    start_date = dt.datetime.strptime(start_date_str, '%Y-%m-%d')

    # Perform the query to calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

    # Convert the query results to a list
    temperature_stats = {"TMIN": results[0][0], "TAVG": results[0][1], "TMAX": results[0][2]}
    session.close()  # Close the session
    return jsonify(temperature_stats)





@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start-end date range."""
    
    # Convert date strings to datetime objects
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')

    # Perform the query to calculate TMIN, TAVG, and TMAX for the specified start-end date range
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()

    # Convert the query results to a list
    temperature_stats = {"TMIN": results[0][0], "TAVG": results[0][1], "TMAX": results[0][2]}
    session.close()  # Close the session
    return jsonify(temperature_stats)



# Showing:
if __name__ == '__main__':
    app.run(debug=True)
