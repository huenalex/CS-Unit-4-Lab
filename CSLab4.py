#Lab 4
#Alex Huen
#Project Euler Problems


#Problem 1
#create an empty list to house all the multiples
list = []
#the following for statement returns all values divisible by 3 or 5
for x in range (0, 1000):
    if x%3==0 or x%5==0:
        #adds all the values to the list
        list.append(x)
answer = sum(list)
print(list)
print(answer)

#Problem 2
#these first 2 values must be given in order to do this problem
n1 = 0
n2 = 1
#add the first 2 values to the list
fibList = [n1, n2]
#the following creates the next number in the sequence through a while loop
while True:
    new_n = n1 + n2

    n1 = n2
    n2 = new_n
    #adds to the list
    fibList.append(new_n)
    #while loop is broken when the newest number exceeds 4 million
    if new_n >= 40000000: break
#the answer adds all of the numbers in the sequence
answer = sum(fibList)
print(answer)

#Problem 3
'''
The code below is a brute force algorithm. Since the value is too large, it takes too long to work
facList = []
x = 600851475143
for i in range(1, x+1):
    if x%i==0:
        facList.append(i)
answer = sum(facList)
print(answer)
'''
