# https://i1.faceprep.in/fp/articles/img/46684 1580817324.png
# Write a programe to print 4 thrid triagnle
count=0
flash=0
temp=0
minus=10
while temp<10:
    count=0
    flash=0
    print("")
    while count<=minus:
        print(" ",end="")
        count+=1
    while flash<temp:
        print("* ",end='')
        flash+=1
    temp+=1
    minus-=1
        
# while count<5:
#     print(" ",end="")
#     count+=1
# print("*",end="")
# print("")
# count=0
# while count<4:
#     print(" ",end="")
#     count+=1
# while flash<2:
#     print("* ",end='')
#     flash+=1
# print("")
# count=0
# flash=0
# while count<3:
#     print(" ",end="")
#     count+=1
# while flash<3:
#     print("* ",end='')
#     flash+=1
