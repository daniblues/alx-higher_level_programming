#!usr/bin/python3
mport random
number = random.randint(-10, 10)
if number < 0:
print(f"{} is negative".format(number))
elif number == 0:
print(f"{} is zero".format(number))
else:
print(f"{} is positive".format(number))
