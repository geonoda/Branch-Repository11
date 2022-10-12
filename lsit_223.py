import random
print("start")
def multiply (a , b ):
     s = 0
     if (b <0 ):
         for i in range (-b ):
             s = s - a
     else :
         for i in range (b ):
             s = s + a
     return s
a = random .randint (-9 , 9 )
b = random .randint (-9 , 9 )
s = multiply (a , b )
print (a , 'x', b ,'=', s )
print("finish")

