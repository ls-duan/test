#! by python
# @author by ls-duan
def tracer(func):
    calls=0
    def onCall(*args,**kwargs):
        nonlocal  calls
        calls+=1
        print('call %s to %s' % (calls,func.__name__))
        return func(*args,**kwargs)
    return onCall

@tracer
def spam(a,b,c):
    print(a+b+c)

@tracer
def eggs(x,y):
    print(x**y)

spam(1,2,3)
spam(a=4,b=5,c=6)
eggs(2,16)
eggs(4,y=4)

class Person:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    @tracer
    def giveRaise(self,percent):
        self.pay *=(1.0+percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]
print('method')
bob=Person('Bob Smith',5000)
sue=Person('Sue Jones',10000)
print(bob.name,sue.name)
sue.giveRaise(.10)
print(int(sue.pay))
print(bob.lastName(),sue.lastName())