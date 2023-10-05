def security_check(request):
  return request.headers.get("X-SECRET-APP-KEY") == os.environ["X_SECRET_APP_KEY"]
  