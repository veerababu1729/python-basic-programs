#guessing game with a computer
a=int(input("guess the number from 1 to 10 which will be created by computer:"))
import random
b=(random.randint(1,11))
print("random number created by computer is :",b)
if(a==b):
 print("your guess is correct")
else:
 print("your guess is wrong better luck next time")
             
               
