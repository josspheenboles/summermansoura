from trainee import Trainee
t1=Trainee(1,'python',2)
t2=Trainee(2,'bi',3)
t1.attend()
t1.doex()
print(t1.getlevel())
print(Trainee.gettraineecont())
'''
from Employee import  Employee
obj1=Employee(100,'aya',5000)
obj2=Employee(100,'mark',4000)
print(Employee.add(obj2,obj1))

obj1.setsalaey(000)
print(obj1.getsalary())
obj1.attend()
e2=Employee(1,'mark',3000)
e2.id=2
e2.setsalaey(0)
print(e2.getsalary())

#create object from employee
#object is instance from class employee
print(Employee.count)
obj1=Employee(100,'aya',5000)
#change class variable using objetc
#remove referance to count class var in this object only
#convert to instance in this object only
obj1.count=10
print(Employee.count)
print(obj1.count)
obj2=Employee(1000,'ali',8000)
print(Employee.count)
print(obj2.count)
obj2.ayakalam=10
print(obj2.ayakalam)



print(Employee.count)
obj2=Employee(1,'mark',5000)
print(Employee.count)
obj3=Employee(2,'ali',9000)
print(Employee.count)

obj1=Employee()#invoke to constructor
obj1.id=100
obj1.name='aya'
obj1.salary=5000
obj2=Employee()
obj2.id=2
obj2.name='mark'
obj2.salary=5000
print('psldpsdl')
#print(type(obj1),obj1)
'''