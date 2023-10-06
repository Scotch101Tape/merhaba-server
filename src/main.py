# Lib
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Modules
from translate import _translate_path
from find_places import _find_places_path
from security import security_check

# To load the .env
load_dotenv()

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
