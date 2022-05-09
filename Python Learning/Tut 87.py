# Regular expressions - Findall,search,split,sub,finditer
# a = "Hello world"
#
# b = a.find("w")
# print(b)
import re

text = '''Tata Limited
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
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

text2 = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
'''

# a = re.search("Landsman",text)
# print(a)
# a = re.split("director",text)
# print(a[0])
# a = re.sub("executive","producer",text2)
# print(a)
# a = re.findall("North",text)
# print(a)

# a = re.compile("^Tata")
# b = a.finditer(text)
# for c in b:
#     print(c)

# Meta Charecters

# a = re.finditer(r".avid",text)
# a = re.finditer(r"^Tata",text)
# a = re.finditer(r"iii$",text)
# a = re.finditer(r"ai{2}",text)
# a = re.finditer(r"ai*",text)
# a = re.finditer(r"ai+",text)
# a = re.finditer(r"ai{5}",text)
# a = re.finditer(r"ai{5}|^Tata",text)
# a = re.finditer(r"ai{5}|^Tata",text)

# Sqecial Sequences

# a = re.finditer("r\ATata",text)
# a = re.finditer(r"\bFax",text)
# a = re.finditer(r"\Bata",text)
# a = re.finditer(r"\d{5}",text)
# a = re.finditer(r"\D{5}",text)
# a = re.finditer(r"\s",text)
# a = re.finditer(r"\S",text)
# a = re.finditer(r"\w",text)
# a = re.finditer(r"\W",text)
# a = re.finditer(r"iiii\Z",text)
#
#
# for b in a:
#     print(b)

# print(text[494:497])


# Task

task = re.finditer(r"\B[+]44 ",text)

for answer in task:
    print(answer)
