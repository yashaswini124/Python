class add:
    def sum(self,a,b,c=0,d=0):   #method overloading is achieved by setting default parameters
        return (a+b+c+d)
    
class add_two_num(add):
    def sum(self,a,b):   #method overriding
        return a+b
    

a=add()    
print(a.sum(25,10,48))  #method overloading

b=add_two_num()
print(b.sum(39,41))