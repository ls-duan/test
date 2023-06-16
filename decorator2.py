class Tracer(object):
    def __init__(self,func):
        self.calls=0
        self.func=func
    def __call__(self, *args, **kwargs):
        self.calls +=1
        print('call %s to %s' % (self.calls,self.func.__name__))
        return self.func(*args,**kwargs)
    def __get__(self, instance, owner):
        return wrapper(self,instance)
class wrapper:
    def __init__(self,desc,subj):
        self.desc=desc
        self.subj=subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj,*args,**kwargs)

if __name__=='__main__':
    @Tracer
    def spam(a,b,c):
        print(a+b+c)

    @Tracer
    def eggs(N):
        return 2**N
    spam(1,2,3)
    spam(a=4,b=5,c=6)
    print(eggs(32))

    class Person:
        def __init__(self,name,pay):
            self.name=name
            self.pay=pay
        @Tracer
        def giveRaise(self,percent):
            self.pay *=(1.0+percent)
        @Tracer
        def lastName(self):
            return self.name.split()[-1]
    print('method')
    bob=Person('Bob Smith',5000)
    sue=Person('Sue Jones',10000)
    print(bob.name,sue.name)
    sue.giveRaise(.10)
    print(int(sue.pay))
    print(bob.lastName(),sue.lastName())