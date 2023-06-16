"""
File access1.py (3.X+2.X)
Privacy for attribute fetched from class instance.
See self-test code at end of file for a usage example.

Decorator same as:Doubler=Private('data','size')(Doubler).
Private returns onDecorator,onDecorator returns onInstance,
and each onInstance instance embeds a Doubler instance.
"""
traceMe=False
def trace(*args):
    if traceMe:print('['+' '.join(map(str,args))+']')

def Private(*privetes):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self,*args,**kargs):
                self.wrapped=aClass(*args,**kargs)
            def __getattr__(self, attr):
                trace('get:',attr)
                if attr in privetes:
                    raise TypeError('private attribute fetch: '+attr)
                else:
                    return getattr(self.wrapped,attr)
            def __setattr__(self, attr, value):
                trace('set:',attr,value)
                if attr=='wrapped':
                    self.__dict__[attr]=value
                elif attr in privetes:
                    raise TypeError('private attribute change: '+attr)
                else:
                    setattr(self.wrapped,attr,value)
        return onInstance
    return onDecorator

if __name__=='__main__':
    traceMe=True

    @Private('data','size')
    class Doubler:
        def __init__(self,label,start):
            self.label=label
            self.data=start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size()):
                self.data[i]=self.data[i]*2
        def display(self):
            print('%s=>%s' % (self.label,self.data))
    X=Doubler('X is',[1,2,3])
    Y=Doubler('Y is',[-10,-20,-30])
    #The following all succeed
    print(X.label)
    X.display();X.double();X.display()
    print(Y.label)
    Y.display();Y.double()
    Y.label='Spam'
    Y.display()
    #The following all fail properly
    #print(X.size())
    #print(X.data)
    #X.data=[1,1,1]
    #X.size=lambda S:0
    #print(Y.data)
    #print(Y.size())