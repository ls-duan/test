#!python
#@author by ls-duan
#File listInstance.py(2.X+3.X)
class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instance via
    inheritance of __str__,coded here;displays instance attrs only;self is
    instance of lowest class;__X names avoid clashing with client's attrs
    """

    def __attrnames(self):
        result=''
    #    print(self.__dict__)
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr,self.__dict__[attr])
        return result
    def __str__(self):
        return '<Instance of %s,address %s:\n %s>' %(self.__class__.__name__,id(self),self.__attrnames())
if __name__=='__main__':
    import testmixin
    testmixin.tester(ListInstance)