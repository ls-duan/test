#python
#ls-duan
import time,timerTest
timer=time.time_ns

def total(func,*pargs,**kargs):
    _reps=kargs.pop('_reps',1000)
    repslist=list(range(_reps))
    start=timer()
    for i in repslist:
        ret=func(*pargs,**kargs)
    elapsed=timer()-start
    return (elapsed,ret)

def bestof(func,*pargs,**kargs):
    _reps=kargs.pop('_reps',5)
    best=2**32
    for i in range(_reps):
        start=timer()
        ret=func(*kargs,**pargs)
        elapsed=timer()-start
        if elapsed<best:best=elapsed
    return (best,ret)

def bestoftotal(func,*pargs,**kargs):
    _reps1=kargs.pop('_reps1',5)
    return min(total(func,*pargs,**kargs) for i in range(_reps1))

for test in (timerTest.forLoop,timerTest.listComp,timerTest.mapCall,timerTest.genExpr,timerTest.genFunc):
    (totalnum,result)=bestoftotal(test,_reps1=5,_reps=1000)
    print('%-9s:%.5f=>[%s...%s]' %(test.__name__,totalnum/1000000000,result[0],result[-1]))
