# My projects during learning

projects_list=["Simple dictionary","Calculator and Faulty calculator","Guess the number","Astrologer's star","Health management system","Rock,paper,Scissor","Upcoming..."]

print("=====Welcome to project house=====\n")
first_input=int(input("Press 1 for projects name list or press 2 for project : "))
if first_input==1:
    for index,item in enumerate(projects_list):
        print(index,item)
elif first_input==2:
    projects_choice=int(input("Enter serial number of the project that you want to use: "))

# Project no. 1
print("-----Welcome to Dictionary-----")
if projects_choice==1:
    project1_dictionary={"Food":"Which give us energy for work","Book":"It used to study and it gives knowledge about something","Computer":"A digital device","Python":"Programming"}
    input_for_dictionary=input("Enter your word : ")
    print(project1_dictionary.get(input_for_dictionary))

#Project no. 2
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
if projects_choice==2:
    calculator_type_choice=int(input("Enter 1 for Normal calculator | Enter 2 for Faulty Calculator : "))
    if calculator_type_choice==1:
        print("-----Welcome to Normal Calculator-----")
        calculator_first_input=int(input("Enter first number : "))
        calculator_operator_input=input("Enter one of these : +, - *, / \n")
        calculator_second_input=int(input("Enter second number : "))

        if (calculator_operator_input=="+"):
            adding=add(calculator_first_input,calculator_second_input)
        print("Your answer is ",adding)
        elif (calculator_operator_input=="-"):
            substitution=minus(calculator_first_input,calculator_second_input)
        print("Your answer is ",substitution)
        elif (calculator_operator_input=="*"):
            multiplicationing= multiplication(calculator_first_input,calculator_second_input)
        print("Your answer is ",multiplicationing))
        elif (calculator_operator_input=="/"):
            divisioning= division(calculator_first_input,calculator_second_input)
        print("Your answer is ",divisioning)

