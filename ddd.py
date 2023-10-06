#task 1 checks that the following relation holds for a given four-digit number: 
# the sum of the first and last digits is equal to the difference between the second and third digits. 
number = int(input("enter four digit number: "))

x1 = number // 1000
x2 = (number // 100) % 10
x3 = (number // 10) % 10
x4 = number % 10

if x1 + x4 == x2 - x3:
    print("yes")
else:
    print("no")



#task 2 determines whether a user is allowed to access an Internet resource or not. 
age = int(input("enter age: "))

if age >= 18:
    print("Access is allowed")
else:
    print("Access denied")


#task 3  consecutive terms
a = int(input("enter three number: "))
b = int(input())
c = int(input())

if b - a == c - b:
    print("YES")
else:
    print("NO")


#task 4 rook move horizontal and vertical
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if (x1 == x2) or (y1 == y2):
    print("YES")
else:
    print("NO")


#task 5 kings move one square 
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if (-1 <= x1 - x2 <= 1 ) and (-1 <= y1 - y2 <= 1):
    print("YES")
else:
    print("NO")


#task 6 average number
a = int(input())
b = int(input())
c = int(input())

numbers = [a, b, c]

numbers.sort()

print(numbers[1])


#task 7 number of days in month 
month = int(input("month"))

if month == 2:
    print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)


#task 8 weight define
weight = int(input())

if weight <= 60:
    print("Light weight")
elif weight <= 64:
    print("First welterweight")
else:
    print("Welterweight")


#task 9 password check
password = input()
password_confirmation = input()

if password == password_confirmation:
    print("Password accepted")
else:
    print("Password not accepted")



#task 10 odd or even
number = int(input())

if number % 2 == 0:
    print("Even value")
else:
    print("Odd number")


#task 11 min find
number1 = int(input())
number2 = int(input())

print(min(number1, number2))


#task 12 what age 
age = int(input())

if age <= 13:
    print("childhood")
elif 14 <= age <= 24:
    print("youth")
elif 25 <= age <= 59:
    print("maturity")
else:
    print("old age")


#task 13 triangle type4567
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Versatile")
