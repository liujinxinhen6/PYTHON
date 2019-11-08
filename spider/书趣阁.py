import requests

response = requests.get('')
response.encoding = response.apparent_encoding
print(response.text)