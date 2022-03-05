# for i in range(1,13):
#     print("Number {} squared is {} and cubed is {:4}".format(i,i **2, i**3))

name=input("please enter your name ")
age=int(input("how old are you, {0} ".format(name)))#returrns a string data type
print(age)

if age >= 18:
    print("go vote")
else:
    print("please come back when you old enough")