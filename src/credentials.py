# Libs
from google.oauth2 import service_account
import json
import os
from dotenv import load_dotenv

# To load the .env
load_dotenv()

# Gets the google credentials from .env and formats them for the google libs
def google_credentials():
  service_account_json = json.loads(os.environ["GOOGLE_ENV_JSON"])
  return service_account.Credentials.from_service_account_info(service_account_json)

# In google's infinite wisdom (and laziness) I can't actually use a service account
# for google maps api, so I have to have *another* key
def google_maps_key():
  return os.environ["GOOGLE_MAPS_API_KEY"]
