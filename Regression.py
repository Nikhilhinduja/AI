x=[1,2,3,4,5,6]#hourses
y=[3,5,7,9,11,13]
class Regression:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.result=[None,None,None,None,None,None]
        self.comresult=["no","no","no","yes","yes","yes"]
        self.w0=None
        self.w1=None
        self.alpha=0.01
        self.h=[None,None,None,None,None,None]
    def hx(self,w0,w1):
        self.w0=w0
        self.w1=w1
        for i in range(len(self.x)):
            self.h[i]=self.x[i]*self.w1[1]+self.w0[i]
            if(self.h[i]>9):
                self.result[i]="yes"
            else:
                self.result[i]="no"
        return self.result
    def compare(self):
        for i in range(len(self.x)):
            if(self.result[i]!=self.comresult[i]):
                return False
        else:
            return True
    def value(self):
        for i in range(len(self.x)):
            self.w0[i]=self.w0[i]+self.alpha*(self.y[i]-self.h[i])
            self.w1[i]=self.w1[i]+self.alpha*(self.y[i]-self.h[i])*self.x[i]
        self.result=self.hx(w0,w1)
        print("result ",self.result)
        if(self.compare()):
            return "yes"
        else:
            print('No')
        self.value()
            
        
    
r=Regression(x,y)
w0=[1,1,1,1,1,1]
w1=[3,3,3,3,3,3]
r.hx(w0,w1)
print(r.compare())
if(not r.compare()):
    print(r.value())
else:
    print('true')
#h(x)=w0+w1*x
#w0=w0+alpha*(y-h(x))
#w1=w1+alpha*(y-h(x))*x
#find values of w0&w1 using regression that satisfy the function where alpha(0.01)
