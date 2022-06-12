import requests
r = requests.get("https://www.youtube.com/watch?v=u6_aYV-1LAE&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=82")
# print(r.text)
print(r.status_code)

url = "https://www.youtube.com/watch?v=u6_aYV-1LAE&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=82"
data = {
    "p1":1,
    "p2":2
}

r2 = requests.post(url= url, data = data)