#from google.cloud.speech_v2 import SpeechClient
#from google.cloud.speech_v2.types import cloud_speech
from flask import Flask, request, jsonify
from google.cloud import speech

client = speech.SpeechClient(credentials=google_credentials())

def _translate_speech_path(request):
  
  content = request.files["file"] 
  #audio = speech.RecognitionAudio(content=content)

  #config = speech.RecongnitionConfig(
  #  encoding=speech.RecogntionConfig.AudioEncoding.LINEAR16,
  #  sample_rate_hertz=44100,
  #  langauge_code="en-US"
  #  alternative_langs=["ar"]

  """
    config = cloud_speech.RecognitionConfig(
    auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
    language_codes=["en-US", "ar"],
    model="long",
  )

  project_id = os.environ["PROJECT_ID"]
  
  request = cloud_speech.RecognizeRequest(
    recognizer=f"projects/{project_id}/locations/global/recognizers/_",
    config=config,
    content=content,
  )

  response = client.recognize(request=request)

  transcript = response.results[0].alternatives[0].transcript
  """
  
  return jsonify({
    "text": "hi", 
    "translation": "dsfjksl"
  })
