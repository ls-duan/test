class FormatError(Exception):
    logfile='formaterror.txt'
    def __init__(self,line,file):
        self.line=line
        self.file=file
    def logerror(self):
        log=open(self.logfile,'a')
        print('Error at:',self.file,self.line,file=log)

def parse():
    raise FormatError(40,'spam.txt')

if __name__=='__main__':
    try:
        parse()
    except FormatError as exc:
        exc.logerror()
