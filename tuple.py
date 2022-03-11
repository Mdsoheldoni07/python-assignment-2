'''
#tupple
x=("ask","hey")
y=(123,456)
z=(True,False)
t=tuple((123,"maaz",False,"maaz"))
print(type(x))
print(len(t))
print(x)
print(y)
print(z)
print(t)
#tuple access
a=("tanveer","maaz","fazal","sohel","salman")
print(a[2])
print(a[-3])
print(a[:2])
print(a[1:])
print(a[1:4])
print(a[-5:-1])
b=("maaz","arab","sakru")
if "arab" in b:
  print("yes, its present in it")
#update tupples
a=(123,123,167,"maaz")
b=("tanveer",)
a+=b
print(a)
a=(123, 123, 167, 'maaz', 'tanveer')
b=list(a)
b[2]="sohel"
a=tuple(b)
print(a)
c=(123, 123, 'sohel', 'maaz', 'tanveer')
d=list(a)
d.append("fazal")
c=tuple(d)
print(c)
e=(123, 123, "sohel", "maaz", "tanveer")
f=list(e)
f.remove("sohel")
e=tuple(f)
print(e)
g=(123, 123, 'maaz', 'tanveer')
h=list(g)
h.remove(123)
g=tuple(h)
print(g)
i=(123, 'maaz', 'tanveer')

print(i)
#unpacking tuple


fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

'''

'''
_a = (10,20,30)


(first_class1 , second_class2
 , third_class3 ) = _a
print(first_class1)
print(second_class2)
print(third_class3)
'''
'''
#Using Asterisk*
_a = (10,20,30,40,50,60,70)
(a,b,c,*d)=_a
print(a,b,c,d)
(a,b,*c,d)=_a
print(a,b,c,d)
'''
'''
#tuple loop
b = ("maaz","sohel","fazal")
for x in b:
  print(b)

b = ("maaz","sohel","fazal")
for x in b:
  print(x)
'''
'''
_c=("tvs","adas","yamaha")
for x in range(len(_c)):
  print(_c[x])
'''
'''
_d=(12,21,25,65,35,15,34,35869)
x=0
while x < len(_d):
   print(_d[x])
   x=x+3
'''
'''
#join tuple
_e=(12,13,14)
a=(21,31,41)
c=a+_e
d=a*2
print(c)
print(d)
'''

z=(1,2,3,4,5,6,8,9,7,6,8,9,7,7,8,7)
x=z.count(7)
y=z.index(3)
print(x)
print(y)













