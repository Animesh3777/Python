num1 = int(input("Enter the number 1st"))
num2 = int(input("Enter the number 2st"))
if num1 > num2:
    mn = num2
else:
    mn = num1

# for i in range(1, mn + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i
# print(f'The HCF/GCD of {num1} and {num2} is {hcf}')


i = 1
# while loop
while i <= mn:
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
    i = i + 1
print(f'The HCF/GCD of {num1} and {num2} is {hcf}')
