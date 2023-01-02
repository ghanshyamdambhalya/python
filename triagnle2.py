# https://i1.faceprep.in/fp/articles/img/46684_1580817324.png
# Write a programe to print 3 thrid triagnle
count=0
space=0
while count<7:
    print("*",end="")
    count+=1
print("")
print("*",end="")

count=4
while count>0:
    while space<count:
        print(" ",end="")
        space+=1
    print("*",end="")
    print("")
    print("*",end="")
    space=0
    count-=1


# while space<3:
#     print("_",end="")
#     space+=1
# print("*",end="")
# print("")
# print("*",end="")
# space=0
# while space<2:
#     print("_",end="")
#     space+=1
# print("*",end="")