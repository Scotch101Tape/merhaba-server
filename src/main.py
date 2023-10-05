import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from translate import _translate_path
from security import security_check

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello():
  return "hello"

@app.route("/translate", methods=["POST"])
def translate_path():
  if (security_check):
    return _translate_path(request)
  else:
    return "", 400
