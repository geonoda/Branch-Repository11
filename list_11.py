import random
score = 0
print("start")
def addtest ():
     global score
     a = random .randint (0 , 15 )
     b = random .randint (0 , 15 )
     c = a + b
     print (a , '+', b , '=', end ='')
     ans = int (input ())
     if ans == c :
         score = score + 1
         print ('True')
     else :
         print ('False')
for i in range (5 ):
    addtest ()
print ('your socre is ', score )
print ('terminated')
