# find the sum of all the multiples of 3 or 5 below 1000

from unittest import result


def find(): 
    print("find the sum of all the multiples of 3 or 5 below X \n X=")
    num= input()
    sum = 0
    for i in range(int(num)):
        if (i % 3 == 0) or (i % 5 == 0): 
            sum += i
    return sum


#sum pair nums in fibonacci sequence under 4M
def findSumFibonacci():
    sum = 0
    num1, num2 = 0, 1
    while num2 < 4000000: 
        aux = num1
        num1 = num2
        num2 += aux
        if (num1 % 2 == 0):
            sum += num1 
    return sum
    
# larges prime factor of num
def largestPrimeFactorX(num):
    number = num
    primeFactor = 1
    i = 2
    while i <= number: 
        if number % i == 0: 
            primeFactor = i 
            number = number / i
        else: 
            i+= 1
    return primeFactor    
     
#larges palindrome product in 3 digit num
def isPal(num):
    numStr = str(num)
    for i in range(0, int(len(numStr) / 2 + 1)):
        if (numStr[i] != numStr[-i -1]):
            return False
    return True

def largestPalindrome(num1, num2):
    maxProduct = 0
    for i in range(num1, 99, -1):
       for j in range(num2, 99, -1):
           aux = int(j * i)
           if isPal(aux) and aux > maxProduct:
               maxProduct = aux
    return maxProduct              
       
           
    

# print("find the sum of all the multiples result: " + str(find()))
# print("result fibonacci:" + str(findSumFibonacci()))
#print("larges prime factor of num: " + str(largestPrimeFactorX(600851475143))) #600851475143
print("larges palindrome: " + str(largestPalindrome(999, 999))) 