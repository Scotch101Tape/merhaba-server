# Lib
from flask import Flask, request, jsonify

# Modules
from translate import _translate_path
from find_places import _find_places_path
from place_details import _place_details_path
from security import security_check

# Flask stuff
app = Flask(__name__)

# Index route, nothing essential or important
@app.route("/")
def hello():
  return "hello"

# translate route, returns a translation
@app.route("/translate", methods=["POST"])
def translate_path():
  if (security_check):
    return _translate_path(request)
  else:
    return "", 400

# find places route, returns places of interest near a location
@app.route("/find-places", methods=["POST"])
def find_places_path():
  if (security_check):
    return _find_places_path(request)
  else:
    return "", 400

# find places route, returns places of interest near a location
@app.route("/place-details", methods=["POST"])
def place_details_path():
  if (security_check):
    return _place_details_path(request)
  else:
    return "", 400
