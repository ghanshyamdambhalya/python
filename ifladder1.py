# write a program to accept user body temperature in farenheit and if is is above 100.2 then display message you have high grade fever and if not display you are normal 
temperature = float(input("Enter the value of body temperature"))
if temperature > 100.2:
    print("You have a high grade fever")
else:
    print("You are normal")