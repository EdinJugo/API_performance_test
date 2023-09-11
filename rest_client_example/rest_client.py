import urllib.request as request
 
url = "http://localhost:6000/student"
 
req = request.Request(url=url)
res = request.urlopen(req)
print(res.read().decode())