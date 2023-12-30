# global and local variable 
# def g(y):
#     print(x)
#     print(x+1)
# x=5
# g(x)
# print(x)

# def f(y):
#     x=1
#     x+=1
#     print(x)
# x=5
# f(x)
# print(x)
    
# def h(y):
#     x+=1
    
# x=5
# h(x)
# print(x) 
# """it will give error, 
# bcoz this cant shange global variable"""

    
# def h(y):
#     global x
#     x+=1
    
# x=5
# h(x)
# print(x) # this code will work

# def f(x):
#     x = x + 1
#     print('in f(x): x', x)
#     return x

# x = 3
# z = f(x)
# print('in main program scope: z =', z)
# print('in main program scope: x =', x)


# def f():
#     def g():
#         print('inside function g')
#     g()
#     print('inside function f')

# print(f())


# def g(x):
#     def h():
#         x='abc'
#         # print(x)
#     x=x+1
#     print('in g(x): x=',x)
#     h()
#     return x
# x=3
# z=g(x)

def g(x):
    def h(x):
        x=x+1
        print("in h(x):x =",x)
    x=x+1
    h(x)
    return x
x=3
z=g(x)
print("in main program scope: x= ",x)
print("in main program scope: z= ",z)

