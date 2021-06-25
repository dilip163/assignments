# 1ans]
print('1ans]')
num = 175
rem = sum = 0
len_1 = len(str(num))
n = num
while (num > 0):
    rem = num % 10
    sum = sum + int(rem ** len_1)
    num = num // 10
    len_1 = len_1 - 1
if (sum == n):
    print(str(n) + " is a disarium number")
else:
    print(str(n) + " is not a disarium number")
print('---'*20)


# 2ans]
print('2ans]')
disarium=[]
for num1 in range(1,100):
    rem1 = sum1 = 0
    len1 = len(str(num1))
    num2=num1
    while (num1 > 0):
        rem1 = num1 % 10
        sum1 = sum1 + int(rem1 ** len1)
        num1 = num1 // 10
        len1 = len1 - 1
    if (sum1 == num2):
        disarium.append(num2)
print(disarium)
print('---'*20)


# 3ans]
print('3ans]')
str1='32'
str2=str1
while len(str1)!=1:
    list1=[int(i) for i in str1]
    sum=0
    for i in list1:
        sum=sum+(i**2)
    str1=str(sum)
if sum==1:
    print(str2 +' is a happy number')
else:
    print(str2 + ' is not a happy number')
print('---'*20)

# 4ans]
print('4ans]')
list3=[]
sum1=False
for j in range(10,100):
    str3=str(j)
    while len(str3) != 1:
        list1 = [int(i) for i in str3]
        sum1 = 0
        for i in list1:
            sum1 = sum1 + (i ** 2)
        str3 = str(sum1)
    if sum1:
        if sum1==1:
            list3.append(j)
    else:
        if i**2==1:
            list3.append(j)
print(list3)
print('---'*20)
print('5ans]')
num10 = 156
rem10 = sum10 = 0
n10 = num10
while (num10 > 0):
    rem10 = num10 % 10
    sum10 = sum10 + rem10
    num10 = num10 // 10
if (n10 % sum10 == 0):
    print(str(n10) + " is a harshad number")
else:
    print(str(n10) + " is not a harshad number")
print('---'*20)
print('6ans]')

def isPronicNumber(num):
    flag = False

    for j in range(1, num + 1):
        if ((j * (j + 1)) == num):
            flag = True
            break
    return flag

print("Pronic numbers between 1 and 100: ")
for i in range(1, 101):
    if (isPronicNumber(i)):
        print(i)