def myfunction():
    print("there is no parameters")

myfunction()    

def myfunction1(name,age,contact_no):
    print(name , age , contact_no)


myfunction1("sohel",22,6361913586,)
myfunction1("maz",24,6361913576,)
myfunction1("tanveer",30,6361913586,)
myfunction1("fazal",28,6361913586,)
myfunction1("shaheed",26,6361913586,)
myfunction1("saeed",24,6361913586,)
myfunction1("shukur",22,6361913586,) 

def myfunction2(*students):
    print("contact no is" , students[2] )


myfunction2("sohel",22,6361913586,)
myfunction2("maz",24,6361913576,)
myfunction2("tanveer",30,6361913586,)
myfunction2("fazal",28,6361913586,)
myfunction2("shaheed",26,6361913586,)
myfunction2("saeed",24,6361913586,)
myfunction2("shukur",22,6361913586,)



def myfunction3(**students):
    print("contact no is" , students["name1"]  )


myfunction3(name1="sohel",age=22,mob_no=6361913586,)
myfunction3(name1="maz",age=24,mob_no=6361913576,)
myfunction3(name1="tanveer",age=30,mob_no=6361913586,)
myfunction3(name1="fazal",age=28,mob_no=6361913586,)
myfunction3(name1="shaheed",age=26,mob_no=6361913586,)
myfunction3(name1="saeed",age=24,mob_no=6361913586,)
myfunction3(name1="shukur",age=22,mob_no=6361913586,)





def myfunction3(student_name="fazal"):
    print("contact no is" , student_name  )


myfunction3("sohel")
myfunction3("maz")
myfunction3("tanveer")
myfunction3()
myfunction3("shaheed")
myfunction3("saeed")
myfunction3("shukur")

def myfunction4(names):
    for x in names:
        print(x)
a=["sohel","saqeeb"]
myfunction4(a)

def myfunction5(x):
    return 10 * x

print(myfunction5(.5))    
print(myfunction5(1))
print(myfunction5(2))
print(myfunction5(3))    
print(myfunction5(4))
print(myfunction5(5))
