#defination
#var,function,class
#class Classname
#define class
class Employee:
    #class variable
    #shared all objects
    count=0#1-->2--->3
    #declare inside class
    #result not affect depend on callable object
    @staticmethod
    def add(employee1,employee2):
        return employee1.__salary+employee2.__salary
    #reserved name to constructor
    def __init__(self,id,name,salary):
        #constructor
        #instance variable
        #public access inside class & using object
        self.id=id
        self.name=name
        #private access inside class only
        self.__salary=salary
        #classname.classvariablename
        Employee.count+=1
        print('iam employee constructor')

    #instance method
    def setsalaey(self,newsalary):
        if(newsalary>=3000 and newsalary<=8000):
            self.__salary=newsalary
        else:
            if(newsalary<3000):
                self.__salary=3000
            elif (newsalary>8000):
                self.__salary=8000
    def getsalary(self):
        return  self.__salary

    def attend(self):
        print(self)
        print('you attended')

    @classmethod
    def employeecount(cls):
        return  Employee.count