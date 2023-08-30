class Animal:
    pass
class Wild:
    def __init__(self):
        print('wild constr')
class Lion(Animal,Wild):
  pass

l=Lion()
"""#inheritance
#employee is a human
#parent
class Human:
    def __init__(self,id ,name):
        if(id>0):
            self.__id=id
        else:
            print('id >0')
        #attribute,instance var
        self.name=name
    #property
    '''
    @id.setter
    
    def id(self,newid):
        if(newid!=0):
            self.__id=newid
        else:
            print('id must > 0')
    @property
    def id(self):
        return  self.__id
    
    def getif(self):
        return self.__id
    def setid(self,newid):
        if (newid != 0):
            self.__id = newid
        else:
            print('id must > 0')
    '''

    def eat(self):
        print('eat')

    def drink(self):
        print('drink')

    def sleep(self):
        print('sleep')
    def speek(self):
        print('iam',self.name)
    def __str__(self):
        return f"My name: {self.name}        My ID: {self.__id}"
    def __len__(self):
        return len(self.name)
#child
class Employee(Human):
    #overide

    def speek(self):
        print('iam ',self.name,"\n my salary:",self.salary)

    def __init__(self,id,name,salary):
        #invoke human constr and pass to it id,name
        super(Employee,self).__init__(id,name)
        self.salary=salary

    def attend(self):
        print('attend')
    def absent(self):
        print('absent')
    def evaluation(self):
        print('evaluation')
    def __str__(self):
        #super(Employee,self).__str__()#id ,name
        return  'My Salary'+str(self.salary)#salary

h=Human(1,'aya')
print(h)
e=Employee(10,"ali",5000)
print(e)

print(len(h))
"""
'''
#public modifier --->parent class,child class
# -->can accessed b object from child
#private modifier --->parent class--->accessd inside parent class only
#private modifer --->child class--->accessd inside child class only
#portected modifier--->patent class --->accessed inside parent and child
e=Employee(1,'aya',8000)
e.name='plpl'
print(e.name)
e.id=10
print(e.id)

e.getif()
e.setid(10)
'''

