# Libs
import googlemaps
from flask import jsonify
from credentials import google_maps_key

# Codes for types of places
CODES = {
  "RESTAURANT": 1, # Unused atm
  "GROCERY": 2,
  "MOSQUE": 3,
  "CLOTHING": 4
}

# Google maps stuff
client = googlemaps.Client(key=google_maps_key())

def _find_places_path(request):
  try:
    # Get the data from the request
    code = request.json["code"]
    location = request.json["location"]

    # Choose a query for the api based on the code sent
    query = ""
    if (code == CODES["GROCERY"]):
      query = "halal grocery"
    elif (code == CODES["MOSQUE"]):
      query = "mosque"
    elif (code == CODES["CLOTHING"]):
      query = "islamic clothing"
    else:
      raise "Not yet implemented"

    # Get the results
    results = client.places(
      query,
      location=location,
    )["results"]

    # Return the results
    return jsonify(results)
  except:
    # If there is any errors return 400
    return "", 400
