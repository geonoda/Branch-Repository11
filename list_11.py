import random
score = 0
def addtest ():
     global score
     a = random .randint (0 , 10 )
     b = random .randint (0 , 10 )
     c = a + b
     print (a , '+', b , '=', end ='')
     ans = int (input ())
     if ans == c :
         score = score + 1
         print ('o')
     else :
         print ('x')
for i in range (3 ):
    addtest ()
print ('your socre is ', score )
print ('terminated')
