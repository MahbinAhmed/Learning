# Requests Module

import requests

url = "https://api.github.com/events"

# gr = requests.get(url)
# # print(gr.text)
# print(gr.status_code)

# dr = requests.delete(url)
# # print(dr.status_code)
# # print(dr.text)

# hr = requests.head(url)
# # print(hr.headers)
# # print(hr.text)
# # print(hr.status_code)

# # par = requests.patch()

# # por = requests.post(url,data)
# # print(pr.text)
# # print(pr.status_code)

# # pur = requests.put(url)
# # print(pur.text)
# # print(pur.status_code)

# rr = requests.request(url)

# From Edureka

# payload = {"key1":"value1"}
# res = requests.get("https://httpbin.org/get",params=payload)
# # print(res.text)
# print(res.url)

# payload = {"key1":"value1"}
# po_res = requests.post("https://httpbin.org/post", data=payload)
# # print(res.text)
# print(po_res.text)

# req = requests.get("https://httpbin.org/get")
# print(req.json())

# cookies = dict(key1 = "value1")
# co_req = requests.get("https://httpbin.org/cookies", cookies=cookies)
# print(co_req.text)

# he_req = requests.get("https://httpbin.org/headers")
# print(he_req.headers)

s = requests.session()
s.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
r = s.get("https://httpbin.org/cookies")
print(r.text)