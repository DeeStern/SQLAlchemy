##Devin Stern
##SQLALCHEMY HOMEWORK
##I do apologize - I couldn't get this to run. I'll have to check in
##with you guys on this flask business. Thanks! -Devin

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

from flask import Flask, jsonify

# Flask Setup
app = Flask(__name__)
    
    ##Define the welcome/home page
@app.route("/")
def home():
    print("Server received request...")
    return "Welcome to the Hawaii Weather Fun-splosion!"

@app.route("/api/v1.0/precipitation")
def precip_func():
    """Precipitation data for dates in data > 8/23/2016"""
    # Query Measurement Table
    precip_results = session.query(measurement.precipitation > 2016-8-23).all()
    
    precip_list = []
    
    for precipitation, date in results:
        prcp_measurement = {}
        precipitation_dict["prcp"] = prcp
        date_dict["date"] = date
        precip_results.append(prcp_measurement)

    return jsonify(prcp_measurement)
    
if __name__ == '__main__':
    app.run(debug=True)  

@app.route("/api/v1.0/stations")

def st_count_funct():
    """Number of stations in the data"""
    #Query station table
st_results = session.query(Station.station).all()
    
    return jsonify(st_results)

if __name__ == '__main__':
    app.run(debug=True)           


@app.route("/api/v1.0/tobs")

def st_count_funct():
    """Tobs for """
    #Query station table
tobs_results = session.query(measurement.tobs, measurement.date > 2016-8-23).all()
    
    return jsonify(tob_results)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/api/v1.0/<start>")
