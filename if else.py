#if  statement
a=100
b=200
if a<b:
    print("b is greater than a")
#IF ELIF
c=100
d=100
if c>d:
    print("c is greater than d")
elif c==d:
    print(" c and d are equal")
#if elif and else
e=300
f=500
if e>f:
    print("e is greater than f")
elif e==f:
    print("e and f are equal")
else:
    print("e is less than f")
#short hand if
g=10
h=20
print("yes") if g > h  else print("no") 
print("yes") if g > h else print("no") if h > g else print("exactly")
#and
i=200
j=500
k=700
if i > j and k > j:
    print("botth conditions are true")
elif i == j and k > j:
    print(" these conditions are true ")
else:
    print("both statements are false")
if i > k or j == i:
    print("hence its true" )
elif i==f or k < j:
    print("these elif condition is corrrect")
else:
    print("both conditions are not true")
if not( i > j and k < j ):
    print("if statisfied")
#nested if    
j=100
if j > 20:
    print("first step")
    if j > 40:
        print("secon step")
        if j > 60:
            print("third step")
            if j > 80:
                print("fourth step")
                if j > 100:
                    print("fifth step")
                elif j==100:
                    print("last step")
                else:    
                    print("end of limits")
k=100
l=200
if k > l:
    pass
