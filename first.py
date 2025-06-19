''' 4. Write a Python program to find the sum of all odd
 numbers between two given numbers. 
     Start = 1, stop = 10
     Sum of odd numbers: 25
     '''


i = 1
sum=0
while i<11 :
    sum +=i
    i+=2

print("sum is :",sum)

'''  
 number using a for loop.
 6. Write a Python program to check if a given number
 is a perfect number. 

  '''
num = int ( input (" enter the number"))
total = 0
for i in range (1,num):
    if num % i==0:
        total+=1

    
if total == num:
    print("Yes")
else:
    print("No")    


"""7. Write a Python program to check if a string is an
 anagram of another string."""

a = input("Enter first string: ")
b = input("Enter second string: ")

if sorted(a) == sorted(b):
    print("True")
else:
    print("False")



   
""" Write a Python program to calculate the LCM (Least
 Common Multiple) of two numbers."""

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    big = x
else:
    big = y

while True:
    if big % x == 0 and big % y == 0:
        print("LCM is:", big)
        break
    big += 1
    

    
"""Write a Python program to count the frequency of
 each element in a list."""

lst = [1, 2, 3, 2, 4, 1, 2, 4, 5]
freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)



""" 10. Write a Python program to reverse the order of
 words in a given sentence."""

s = input("Enter a sentence: ")
words = s.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print(result)





"""11. Write a Python program to calculate the sum of
 digits of a given number until the sum becomes a
 single-digit number."""

num = int(input("Enter a number: "))

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

while num > 9:
    num = sum_digits(num)

print("Final Output:", num)




"""12. Write a Python program to reverse a number using
 a while loop."""

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reversed number is:", rev) 