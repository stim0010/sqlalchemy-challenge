from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():

@app.route("/api/v1.0/precipitation")
def precipitation():

    jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():

    jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():

    jsonify(tobs)

@app.route("/api/v1.0/<start>` and `/api/v1.0/<start>/<end>")
def 

if __name__ == "__main__":
    app.run(debug=True)