
# age=int(input("how old are you"))
# if age >16 and age<=65:
#     print("ballsack")


# if 16<=age<=65:
#     print("go go gadget flow")



numbers="1,222;355:033 344,446;666"
seperators=""
# day="Monday"
# temperature=30
# raining=True
# if day == "saturday" and temperature>27 and not raining:
#     print("Go Swimming")
# else:
#     print("Learn python")

parrot = "Norwegian Blue"

for i in numbers:
    if not i.isnumeric():
        seperators=seperators+i
print(seperators)

values="".join(i if i not in seperators else " " for i in numbers).split()
print([int(val) for val in values])
