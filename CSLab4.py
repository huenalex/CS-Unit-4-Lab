#Lab 4
#Alex Huen
#Project Euler Problems
'''
#Problem 1 (done)
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

#Problem 2 (done)
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
'''
'''
#Problem 3 (done)
'''
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


#Problem 4 (done)
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
'''
#Problem 5 (not finished)
#gcd is greatest common denominator
def gcd(x,y):
    if x>y:
        smallerV = y
    else:
        smallerV = x
        for i in range()
def lcm():
    answer = 1
    for i in range(1,n+1):



'''
#Problem 6 (done)
#the following 3 are just placeholder values
SumOfSquare = 0
SquareOfSum = 0
Sum = 0
#the for loop calculates the values so that we can use it to generate our answer later
for i in range(1,101):
    SumOfSquare = SumOfSquare + i**2
for i in range(1,101):
    Sum = Sum + i
SquareOfSum = Sum**2
#we do the calculations in the "print" command, which is the difference of the 2 values
print(SquareOfSum - SumOfSquare)

#Problem 7 (not finished)

primeNumList = []
primeNumList.append(2)
while len(primeNumList) <10001:
    for i in range(2,10001,2):

'''
'''
#Problem 8 (done)
#the series of numbers for the problem
NumSeries = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
#amount of numbers we want to multiply
length = 13
#placeholder value for the final answer
Answer = 0
#the for look runs through the entire code
for i in range(0, len(NumSeries) - length +1):
    #placeholder for the values caluclated in the for loop
    tempAnswer = 1
    #for loop from i to 14 places after
    for x in range(i, i + length):
        #set the temp answer to the numbers the come after itself
        tempAnswer = tempAnswer * int(NumSeries[x:x + 1])
    #just set the final answer to the newest value if turns out to be larger than the initial "largest" number
    if Answer < tempAnswer:
        Answer = tempAnswer
print(Answer)
'''
'''
#Problem 9 (done)
#we start of with 3 since that is the min value for a pythag. thriple
for a in range(3, 1000):
    for b in range(a + 1, 1000):
        #(ALTERNATE)cSquared = a**2 + b**2
        #(ALTERNATE)c = cSquared**0.5
        #calculate the c value
        c = (a**2 + b**2)**0.5
        if a + b + c == 1000:
            Answer = a * b * c
print(Answer)
'''
#PRoblem 10
#need help with prime numbers

#problem 11
