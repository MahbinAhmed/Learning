import requests
# data = {"Hello":5}
# r = requests.get("https://api.github.com/users/naveenkrnl", )
# print(r.text)
# print(r.content)
# print(r.url)
# print(r.status_code)
# print(r.elapsed)
# print(r.iter_content())
# print(r.json())
# print(r.links)

# From Corey Schafer----->>>>>

# Image Downloading
# r = requests.get("https://imgs.xkcd.com/comics/python.png")
# # print(r.content)
# with open("downloaded.png","wb") as f:
#     f.write(r.content)

# payload = {"Hello":5, "Hi":6}
# r = requests.get("https://httpbin.org/get", params=payload)
# print(r.headers)

# payload = {"Hello":5, "Hi":6}
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.url)

r = requests.get("https://httpbin.org/basic-auth/hello/heythere", auth=("hello","heythere"))
print(r.text)