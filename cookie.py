import requests
  
r = requests.get('http://google.com')
  
for c in r.cookies:
    print(c.name +"==>>", c.value)

f = open("cookies.txt", "a")
f.write(f"{c.value}\n")
f.close()
