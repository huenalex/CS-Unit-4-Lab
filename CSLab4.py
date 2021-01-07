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

def LargePrimeFactor(n):
    #set largest prime factor to 0 as a placeholder
    LPF = 0
    #set 1 to 2, which is the smaller possible prime number
    i = 2
    #set up a while loop in which the number n is divided by the current prime number value i
    while i <=n/i:
        #see if the "i" is divisible
        if n%i == 0:
        #set the newest i value as the largest prime factor
            LPF = i
        #divide the number
            n = n/i
        else:
            i = i+1
    #if the potential prime factor doesn't exceed the original number, the set it as the LPF
    if LPF < n:
        LPF = n
    return LPF

print(LargePrimeFactor(600851475143))


#Problem 4
#def PalinddromeProduct(n):
n = 0
#the x value is found by decreasing order from largest 3 digit number to smallest 3 digit number
for x in range(999,100,-1):
    #the same happens for y, but extra steps is taken out by replacing 999 with the x value
    for y in range(x,100,-1):
        #the palindrom number is found by multiplying both numbers
        product = x * y
        #the following checks whether the number tested is actually a palindrome
        if product > n:
            #turns it into a string
            StringProduct = str(x*y)
            #the operation bellow reverses a string
            if StringProduct == StringProduct[::-1]:
                n = x*y
print(n)

#PRoblem 5
