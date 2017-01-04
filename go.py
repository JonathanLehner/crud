import requests, time
r = requests.post('http://requestbin.fullcontact.com/wv5tvowv', data={"ts":time.time()})
print(r.status_code)
print(r.content)