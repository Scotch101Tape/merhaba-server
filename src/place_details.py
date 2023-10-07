# Libs
import googlemaps
from flask import jsonify
from credentials import google_maps_key

# Google maps stuff
client = googlemaps.Client(key=google_maps_key())

def _place_details_path(request):
  try:
    # Get the data from the request
    place_id = request.json["placeId"]
  
    # Get the result
    # We are grabbing the opening hours, phone number, and website
    result = client.place(
      place_id,
      language = "en", # May change in near future
      fields = ["international_phone_number", "website"]
    )["result"]
  
    # Return the result
    print(result)
    return jsonify(result)
  except:
    # If there is any errors return 400
    return "", 400
