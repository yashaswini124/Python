#n1 and n2 are placeholders and n2=0 is default value
 
def sum(n1,n2=0):
    sum=n1+n2
    return sum
x=25
y=15
print("sum is",sum(x,y)) 

#positional argument
print(sum(25,15))

#keyword argument
print(sum(n1=27 ,n2=19))

#default arguments- n2 takes a default value 0
print(sum(8))

# arbitary arguments-accepts variable number of arguments
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print("sum is ",add(45,9,60,2))

#keyword arbitary arguments- key value pairs
def studentinfo(**dictionary):
    for x,y in dictionary.items():
        print(x,y)

studentinfo(name="yashu", city="banglore")
studentinfo(a=4,b=6,c=8,d=10)
