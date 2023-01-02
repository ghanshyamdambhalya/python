# Write a programe to findout which number is smaller outof given 3 number 
num1=float(input("Enter value of number 1 "))
num2=float(input("Enter value of number 2 "))
num3=float(input("Enter value of number 3 "))

if num1 < num2 and num1 < num3:
     print("num1 is smaller ")
elif num2<num1 and num2<num3:
     print("num2 is smaller ")
elif num3<num1 and num3<num2:
     print("num3 is smaller ")
     