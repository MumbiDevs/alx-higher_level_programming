import urllib.request
import sys

def get_request_id(url):
  """Fetches the URL and displays the X-Request-Id header value."""
  with urllib.request.urlopen(url) as response:
    headers = response.getheaders()
  
  for header, value in headers:
    if header.lower() == "x-request-id":
      print(value.decode('utf-8'))
      return

  print("X-Request-Id header not found")

if __name__ == "__main__":
  if len(sys.argv) > 1:
    get_request_id(sys.argv[1])
  else:
    print("Usage: ./1-hbtn_header.py <URL>")
