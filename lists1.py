company1 = ['hp','dell','lenovo','asus','acer'] # list start with 0 and end with total-1
dealer1 = ['techno','anant','ram','fakhri']
print(company1) #it prints complete list we defined
print(dealer1) #it prints complete list we defined 
company1.append('mi')
print(company1)
company1.extend(dealer1)
print(company1)
company1.insert(3,'compact')
print(company1)
company1.remove('fakhri')
print(company1)
temp=company1.pop(6)
print(company1)
print(temp)
#dealer1.clear()
#dealer1.sort()
#print(dealer1)
dealer1.reverse()
print(dealer1)
temp=dealer1.copy()
print(temp)

