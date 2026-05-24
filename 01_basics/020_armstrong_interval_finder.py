lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Armstrong Numbers are:")

for num in range(lower, upper + 1):
    sum = 0
    temp = num
    
    power = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** power
        temp = temp // 10

    if sum == num:
        print(num)