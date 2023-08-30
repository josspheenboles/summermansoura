class Wall:
    def __init__(self,width,height):
        self.width=width
        self.height=height

class Marker:
    def __init__(self,color,type):
        self.color=color
        self.type=type
class Instructor:
    def __init__(self,_id,_name):
        self.id=_id
        self.name=_name

    def writonboard(self,marker1):
        print(marker1)

class Room:

    def __init__(self,number,traineecount,walls):
        self.number=number
        self.traineecount=traineecount
        #composition realtion
        #object of room must cosist of 4 walls
        self.walls=walls
    def instructorenter(self,instru):
        print(instru)
ins=Instructor(1,"aya")
markerobj=Marker('black','perm.')
wallsl=Wall(10,10)
wallsr=Wall(10,10)
wallsf=Wall(10,10)
wallsb=Wall(10,10)

roomobj=Room(1,15,[wallsr,wallsl,wallsf,wallsb])
#association relation
#object use another object
#for short time
ins.writonboard(markerobj)
#aggergation relation
#object use another object
#for long time than association
roomobj.instructorenter(ins)