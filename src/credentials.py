from google.oauth2 import service_account
import json
import os

def credentials():
  service_account_json = json.loads(os.environ["GOOGLE_ENV_JSON"])
  return service_account.Credentials.from_service_account_info(service_account_json)
  