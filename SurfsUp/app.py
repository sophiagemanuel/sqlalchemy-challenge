# Import the dependencies.
#Using dependencies found in the app.py of "10-Ins_Flask_with_ORM" from class 10.3
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
# Creating routes of "/", "/api/v1.0/precipitation", "/api/v1.0/stations", "/api/v1.0/tobs", "/api/v1.0/<start>", and "/api/v1.0/<start>/<end>"

@app.route("/")
def welcome():
    return(
        f"Welcome to the homepage of my Hawaii Climate API<br>"
        f"Here are all the available routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"For the next two:"
        f"Enter start date as: YYYY-MM-DD"
        f"Enter start/end date as: YYYY-MM-DD/YYYY-MM-DD"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end><br>"
    )

#Percipitation
@app.route("/api/v1.0/precipitation")
def percipitation():
    session = Session(engine)
    year = dt.date(2017, 8, 23)-dt.timedelta(days=365)
    previous_year = dt.date(percipitation.year, percipitation.month, percipitation.day)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date>=previous_year).order_by(measurement.date.desc()).all()
    p_dict = dict(results)

    print(f"The results for Percipitation: {p_dict}")
    print("Out of Percipiration section")
    return jsonify(p_dict)

#Stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    sel = [station.station, station.name, station.latitude, station.longitude, station.elevation]
    s_results = session.query(*sel).all()
    session.close()

    stations=[]
    for station,name,latitude,longitude,elevation in s_results:
        station_dict={}
        station_dict['Station']=station
        station_dict['Lat']=latitude
        station_dict['Lon']=longitude
        station_dict['Elevation']=elevation
        stations.append(station_dict)

    return jsonify(stations)

#Tobs USC00519281
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    tobs_results = session.query(measurement.tobs).filter(measurement.station=='USC00519281').filter(measurement.date>='2016-08-23').all()

    tobs_list = []
    for date, tobs in tobs_results:
        tobs_dict={}
        tobs_dict['Date']=date
        tobs_dict['Tobs']=tobs
        tobs_list.append(tobs_dict)
    return jsonify(tobs)

#Start
@app.route("/api/v1.0/<start>")
def start_temp(start):
    session = Session(engine)
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).all()
    session.close()

    temps=[]
    for min_temp,avg_temp,max_temp in results:
        temp_dict = {}
        temp_dict['Minimum Temp']= min_temp
        temp_dict['Average Temp']= avg_temp
        temp_dict['Maximum Temp']=max_temp
        temps.append(temp_dict)
    return jsonify(temps)

#Start/End
@app.route("/api/v1.0/<start>/<end>")
def start_end_temps(start,end):
    session = Session(engine)
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()
    session.close()

    temps=[]
    for min_temp,avg_temp,max_temp in results:
        temp_dict = {}
        temp_dict['Minimum Temp']= min_temp
        temp_dict['Average Temp']= avg_temp
        temp_dict['Maximum Temp']=max_temp
        temps.append(temp_dict)
    return jsonify(temps)


if __name__ == '__main__':
    app.run(debug=True)
