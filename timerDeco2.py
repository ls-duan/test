import time
def timer(label='',trace=True):
    class Timer:
        def __init__(self,func):
            self.func=func
            self.alltime=0
        def __call__(self, *args, **kargs):
            start=time.time_ns()/1000000000
            result=self.func(*args,*kargs)
            elapsed=time.time_ns()/1000000000-start
            self.alltime+=elapsed
            if trace:
                format='%s %s:%s:%.5f,%.5f'
                values=(label,self.func.__name__,args[0],elapsed,self.alltime)
                print(format % values)
            return result
    return Timer