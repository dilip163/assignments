#1ans]
number=int(input('enter a number:'))
if number<0:
    print(number,'is negitive number')
elif number>0:
    print(number,'number is positive')
else:
    print(number,'is zero')

#2ans]
value=int(input('enter the number'))
if value%2==0:
    print(value,'is the even number')
else:
    print(value,'is a odd number')


#3ans]
year = int(input("enter the year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


#4ans]
status=True
check_prime=int(input("enter the number"))
for i in range(2,check_prime):
    if check_prime%i==0:
        status=False
if status:
    print(check_prime,'is a prime number')
else:
    print(check_prime,'is not a prime number')

#5ans]
empty=[]
for i in range(1,10000):
    status = True
    for i in range(2, i):
        if check_prime % i == 0:
            status = False
    if status:
        empty.append(i)
print(empty)
    
