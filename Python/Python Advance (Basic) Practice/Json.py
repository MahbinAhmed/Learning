import json

text = '{"Hi":"Hello","Hey":"There","Name":"Nothing","Boolean":false}'

loaded = json.loads(text)
# print(loaded)

# text = {"Hi":"Hello","Hey":"There","Name":"Nothing","Boolean":False}
# dumped = json.dumps(text)
# print(dumped)

with open("hello.json","r")as f: 
    file_loaded = json.load(f)
    
print(file_loaded)

# with open("hello2.json","w")as f:
#     json.dump(text,f)