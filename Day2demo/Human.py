class Human:
    def __init__(self,id,name):
        self.id=id
        self.__name=name
        self._protname=name
    def sleep(self):
        print('sleeping')
    def eat(self):
        print('eat')
    def drink(self):
        print('drinking')
    def speek(self):
        print('iam ',self.name)
    def add(self,n1,n2):
        print('human add')
#inheritance is a relation
#object is a object
#employee is a human
#human is not a employee
class Employee(Human):
    def __init__(self,id,name,salary):
        super(Employee,self).__init__(id,name)
        self.salary=salary

    def add(self, n1, n2):
        print('emplyee add')

    def add(self, n1, n2,n3):
        print('emplyee take 3 number')
    def attend(self):
        print('attending')
    def absent(self):
        print('absent')
    def evaluate(self):
        print('evaluation')

    def add(a=None, b=None, c=None):
        pass
    #override
    def speek(self):
        print('iam',self._protname,'\nmy salary:',self.salary)
    
emp=Employee(1,'aya',5000)
emp.speek()
print(emp._protname)
emp.add(1,2,3)