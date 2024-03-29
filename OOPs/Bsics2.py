class Employee:
    
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=int(pay)
        self.email=first+"."+last+"@company.com"
        
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay*Employee.raise_amount)
             
emp_1=Employee("Animesh","Kumar","1000")
emp_2=Employee("Mohit","Verma","2000")
# print(emp_1.first,emp_2.last)
# print(emp_1.email)

# print(emp_1.fullname())
# print(Employee.fullname(emp_2))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
print(Employee.__dict__)
