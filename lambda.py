x= lambda a: a+10
y= lambda b: b*10
print(x(5))
print(y(5))
a= lambda a,b,c: a+b+c
b= lambda a,b,c: a*b*c
c= lambda a,b,c: a+b*c
print(a(1,2,3))
print(b(1,2,3))
print(c(1,2,3))


def myfunction1(n):
    return lambda a,b,c: a*b*c*n

myequation = myfunction1(10)
myequation1 = myfunction1(200)
print(myequation(1,2,3))
print(myequation1(1,2,3))
