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



    