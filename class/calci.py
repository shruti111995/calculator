class calci:
    val1=0
    val2=0
    val3=0
    val4=0
    val5=0
    def __init__(self,num1,num2,num3,num4,num5):
       print("this is constructor")
       self.val1=num1
       self.val2=num2 
       self.val3=num3
       self.val4=num4
       self.val5=num5
    def addvalue(self):
        print(f'addition={self.val1+self.val2+self.val3+self.val4+self.val5}')

    def subvalue(self):
        print(f'substracton={self.val1-self.val2-self.val3-self.val4-self.val5}')
    def mulvalue(self):
        print(f'multiplication={self.val1*self.val2*self.val3*self.val4*self.val5}')
    def divvalue(self):
        print(f'division={self.val1/self.val2/self.val3/self.val4/self.val5}')
    def minvalue(self):
        print(f'minimum={min(self.val1,self.val2,self.val3,self.val4,self.val5)}')
    def maxvalue(self):
        print(f'maximum={max(self.val1,self.val2,self.val3,self.val4,self.val5)}')
    def modlusvalue(self):
        print(f'mod={self.val1//self.val2//self.val3//self.val4//self.val5}')    
    def meanvalue(self):
        print(f'mean={(self.val1+self.val2+self.val3+self.val4+self.val5/(5))}')  
    def total_75per(self):
        print('75% of total:',(75*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)     
    def total_50per(self):
        print('50% of total:',(50*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)

    def total_25per(self):
        print('25% of total:',(25*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)    
f1=calci(92,62,30,25,58) 
f1.addvalue()
f1.subvalue()
f1.mulvalue()
f1.divvalue()
f1.minvalue()
f1.maxvalue()
f1.modlusvalue() 
f1.meanvalue() 
f1.total_75per()
f1.total_50per()
f1.total_25per()  



print('f1.val1=',f1.val1)
print('f1.val2=',f1.val2)
print('f1.val3=',f1.val3)
print('f1.val4=',f1.val4)
print('f1.val5=',f1.val5)