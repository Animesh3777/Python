n = int(input("Enter the n number"))
sum = 0
# for i in range(1,n+1):
#     if i%2==0:
#         sum+=i
# print("Sum of n is:", sum)

# while loop
i = 1
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)
