from google.cloud import translate_v2 as translate
from credentials import credentials
from flask import jsonify

translate_client = translate.Client(credentials=credentials())

def _translate_path(request):
  try:
    text = request.json["text"]
    target = request.json["target"]
    if target != "en" and target != "ar":
      raise "target not either arabic or english"
  
    translation = translate_client.translate(text, target_language=target)["translatedText"]
    return jsonify({
      "translation": translation,
      "text": text,
      "target": target
    })
  except:
    print("ERROR IN TRANSLATION")
    return "", 400
