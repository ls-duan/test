#! by python
#@author by ls-duan
import sys,time
force =list if sys.version_info[0]==3 else (lambda x:x)

class Timer:
    def __init__(self,func):
        self.func=func
        self.alltime=0
    def __call__(self, *args, **kargs):
        start=time.time_ns()/1000000000
        result=self.func(*args,**kargs)
        elapsed=time.time_ns()/1000000000-start
        self.alltime+=elapsed
        print('%s %s:%.5f,%.5f' % (self.func.__name__,args[0],elapsed,self.alltime))
        return result

@Timer
def listcomp(N):
    return [x*2 for x in range(N)]

@Timer
def mapcall(N):
    return force(map((lambda x:x*2),range(N)))

result=listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime=%s' % listcomp.alltime)
print(' ')
result=mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime=%s' % mapcall.alltime)
print('\nmap/comp=%s' % round(mapcall.alltime/listcomp.alltime,3))