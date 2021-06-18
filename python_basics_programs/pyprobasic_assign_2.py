#1ans]
kilometers=float(input("enter the value in kilometers"))
miles=kilometers*0.621
print('miles:',miles)

#2ans]
celsius=float(input("enter the value in celsius"))
fohreenheit=(celsius*9/5)+32
print("fohreenheit:",fohreenheit)

#3ans]
import calendar
yy = int(input('enter year '))  # year
for i in range(1,13,1):
    print(calendar.month(yy, i))


#4ans]
import cmath
a,b,c = 1,5,6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))