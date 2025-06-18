"""If a number is divisible by 3 it should print “SKILLBREW”
 as a string
 If a number is divisible by 5 it should print “BRUDITE” as a
 string
 If a number is divisible by both 3 and 5 it should print
 “BRUDITE - NIRVANA” as a string
 """
a = int(input("enter a number"))
print(a,"here is the input number")  # print funtions
print(f"here is the input number{a}") # formated string pint 
"""if a % 3 == 0:
    if a % 5 == 0:
        print("brudite - nirvana")
        else
         print("skillbrew ")
if a % 5 == 0:
    if a % 3 == 0:
        print("brudite - nirvana")
        else
        print("brudite") 
    """
if a % 3 == 0 and a % 5 ==0 :
   print ("brudite - nirvana")
elif a % 3 ==0:
  print("skillbrew")
elif a % 5 ==0:
  print("brudite")




  """ 2. Write a program that accepts a string as input from
 the user and calculates the number of digits and
 letters.
     Input: Hello123 
     Output: Alphabets: 5 & Number : 3
     """
  

  alpha = 0
  num = 0
  for i in list("Brudite"):
    if i.isalpha():
      alpha += 1
    else:
      num += 1

print(f"total alphabets: {alpha}")
print(f"total nums: {num}")

"""Write a Python program to find the factorial of a
 number using a for loop.
"""
a = 10 
fact = 1
while a>0:
  fact = fact * a
  a-=1

print(fact)




""". Write a Python program to input marks for five
 subjects Physics, Chemistry, Biology, Mathematics,
 and Computer. Calculate the percentage and grade
 according to the following:
 Percentage >= 90% : Grade A
 Percentage >= 80% : Grade B
 Percentage >= 70% : Grade C
 Percentage >= 60% : Grade D
 Percentage >= 50% : Grade E
 Percentage < 40% : Grade F
"""

physics = float(input("enter the number"))
chemistry = float(input("enter the number"))
biology = float(input("enter the number"))
mathematics = float(input("enter the number"))
computer = float(input("enter the number"))

total = physics+ chemistry +biology+ mathematics+ computer
percantage=(total/500)*100
if percantage >=90:
  print("grade A")
elif percantage >=80:
   print("grade B")
elif percantage >=70:
   print("grade C")
elif percantage >=60:
   print("grade D")
elif percantage >=50:
   print("grade E")
elif percantage >=40:
  print("grade F")