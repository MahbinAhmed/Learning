# *args

# def function(*args):
#     for i in args:
#         print(i)

list = ["Burger","Pizza","Sandwitch","Fry","Bread"]

# function(list)
# function("Burger","Pizza","Sandwitch","Fry","Bread")


# **kwargs

def function(*args,**kwargs): # *args is need before **kwargs in case of use dictionary as a paramater
    for key,value in kwargs.items():
        print(key,value)

    for i in args:
        print(i)


def function2(**kwargs): # only **kwargs is needed if the parameter passed in key-value pair but not in dictionary format
    for key,value in kwargs.items():
        print(key,value)

dict = {"Burger":50,"Pizza":100,"Sandwitch":40,"Fry":90}

# function({"Burger":50,"Pizza":100,"Sandwitch":40,"Fry":90})
function2(Burger=50,Pizza=100,Sandwitch=40,Fry=454)