import requests

url = "https://maps.googleapis.com/maps/api/distancematrix/json"

querystring = {"origins":"-12.0604755,-76.9434953","destinations":"-12.0680735,-76.9404941","key":"AIzaSyDJQZgcTpQWmM9zwUn5RDIvrbm73opKpoU"}

response = requests.request("GET", url, params=querystring)

print(response.text)
