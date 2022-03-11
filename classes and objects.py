class my1:
    x=100
print(my1)    

class my2:
    x=100

s1=my2()
print(s1.x)

class student:
    def __init__(self,name,roll_no,usn):
        self.name= name
        self.roll_no= roll_no
        self.usn= usn


p1=student("sohel",1251,"2sa15cv427")
p2=student("sohel1",1252,"2sa15cv427")
p3=student("sohel2",1253,"2sa15cv427")
p4=student("sohel3",1254,"2sa15cv427")
p5=student("sohel4",1255,"2sa15cv427")
p6=student("sohel5",1256,"2sa15cv427")
p7=student("sohel6",1257,"2sa15cv427")
print(p1.name,p1.roll_no,p1.usn)
print(p2.name,p2.roll_no,p2.usn)
print(p3.name,p3.roll_no,p3.usn)
print(p4.name,p4.roll_no,p4.usn)
print(p5.name,p5.roll_no,p5.usn)
print(p6.name,p6.roll_no,p6.usn)
print(p7.name,p7.roll_no,p7.usn)


class staff:
    def __init__(self,name,salary,):
        self.name=name
        self.salary=salary

s1=staff("salman",100000)
print(s1.name,s1.salary)






class home:
    def __init__(self,name,work,time):
        self.name= name
        self.work = work
        self.time = time


h1=home("sohel","grocery", "9-12hrs")
print(h1.name,
      h1.work,
      h1.time)



class friends:
    def __init__(self,name,location):
        self.name = name
        self.location = location


    def sentence(self):
            print("my name is" ,self.name , " my location is ", self.location)
f1=friends("maaz","m-mart")
f1.sentence()
f2=friends("tanveer","j m road")
f2.sentence()
f3=friends("fazal","sedji malla")
f3.sentence()
f4=friends("sohel","aman coloney")
f4.sentence()
f5=friends("saeed","gandhi chowk")
f5.sentence()
#print(f1.name,f1.location,f2.name,f2.location,f3.name,f3.location,f4.name,f4.location,f5.name,f5.location)

class employees:
    def __in__(self,id1,name,email,contact_no):
        self.id1 = id1
        self.name = name
        self.email = email
        self.contact_no = contact_no


    def s1(self):
        print("id no this is",self.id1,"having email",self.name,"and contact no",self.email,"going to be hiked fo their salary",slf.contact_no, "contact them")
emp1=employees(1,"sohel","abc@gmail.com",6361231466)
emp1.s1()
emp2=employees(2,"maaz","abc@gmail.com",6361231466)
emp2.s1()
emp3=employees(3,"tanveer","abc@gmail.com",6361231466)
emp3.s1()
emp4=employees(4,"fazal","abc@gmail.com",6361231466)
emp4.s1()
emp5=employees(5,"saeed","abc@gmail.com",6361231466)
emp5.s1()
