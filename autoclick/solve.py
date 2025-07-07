import requests

url = "http://localhost:32768"

s = requests.Session()
r = s.get(url)
print(r.text)
for i in range(1010):
  s.cookies['time'] = "1717"
  r = s.get(url + "/clicked", headers={"User-Agent":"nice_browser"})
  print(r.text)

#