num = int(input("Enter your number"))
for i in range(2, num):
    if i % 2 == 0:
        print(i, "is not prime")
    else:
        print(i, "is prime")