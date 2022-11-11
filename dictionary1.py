employee = {'name':'ghanshyam dambhalya','age':38,'weight':81, 'education':'mechanical', 'department':'it','employee code':85}
print(employee['name'])
print(employee['education'])
print(employee)
employee['name']='sunil patel'
print(employee)
temp=employee.items()
print(temp)
temp=employee.keys()
print(temp)
temp=employee.values()
employee.update({'employement type':'permenant'})
print(employee )