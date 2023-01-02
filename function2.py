# Write a programe to create a function which find's area of triagnle 
def area_triangle(a,b):
     answer=a*b/2;
     return answer
height=int(input("Enter value of height "))
base=int(input("Enter value of base "))
result=int(area_triangle(height, base))
print("the value of result is ",result)