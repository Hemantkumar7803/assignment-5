# assignment-5
a=float(input("enter your first side:"))
b=float(input("enter your second side:"))
c=float(input("enter your third side:"))
if a+b>c and b+c>a and a+c>b:
   s= (a+b+c)/2
   area =(s*(s-a)*(s-b)*(s-c))**0.5
   print(area)
else :
  print("triangle does not exist")

