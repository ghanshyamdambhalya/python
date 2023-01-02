# Example of function 
# Write a programe to create a function which returns a sqaure of give number 
def getSqaure(number):
     answer=number*number
     # print("your answer is ",answer)
     return answer

number=int(input("Enter value of number "))
result=getSqaure(number)
print("the value of result is ",result)