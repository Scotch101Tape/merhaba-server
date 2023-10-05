import os
from flask import Flask, request, jsonify

from translate import translate_path

app = Flask(__name__)

@app.route("/")
def hello():
  return "hello"

@app.route("/translate")
def translate_path():
  return translate_path(request)
