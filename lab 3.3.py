a,b=input("enter two numbers:").split()
print("two numbers are:",a,b)
c=abs(float(a)-float(b))
d=round(c,3)
if(d==0.001):
    print("close")
else:
    print("not close")
    
