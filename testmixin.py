#!python
#@author by ls-duan
"""
Generic lister mixin tester: similar to transitive reloader in Chapter
25, but passes a class object to tester (not function),and the testByNames
adds loading of both module and class by name string here,in keeping
with Chapter 31's factories pattern.
"""
import importlib
def classTs(listerclass,sept=False):
    class Super:
        def __init__(self):
            self.data1='spam'
        def ham(self):
            pass
    class Sub(Super,listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2='eggs'
            self.data3=42
        def spam(self):
            pass
    instance=Sub()
    print(instance)
    if sept:print('_'*80)
def tsByNames(mod_name,classname,sept=False):
    modobject=importlib.import_module(mod_name)
    listerclass=getattr(modobject,classname)
    classTs(listerclass,sept)
if __name__=='__main__':
   tsByNames('listInstance','ListInstance',True)