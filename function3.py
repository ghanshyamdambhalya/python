# Write a to make a clac using functions
def addition(a,b):
     answer=a+b
     print("your answer is ",answer)
def subtraction(a,b):
     answer=a-b
     print("your answer is ",answer)
def multiplication(a,b):
     answer=a*b
     print("your answer is ",answer)
def divison(a,b):
     answer=a/b
     print("your answer is ",answer)
def modlus(a,b):
     answer=a%b
     print("your answer is ",answer)
def max(a,b):
     if a>b:
          print("num1 is greater ")
     elif b>a:
          print("num2 is greater ")
def min(a,b):
     if a<b:
          print("num1 is smaller ")
     elif b<a:
          print("num2 is smaller ")
def eqaulity(a,b):
     if a==b:
          print("both are same ")
     else :
          print("both are not same ")
num1=int(input("Enter value of num1 "))
num2=int(input("Enter value of num2 "))
print("""Enter 1 for addition 
Enter 2 for subtraction
Enter 3 for multiplication 
Enter 4 for divison
Enter 5 for modlus 
Enter 6 for max
Enter 7 for min
Enter 8 for eqaulity """)
option=int(input("Select any one option "))

if option==1:
     # addition
     addition(num1,num2)
     print()
elif option==2:
     # subtraction
     subtraction(num1,num2)
     print()
elif option==3:
     # multiplication
     multiplication(num1,num2)
     print()
elif option==4:
     # divison
     divison(num1,num2)
     print()
elif option==5:
     # modlus
     modlus(num1,num2)
     print()
elif option==6:
     # max
     max(num1,num2)
     print()
elif option==7:
     # min
     min(num1,num2)
     print()
elif option==8:
     # eqaulity
     eqaulity(num1,num2)
     print()