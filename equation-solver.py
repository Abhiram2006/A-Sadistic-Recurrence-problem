def f1(a,b,c):
    return b+c-(((a+3)*(c+1)/(a+c+4))+b+4)/(((a+3)*(c+1)/(a+c+4))+b+5)
def f2(a,b,c):
    return a+c-((2*(c+2)*((b+3)/(b+3+2*c+4)+(a+1)/(a+1+2*c+4)))*(4*c+8)/(c+1))/(2*(c+2)*((b+3)/(b+3+2*c+4)+(a+1)/(a+1+2*c+4))+(4*c+8)/(c+1))
def f3(a,b,c):    
    return a+b-((5*c+11)*(b+2)/(5*c+2*b+15)+(5*c+11)*(a+1)/(5*c+3*a+14))*((5*c+11)/(c+1))/((5*c+11)*(b+2)/(5*c+2*b+15)+(5*c+11)*(a+1)/(5*c+3*a+14)+(5*c+11)/(c+1))
def f(a,b,c):
    return f1(a,b,c)**2+f2(a,b,c)**2+f3(a,b,c)**2
    
import math
a=2.1198433830655907
b=0.4782112637848495
c=0.369261403430641
N=1000000
l=1*10**(-9)
d=1*10**(-11)
for i in range(N):
    fa=(f(a+d, b, c)-f(a, b, c))/d
    fb=(f(a, b+d, c)-f(a, b, c))/d
    fc=(f(a, b, c+d)-f(a, b, c))/d
    
    F=math.sqrt(fa**2+fb**2+fc**2)
    a-=fa*l/F
    b-=fb*l/F
    c-=fc*l/F
    print(a,b,c)
print('Out of The Loop')
print(f(a,b,c))
print(f1(a,b,c))
print(f2(a,b,c))
print(f3(a,b,c))
