# SQLAlchemy Climate Analysis and Flask API Project
## Overview:
This comprehensive project, assigned by the University of Toronto Boot Camp Certificate Program, aims to conduct a thorough climate analysis of Honolulu, Hawaii. The analysis utilizes Python, SQLAlchemy, and Flask, providing insights into historical precipitation and temperature data. The project encompasses two main components: a Jupyter Notebook (climate_starter.ipynb) for data exploration and analysis and a Flask API (app.py) for data retrieval and visualization.

## Climate Analysis (climate_starter.ipynb):
Project Objective:
To perform an exhaustive climate analysis using Python, SQLAlchemy, and Pandas, exploring precipitation and temperature data for Honolulu, Hawaii.

## Steps and Findings:

### Database Connection:

Utilized SQLAlchemy to create an engine for connecting to the provided hawaii.sqlite database.
Used automap_base to reflect the tables (station and measurement) into classes.
### Precipitation Analysis:

Identified the most recent date in the dataset.
Calculated the date one year ago from the most recent date.
Executed a query to retrieve precipitation data for the last 12 months.
Stored the query results in a Pandas DataFrame, sorted it by date, and plotted the precipitation data over time.
Calculated and displayed summary statistics for the precipitation data.

### Station Analysis:

Designed queries to calculate the total number of stations and identify the most active stations.
Calculated the lowest, highest, and average temperatures for the most active station.
Executed a query to retrieve the last 12 months of temperature observation (TOBS) data for the most active station.
Plotted the TOBS data as a histogram with bins=12.

### Limitations:
The analysis assumes the provided dataset is representative of the overall climate conditions in Honolulu, Hawaii.
### Data Source:
The data for this project was sourced from the Global Historical Climatology Network-Daily Database (Menne et al., 2012).


## Flask API (app.py):

### Project Objective:
To design and implement a Flask API that provides various routes for accessing climate data from the analyzed dataset.

### Routes and Functionality:
Home Route (/):

Lists all available API routes.
Precipitation Route (/api/v1.0/precipitation):

Converts the query results to a dictionary using date as the key and precipitation as the value.
Stations Route (/api/v1.0/stations):

Returns a JSON list of stations from the dataset.
TOBS Route (/api/v1.0/tobs):

Queries the dates and temperature observations of the most-active station for the previous year of data.
Returns a JSON list of temperature observations for the previous year.
Start Route (/api/v1.0/start):

Accepts the start date as a parameter from the URL.
Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for dates greater than or equal to the start date.
Start/End Route (/api/v1.0/<start>/<end>):

Accepts the start and end dates as parameters from the URL.
Returns a JSON list of the temperature statistics for the specified start-end range.

### Limitations:
The API assumes the availability of a constant and up-to-date database for real-time data access.
Running the Application:
The Flask application can be executed by running the app.py script. The home route (/) provides a list of available routes.

### Data Source:
The project uses climate data sourced from the Global Historical Climatology Network-Daily Database (Menne et al., 2012).


## File Structure:



- main/
    - climate_starter.ipynb
    - app.py
    - README.md
    - resources/
        - hawaii_measurements.csv
        - hawaii_stations.csv
        - hawaii.sqlite
    - pictures/
        - PrecipitationAnalysis_12months.png
        - Temperature_12Months.png
        - 
## Reference:

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910. https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml





