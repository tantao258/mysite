import requests

method = "get"
url = "http://182.61.21.98/login/"
data = {
    "username": "tantao258",
    "password": "910806"

}
if method == "GET":
    obj = requests.get(url=url)
elif method == "POST":
    obj = requests.post(url=url, data=data)