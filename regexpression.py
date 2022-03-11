import re
a = "sohel saqeeb shoaib"
x = re.search("^sohel.*shoaib$",a)
print(x)
if x:
    print("yes ots match")
else:
    print("no its not a matrch")
    
b = "who the hell you are to tell me like that"
x1 = re.search("hire",b)
print(x1)
if x1:
    print("its there")
else:
    print("its not there")

c = "hi how are you"
x3 = re.search("\s",c)
print(x3.start())
    
d = "tanveer what are you doing"
x4 = re.split("\s",d)
print(x4)

d = "tanveer what are you doing"
x4 = re.split("\s",d,2)
print(x4)

d = "tanveer what are you doing"
x4 = re.sub("\s", "gap",d)
print(x4)


d = "tanveer what are you doing"
x4 = re.sub("\s", "gap",d,2)
print(x4)

b = "who the hell you are to tell me like that"
x1 = re.search("e",b)
print(x1)
