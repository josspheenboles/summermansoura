class Trainee:
    #class var
    count=0
    #constructor
    def __init__(self,nationanum,track,level):
        #instance var
        self.nationalnum=nationanum
        self.track=track
        self.setlevel(level)
        Trainee.count+=1
    #instance method
    def setlevel(self,newlevel):
        if(newlevel==2 or newlevel==3):
            self.__level=newlevel
        else:
            print('cant set level must be 2 or 3')

    def getlevel(self):
        return  self.__level
    def doex(self):
        print('exer. done')
    def attend(self):
        print('you attend')
    #class method
    @classmethod
    def gettraineecont(cls):
        return Trainee.count