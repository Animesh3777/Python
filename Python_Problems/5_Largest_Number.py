num1 = float(input("Enter the 1st Number"))
num2 = float(input("Enter the 2nd Number"))
num3 = float(input("Enter the 3rd Number"))
if num1 > num2 or num1 > num3:
    print(num1, " is greater")
elif num2 > num1 and num2 > num3:
    print(num2, " is greater")
else:
    print(num3, " is greater")
