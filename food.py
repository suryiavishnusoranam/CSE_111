import random
import math
import datetime
# x = round(pow(17,9)/3)-6
# y = False
# if x % 2 == 0:
    #y = True
    #print(x,y)

#def random_math():
    #print(math.ceil(math.pow(17,9) / 3) - 6)
    #return(math.ceil(math.pow(17,9) / 3) - 6) % 2 == 0 # acts like if statement
#print(random_math())

#myList = []
#iterator = 0
#while len(myList) < 100:
 #   myList.append(random.randint(0,1000))
#myList.sort(reverse=True)
#print(myList)

now = datetime.now()
display_message = "even minute"
if (now.minute % 2 > 0):
    display_message = "odd minute"
print(display_message)

