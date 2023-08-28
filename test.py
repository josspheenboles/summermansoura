from psycopg2 import *
#connection
conn=connect(
    host='localhost',
    user='postgres',
    password='123456',
    database='iti'
)
conn.autocommit=True
#update query
#query="update empaloyee set name='ahmed mohamed' where id=2"
query="insert into empaloyee (name) values('hala')"
cur=conn.cursor()
#execuate
cur.execute(query)
#conn.commit()
cur.execute('delete  from empaloyee')
cur.execute('select * from empaloyee')
res=cur.fetchall()
print(res)
#close
conn.close()
'''
#establish connection

#host ,username,password,db,port
conn= connect(host='localhost',
              user='postgres',password='123456',port=5432,database='iti')
#cusror
curs=conn.cursor()
#run query
curs.execute('select  * from empaloyee');
res=curs.fetchone()
print(res)
#close connection
conn.close()

import sys
try:
    n1=input('enter n1')
    n2=input('enter n2')
    print(float(n1)+float(n2))#valueerror
    print(float(n1)/float(n2))#zerodivison
except ValueError:
    print('el rakam lazem be digits')
except ZeroDivisionError:
    print('mesh divie by zero')
except: #general 
    print(sys.exc_info()[1])
else:#only if try done correct
    print('done try')
finally:#even try,except
    print('thnxx')



n1=input('enter n1')
n2=input('enter n2')
print(float(n1)+float(n2))

#syntax error
#print('dfdffd)

#open file
f=open('asd2.txt','a')
f.write('\ntest')
f.writelines(['a','s','d'])
#close file
f.close()

#open file
f=open('asd.txt','r+')
f.write('line1\n')
f.write('line2')
f.write("""
        line3
        line4""")
l=["\nline5\n","line6"]
f.writelines(l)
f.seek(2)
print(f.read())
#close fiel
f.close()
"""
#open file
#w --->if file exsist--->i will clear
#a --->if file exsist--->i will append 
f=open('asd.txt','r')
for x in f:
    print(x)
#print(f.read(2))
#print('==',f.read(),'===')
#s=f.readlines()
#print(s[1])
#for line in s:
#    print(line)

print(f.readline())
print(f.readline())
print(f.readline())
print('-',f.readline(),'-')
#print(type(s),s)
"""
#close file
f.close()

from re import *
#define string your search for
regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
str1=input('enter email')
if(fullmatch(regex,str1) is not None):
    print('correct email')
else:
    print('invalid email')
print(match(regex,str1)) #compare must with email
print(fullmatch(regex,str1))#compare string is email
print(search(regex,str1))
print(findall(regex,str1))

#import os
from os import *
#get current user
print(getlogin())
#os name--->linux,windows--->nt
print(name)
#command run -->cmd(windows),terminal(linux)
print(system("dir"))
chdir("c:\\")
print(system("dir"))

#import blockofcode,modulename
from pkg import module1
print('summer python track')
'''
