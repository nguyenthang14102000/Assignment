#2
name=input("Ban ten la gi?")
print("Xin chao",name)

#3
r=float(input("radius="))
C=2*3.14*r
print("C=",(C))

#4
a=float(input("Length"))
b=float(input("Width"))
if a>b:
 p=(a+b)*2
 c=a*b
 print(f"Perimeter= {p},Area= {c}")
else:
 print("Wrong")

#5
a=int(input("Number1="))
b=int(input("Number2="))
c=int(input("Number3="))
d=a+b+c
v=a*b*c
n=d/3
print(f"Sum= {d}, product= {v}, average= {n}")

#6
a=float(input("Talent = "))
b=float(input("Pound = "))
c=float(input("Lot  = "))
total=a*20*32*13.3+b*32*13.3+c*13.3
kg=int(total/1000)
gr=round(total-kg*1000,2)
print(f"kg= {kg}, gr= {gr}")

#7
import random
a=range(0,9)
combo=random.sample(a,3)
b=range(1,6)
combo2=random.sample(b,4)
print(f"X= {combo}, Y= {combo2}")

