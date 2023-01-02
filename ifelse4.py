#  Write a Python program to calculate final electricity bill based upon below given criteria. take monthly electricity unit from user as input. 

# units           price  per unit 
# <100            1
# >100 & <200     2 
# >200 & <300     3
# >300 & <400     4
# >400            5

unit=int(input("Enter value of unit "))

if unit<=100:
     answer=unit*1
elif unit>=100 and unit<200:
     answer=unit*2
elif unit>=200 and unit<300:
     answer=unit*3
elif unit>=300 and unit<400:
     answer=unit*4
else:
     answer=unit*5

print("your final amount is ",answer)