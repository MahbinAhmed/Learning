import re

txt = "The rain in Spain"
r = re.search("ain",txt)
# r = re.findall("\W",txt)
# r = re.split("ai",txt,1)
# r = re.sub("ai","ui",txt,1)
print(r.span())
print(r.group())
print(r.string)