def searcher():
    import time
    # This is time consuming task
    book = "Welcome to parallax coders. Hello world"
    time.sleep(3)

    while True:
        txt = (yield )
        if txt in book:
            print("Word found")
        else:
            print("Word not found")


search = searcher()
# next(search)
search.__next__()
search.send("Welcome")
print("Again sending")
search.send("Hey Guys")
print("Again sending")
search.send("parallax coders")
print("Again sending")
search.send("Hello World")
search.close()
# search.send("Hello")
# print(type(searcher))