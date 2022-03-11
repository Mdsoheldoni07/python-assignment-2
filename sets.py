
#python access
a={1,2,3,4,5}
for x in a:
  print(x)
print(6 in a)
#python add itesms
c={10,20,30,40,50}
c.add(100)
print(c)
d={200,400,600}
c.update(d)
print(c)
e=(1000,2000)
c.update(e)
print(e)
print(c)
f={"yes:True","no:False"}
c.update(f)
print(c)
#remove item
c.remove("yes:True")
print(c)

c.discard("no:False")
print(c)
x=c.pop()
print(c)
c.clear()
print(c)
del c
print(c)
'''
'''
#loop
n={200,400,600}
for x in n:
    print(x)

#joins
a={"saqeeb","shoaib","sohel"}
b={"no3","no2","no1"}
c=a.union(b)
print(c)
p={"maaaz","tanveer","fazal"}
q={20,30,40}
p.update(q)
print(p)
r={1,2,3,4,5,16}
s={61,5,4,3,2,1,4}
t=r.intersection_update(s)
print(s)
r.intersection(s)
print(r)
r.symmetric_difference_update(s)
print(r)
u=r.symmetric_difference(s)
print(u)












