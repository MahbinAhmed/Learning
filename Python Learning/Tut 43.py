import time
the_time = time.time()
print(the_time)
for i in range(100):
    print("Hello World")
the_time2=time.time()
print(the_time2)
tell_localtime=time.asctime(time.localtime(time.time()))
print(tell_localtime)