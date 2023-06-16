#! by python
#@ author by ls-duan
"""
File access.py (3.X+2.X)
Class decorator with Private and Public attribute declarations.

Control external access to attributes stored on an instance,or
Inherited by it from its classes.Private declares attribute names
that cannot be fetched or assigned outside the decorated class,
and Public declares all the names that can.

Caveat: this works in 3.X for explicitly named attributes only:__X__
operator overloading methods implicitly run for built-in operations
do not trigger either __getattr__ or __getattribute__ in newly-style
classes.Add __X__ methods here to intercept and delegate built-ins.
"""
traceMe=False
def trace(*args):
    if traceMe:print('['+'   '.join(map(str,args))+']')

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self,*args,**kargs):
                self.__wrapped=aClass(*args,**kargs)
            def __getattr__(self, attr):
                trace('get:',attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: '+attr)
                else:
                    return getattr(self.__wrapped,attr)
            def __setattr__(self, attr, value):
                trace('set:',attr,value)
                if attr=='_onInstance__wrapped':
                    self.__dict__[attr]=value
                elif failIf(attr):
                    raise TypeError('private attribute change: '+attr)
                else:
                    setattr(self.__wrapped,attr,value)
        return onInstance
    return onDecorator
def Private(*attributes):
    return accessControl(failIf=(lambda attr:attr in attributes))
def Public(*attributes):
    return accessControl(failIf=(lambda attr:attr not in attributes))

if __name__=='__main__':
    @Private('age')
    class Person:
        def __init__(self,name,age):
            self.name=name
            self.age=age
    x=Person('Bob',40)
    #print(type(x))
    print(x.name)
    x.name='Sue'
    print(x.name)
    #print(x.age)