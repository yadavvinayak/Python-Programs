                                                                                               
                                                     

class A(object):
    def doThis(self):
        print('Doing this in A')

class B(A):
    pass

                                                                               
class C(object):
    def doThis(self):
        print('Doing this in C')

class D(B, A):
    pass

if __name__ == '__main__':
    dObj = D()
    dObj.doThis()                                                                                        

    print(D.mro())
