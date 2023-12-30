def is_even(num):
    if type(num)==int:
     if num%2==0:
         return num,"Is Even"
     else:
         return num,"Is Odd"
    else:
        return"Try integer Value"
while True:
    try:
        number = int(input("Enter the number: "))
        break  # Break out of the loop if the input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(is_even(number))

for i in range(1, 9):
    result = is_even(i)
    print(result)

