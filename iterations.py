
a={"sohel","maaz","tanveer","saeed","fazal"}
x=iter(a)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

b="mohammad sohel doni"
a=iter(b)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


class sohel:
  def __iter__(self):
        self.x = 1
        return self
  def __next__(self):
        y = self.x
        self.x += 1
        return y
me = sohel()
go = iter(me)

print(next(go))
print(next(go))
print(next(go))
print(next(go))
print(next(go))
print(next(go))
print(next(go))
print(next(go))
print(next(go))
print(next(go))

class tanveer:
    def __iter__(self):
        self.p = 2
        return self
    def __next__(self):
        if self.p <= 100:
            q = self.p
            self.p += 2
            return q
        else:
            raise StopIteration

tan = tanveer()
result = iter(tan)


for x in result:
    print(x)
