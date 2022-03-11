class x1:
    def __init__(self,name,age,mob_no):
        self.name = name
        self.age = age
        self.mob_no = mob_no

    def details(self):
        print("my name is", self.name, "and age is", self.age,"and mob_no is", self.mob_no)

a=x1("sohel","24",6361913586)
a.details()
        
class x2:
    def __init__(self,name,age,mob_no):
        self.name = name
        self.age = age
        self.mob_no = mob_no
    def _x2(self):   
        print(self.name,self.age,self.mob_no)
class x3(x2):
    def __init__(self,name,age,mob_no):
        x2.__init__(self,name,age,mob_no)
a1=x3("sohel",25,6361913586)
a1._x2()
    
class tanveer:
    def __init__(self,name,age,mob_no):
        self.name = name
        self.age = age
        self.mob_no = mob_no

    def details(self):
        print(self.name,self.age,self.mob_no)

class sohel(tanveer):
    def __init__(self,name,age,mob_no,usn):
        super().__init__(name,age,mob_no)
        self.usn = usn
    def details2(self):
           print(self.name,self.age,self.mob_no,self.usn)   
        
        
a1=tanveer("tanvi","31",7019268335)

a2=sohel("tanveer","29",7019268334,"2sa16cv427")
a1.details()
a2.details2()
        
                
        
        
