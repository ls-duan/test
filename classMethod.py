class Spam:
    numInstances=0
    def __init__(self):
        Spam.numInstances=Spam.numInstances+1
    def printNumInstances(a):
        print('Number of instance created: %s' % Spam.numInstances)
if __name__=='__main__':
    a,b,c=Spam(),Spam(),Spam()
    a.printNumInstances()
    Spam.printNumInstances(a)
    Spam().printNumInstances()

class Methods:
    def imeth(self,x):
        print([self,x])
    def smeth(x):
        print([x])
    def cmeth(cls,x):
        print([cls,x])
    smeth=staticmethod(smeth)
    cmeth=classmethod(cmeth)