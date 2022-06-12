def args_and_kwargs(*args,**kwargs):

    for value in kwargs.items():
        print(value)
    print(args)

list=["Alex","Harry","Jack"]
dict = {"Book":"A bundle of knowladge","Egg":"A kind of food","ICT":"Information and Communication Techonology"}

args_and_kwargs(*list,**dict)