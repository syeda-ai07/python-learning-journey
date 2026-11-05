print("Simple Calculator:")
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter your desired operation"))
if choice==1:
  print("Your Result=",a+b)
elif choice==2:
  print("Your Result=",a-b)
elif choice==3:
  print("Your Result=",a*b)
elif choice==4:
  if b!=0:
    print("Your Result="a/b)
  else:
    print("Cannot divide by 0")
else:
  print("Invalid choice")
