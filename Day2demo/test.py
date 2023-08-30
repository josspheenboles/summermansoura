


'''
#def add(int x,int y)
#def add(float x,float y)
def add(datatype,*args):
    res=0
    if(datatype=='int' or datatype=='float'):
        for x in args:
            res+=x
        return  res
    elif(datatype=='str'):
        for x in args:
            res+=','+x
        return  res
#calling function with
#different daatype
#different count of param
add('int',1,2,3,4,5,7,8)
add('str','2','3','4')
add('float',1.1,2.3,4.7,5.4,5.6)
'''