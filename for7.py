# Write a print table of 5
number=int(input("Enter your number "))
divisior=1

while divisior<=10:
    answer=number*divisior
    print(f"{number} x {divisior} = {answer}")
    divisior+=1