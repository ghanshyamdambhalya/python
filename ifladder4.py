'''Write a Python program to calculate income tax, gross income, net income from monthly income given by user 

yearly income     tax rate
<3,00,000         5%  

>=3,00,000
<5,00,000         10%  

>=5,00,000
<8,00,000         20%

>=8,00,000        30%  '''
incomem=int(input("Enter the monthly income in rupees"))
incomey=incomem*12
tax1= incomey%5
print ("total salary in a year", incomey)
if incomey <300000:
    print("total incometax", tax1)
elif incomey >= 300000 and incomey < 500000:
    print("total incoemtax", tax1)
print("good bye");
'''tax2=incomey%10
tax3= incomey%20
tax4= incomey%30
if incomey < 300000:'''
#  print("Total incometax", tax1)
#print("good bye");
'''elif incimey >= 300000: and incomey < 500000:
    print(Total income tax, tax2)
elif incomey >= 500000 and incomey <800000:
    print(Total Income tax, tax3)
elif incomey >= 800000:
    print(Total income tax, tax4)'''