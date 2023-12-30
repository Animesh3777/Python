# type an id
# def square(num):
#     return num**2

# print(square(3))
# print(type(square))
# print(id(square))

#reassign
# x= square(3)
# print(x)

# x=square
# print(x(3))

# del square #now i am deleting the function
# print(square(2))

# L= [1,2,3,square]
# print(L)
# print(L[-1](3))

# # returning a function 
# def f():
#     def x(a,b):
#         return a+b
#     return x

# val=f()(3,4)
# print(val)

def func_a():
    print("inside the func_a")

def func_b(z):
    print("inside the func b")
    return z()

print(func_b(func_a))
