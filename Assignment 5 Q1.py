# assignment-5
a=input("enter your string:")
x=len(a)
reverse_string=""
i=0
while i<=x:
  reverse_string += a[-(i+1)+x:-i+x]
  i=i+1
print(reverse_string)

