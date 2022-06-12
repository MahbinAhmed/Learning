import datetime
getdateandtime=datetime.datetime.now()
getonlydate=datetime.date.today()
getonlytime=datetime.time.min

print(getdateandtime)
print(getonlydate)
print(getonlytime ,"\n")

import random
list=["Rahim","karim","Moga","Doga"]
getrandomnumer=random.randint(1,100)
getrandomchoice=random.choice(list)

print(getrandomnumer)
print(getrandomchoice)