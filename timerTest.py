#python
#ls-duan
import time,sys
timer=time.time_ns
repst=10000
repslist=list(range(repst))
def total(reps,func,*pargs,**kargs):
    """
    Total time to run func() reps times
    Return (total time,last result)
    """
    replist=list(range(reps))
    start=timer()
    for i in replist:
        ret=func(*pargs,**kargs)
    elapsed=timer()-start
    return (elapsed,ret)

def bestof(reps,func,*pargs,**kargs):
    """
    Quickest func() among reps runs.
    Returns(best time,last result)
    """
    best=2**32
    for i in range(reps):
        start=timer()
        ret=func(*pargs,**kargs)
        elapsed=timer()-start
        if elapsed<best:best=elapsed
    return (best,ret)

def bestoftotal(reps1,reps2,func,*pargs,**kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1,total,reps2,func,*pargs,**kargs)


def forLoop():
    res=[]
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs,repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)
'''for test in (forLoop,listComp,mapCall,genExpr,genFunc):
    (bestoff,(num,result))=bestoftotal(5,1000,test)
    print('%-9s:%.5f=>[%s...%s]' % (test.__name__,bestoff/1000000000,result[0],result[-1]))
'''
