# Libs
from google.cloud import translate_v2 as translate
from credentials import google_credentials
from flask import jsonify

# Google translate stuff
translate_client = translate.Client(credentials=google_credentials())

def _translate_path(request):
  try:
    # Get the data from the request
    text = request.json["text"]
    target = request.json["target"]

    # Only translate into english or arabic (for now)
    if target != "en" and target != "ar":
      raise "target not either arabic or english"

    # Get the translation
    translation = translate_client.translate(text, target_language=target)["translatedText"]

    # Return the translation,
    # as well as data sent like the original text and target language
    return jsonify({
      "translation": translation,
      "text": text,
      "target": target
    })
  except:
    # If there is any errors return 400
    return "", 400
