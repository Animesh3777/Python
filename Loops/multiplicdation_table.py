#multiplication table for a given number upto 10 and skipping the 5th iteration.
number =3
for i in range (1,11):
    if i==5:
        continue
        # break
    print (number,"x",i,"=",number*i)
    
