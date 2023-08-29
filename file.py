class employee:
    def __init__(self, empID, name, age, salary):
        self.empID = empID
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"{self.empID} {self.name} {self.age} {self.salary}"

class employeeTable:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def search_by_age(self, age):
        result = []
        for employee in self.employees:
            if employee.age == age:
                result.append(employee)
        return result
    def search_by_name(self, name):
        result = []
        for employee in self.employees:
            if employee.name == name:
                result.append(employee)
        return result
    def search_by_salary(self, salary, operator):
        result = []
        if operator == ">":
            for employee in self.employees:
                if employee.salary > salary:
                    result.append(employee)
        elif operator == "<":
            for employee in self.employees:
                if employee.salary < salary:
                    result.append(employee)
        elif operator == ">=":
            for employee in self.employees:
                if employee.salary >= salary:
                    result.append(employee)
        else:
            for employee in self.employees:
                if employee.salary <= salary:
                    result.append(employee)
        
        return result
                
employee_Table = employeeTable()
employee_Table.add_employee(employee("161E90", "Raman", 41, 56000))
employee_Table.add_employee(employee("161F91", "Himadri", 38, 67500))
employee_Table.add_employee(employee("161F99", "Jaya", 51, 82100))
employee_Table.add_employee(employee("171E20", "Tejas", 30, 55000))
employee_Table.add_employee(employee("171G30", "Ajay", 45, 44000))

result = []
searchVar = input("search employee by name(1) or age(2) or salary(3)\n")
if searchVar == "1":
    name = input("Enter the name\n")
    result = employee_Table.search_by_name(name)
if searchVar == "2":
    age = input("Enter the age\n")
    result = employee_Table.search_by_age(age)
if searchVar == "3":
    salary = int(input("enter the salary\n"))
    operator = input("enter the operator like >, >=, <, <=\n")
    result = employee_Table.search_by_salary(salary, operator)

for employee in result:
    print(employee)


        