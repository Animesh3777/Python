# # x-> x^2
# a=lambda x:x**2
# print(a(2))

# sum=lambda x,y:x+y
# print(sum(3,4))

# #check if a string has 'a'

# h=lambda s:'a' in s
# print(h("Jarvis")) #True
# print(h("Sun")) #False

# oe=lambda x:'Is even' if x%2==0 else "I sodd"
# print(oe(6))



# #Higher Order Function (HOF)

# def sqr(x):
#     return x**2

# def transform(f,L):
#     output=[]
#     for i in L:
#         output.append(f(i))
    
#     print(output)
    
# L=[1,2,3]
# print(transform(sqr,L))

# HOF using lambda

# print(transform(lambda x:x**2,L))


# def cube(g,L2):
#     output=[]
#     for i in L2:
#         output.append(g(i))
#     print(output)
# L2=[1,2,3]

# print(cube(lambda x:x**3,L2))

#MAP
# print(list(map(lambda x:x**2,[1,2,3,4,5])))

# L=[1,2,3,4,5]
# oe2=list(map(lambda x:'even' if x%2==0 else "odd",L))
# print(oe2)

#Filter

# L=[78,3,4,5,6,7,0,12]
# Flr=list(filter(lambda x:x>5,L))
# print(Flr)

fruits=["apple","guava","cherry"]
flr=list(filter(lambda x:x.startswith("a"),fruits))
print(flr)
