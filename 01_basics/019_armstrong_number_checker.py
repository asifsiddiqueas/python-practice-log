num = int(input("Enter a number: "))

sum = 0
temp = num

power = len(str(num))

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** power
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")