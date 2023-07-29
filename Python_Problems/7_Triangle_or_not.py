s1=float(input('Enter side 1 Length'))
s2=float(input('Enter side 2 Length'))
s3=float(input('Enter side 3 Length'))
if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
    print('it is a triangle')
else:
    print('it is not a triangle')