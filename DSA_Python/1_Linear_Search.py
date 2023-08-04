def linear_search(arr, length, item):
    for i in range(0, length):
        if arr[i] == item:
            return i
    return -1


arr = [10, 2, 8, 20, 40, 50, 25]
item = int(input("Enter the value that you'd want to search: "))
length = len(arr)
# print(length)
result = linear_search(arr, length, item)
if result == -1:
    print("The item {} was not found".format(item))
else:
    print("The value {} was found {} index".format(item, result))
