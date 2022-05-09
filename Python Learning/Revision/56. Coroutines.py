# Coroutines

import time

def coroutine():
    time.sleep(3)
    text = "Hey guys! Welcome to Parallax Coders. How are you ? Have a great day"

    while True:
        checking_text = (yield)
        if checking_text in text:
            print("Your word has been found !")
        else :
            print("Your book has not been found !")

searcher = coroutine()
print("Initializing function...")
searcher.__next__()
searcher.send("guys")
print("Sent !")
searcher.send("Parallax Coders")
print("Sent again !")
searcher.send("How")
print("Again sent !")
searcher.close()
