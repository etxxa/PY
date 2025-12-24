a=int(input("give a number a : "))
b=int(input("give a number b : "))
if a*b>0:
    c = a
    a = b
    b = c
    print("the new value of a is : ", a ,"\n and for b :", b)
else:
    print("a :",a+b,"\n and b :",a*b)
