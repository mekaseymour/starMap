from flask import Flask, render_template, request
import requests
import os
import googlemaps
from datetime import datetime

app = Flask(__name__)

@app.route('/getcity')
def coordinates():

    gmaps = googlemaps.Client(key='AIzaSyDbhD3BxXgIRooBSvYwfhG8GwP1ChxVy-E')

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    # reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    #r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDbhD3BxXgIRooBSvYwfhG8GwP1ChxVy-E')
    #json_object = r.json()

    #lat = float(json_object['results']['geometry'])

    return render_template('index.html', data=geocode_result)

if __name__ == '__main__':
    # port = int(os.getenv('PORT', 5000))
    app.run(debug=True)

    #, host='0.0.0.0', port=port)
