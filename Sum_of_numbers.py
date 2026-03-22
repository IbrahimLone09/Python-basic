"""Program to find sum of "n" natural numbers"""

i = 1
n = int(input("Enter the number:"))
sum = 0
while i <= n:
    sum += i
    i += 1

print("The sum is:", sum)    