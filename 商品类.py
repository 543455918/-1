class shangpinlei(object):
    def __init__(self,num,name,price,summ,last):
        self._num=num
        self._name=name
        self._price=price
        self._summ=summ
        self._last=last

    def display(self):
        print('%d %s %f %d %d'%(num,name,price,summ,last))

    def income(self):
        s=(summ-last)*price
        print('%d'%s)

    def setdata(self):
        a=input().split()
        self._num = int(a[0])
        self._name = a[1]
        self._price = float(a[2])
        self._summ = int(a[3])
        self._last = int(a[4])

def main():
    b = input().split()
    shangpinlei=shangpinlei(int(b[0]),b[1],float(b[2]),int(b[3]),int(b[4]))

if __name__=='__main__':
    main()