# Regular Expression Module

import re

text = """Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii
"""

# if re.search("VA",text):
#     print("Found")

# founder = re.findall("Tata",text)

# for i in founder:
#     print(i)

# founder = re.finditer("Tata",text)

# for i in founder:
#     print(i)

text2 = "sat, hat, mat, pat"

# founder = re.findall(r"[shmp]at", text2)

# for i in founder:
#     print(i)

# founder = re.findall(r"[h-m]at", text2)
# for i in founder:
#     print(i)

# replacer = re.compile(r"[p]at")

# replaced = replacer.sub("bat",text2)
# print(replaced)

# spliter = re.search("lekin",text)
# spliter = re.search("\s",text)
# print(spliter.span())
# print(spliter.string)
# print(spliter.group())

# tester = re.compile(r"fass")
# tester = re.compile(r".ta")
# tester = re.compile(r"^Tata")
# tester = re.compile(r"iii$")
# tester = re.compile(r"Ta*")
# tester = re.compile(r"Ta+")
# tester = re.compile(r"(Ta){1}")
# tester = re.compile(r"(Ta){1}|Tata.")

# tester = re.compile(r"\ATata")
# tester = re.compile(r"\bView")
# tester = re.compile(r"\Bap")
# tester = re.compile(r"\d")
# tester = re.compile(r"\D")
# tester = re.compile(r"\s")
# tester = re.compile(r"\S")
# tester = re.compile(r"\w")
# tester = re.compile(r"\W")
# tester = re.compile(r"i\Z")
# tester = re.compile(r"\b[a-c]")
tester = re.compile(r"\d{3}-\d{4}")
test = tester.finditer(text)
for te in test:
    print(te)