from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
from flask import jsonify

credentials = service_account.Credentials.from_service_account_file("google-env.json")
translate_client = translate.Client(credentials=credentials)

def translate_path(request):
  try:
    text = request.json["text"]
    target = request.json["target"]
    if target != "en" and target != "ar":
      raise "target not either arabic or english"

    translation = translate_client.translate(text, target_language=target)
    return jsonify({
      translation,
      text,
      target
    })
  except:
    print("ERROR IN TRANSLATION")
    return 400
