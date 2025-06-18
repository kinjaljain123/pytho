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