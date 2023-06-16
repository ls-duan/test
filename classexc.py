#! by python
#author @ ls-duan
class General(Exception):pass
class Specific1(General):pass
class Specific2(General):pass

def raise0():
    raise General()
def raise1():
    raise Specific1()
def raise2():
    raise Specific2()

for func in  (raise0,raise1,raise2):
    try:
        func()
    except General as X:
        import sys
        print('caught:%s' % X.__class__)