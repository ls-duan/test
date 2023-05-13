#!python
#author by ls-duan
class ListInherited:
    """
    Use dir() to collect both instance attrs and names inherited from
    its classes;Python 3.X shows more names than 2.X because of the
    implied object superclass in the new-style class model;getattr()
    fetches inherited names not in self.__dict__;use __str__,not
    __repr__,or else this loops when printing bound methods!
    """
    def __attrnames(self):
        result=''
        for attr in dir(self):
            if attr[:2]=='__' and attr[-2:]=='__':
                result +='\t%s\n' % attr
            else:
                result +='\t%s=%s\n' % (attr,getattr(self,attr))
        return result
    def __str__(self):
        return '<Instance of %s,address %s:\n%s>' % (self.__class__.__name__,id(self),self.__attrnames())

if __name__=='__main__':
    import testmixin
    testmixin.classTs(ListInherited)