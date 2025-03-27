#H.mclachlin
#March 27th, 2025
#lists
#program displays average of randome 0 - 100 numbers
import random 
numbers=[]
for index in range(1,100):
    num=random.randint(0,100)
    print(num)
    numbers.append(num)
average=(sum(numbers)/100)
print("the average of the random numbers is", average)