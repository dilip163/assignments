#1ans]
number=int(input("enter the number"))
mul=1
for i in range(2,number+1):
    mul=mul*i
print(mul)

#2ans]
number1=int(input("enter the number"))
for i in range(1,11):
    print('{} X {} ='.format(number1,i),number1*i)

#3ans]
n1,n2=1,1
list1=[n1,n2]
number2=int(input("enter the number"))
for i in range(1,number2):
    n=n1+n2
    n1,n2=n2,n
    list1.append(n)
print(list1)

#4ans]
number3=int(input("enter the number"))
dup=number3
order=len(str(number3))
sum=0
while dup>0:
    n_1=dup%10
    sum=sum+(n_1**order)
    dup=int(dup/10)
print(sum)
if sum==number3:
    print('entered is the armstrong number')
else:
    print('entered is not the armstrong number')

#5ans]
lower,upper=100,2000
for i in range(lower,upper+1):
    dup = i
    order = len(str(i))
    sum = 0
    while dup > 0:
        n_1 = dup % 10
        sum = sum + (n_1 ** order)
        dup = int(dup / 10)
    if sum == i:
        print(i)

#6ans]
number4=int(input("enter the number"))
sum=0
for i in range(1,number4+1):
    sum=sum+i
print(sum)