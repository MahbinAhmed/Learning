# Coding section

class Employee:
    company_working_hour = 10
    pass

rohan = Employee()
harry = Employee()

rohan.name = "Rohan"
rohan.post = "Admin"
rohan.salary = 5000

harry.name = "Harry"
harry.salary = 6000
harry.post = "CEO"
harry.company_working_hour = 8

# Print Section

# print(rohan.name)
# print(harry.company_type)

print(harry.company_working_hour)
harry.company_working_hour = 7
print(harry.company_working_hour)
print(Employee.company_working_hour)
Employee.company_working_hour = 9
print(Employee.company_working_hour)
print(Employee.__dict__)
print(rohan.__dict__)
print(harry.__dict__)