# find the sum of all the multiples of 3 or 5 below 1000

def find(num): 
    sum = 0
    for i in range(num):
        if (i % 3 == 0) or (i % 5 == 0): 
            sum += i
    return sum



print("find the sum of all the multiples of 3 or 5 below X \n X=")
userNum = input()
print(find(int(userNum)))