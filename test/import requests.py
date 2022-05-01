import requests
import base64

a = "PotatoEarlyBlight1.jpg"
with open(a, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

url = "http://10.0.0.59:8080"

#r = requests.post(url,json={"image":encoded_string})
print(encoded_string)