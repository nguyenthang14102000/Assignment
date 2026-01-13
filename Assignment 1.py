#2
name=input("Ban ten la gi?")
print("Xin chao",name)

#3
while True:
 try:
  r=float(input("radius="))
  if r>0:
   C=2*3.14*r
   print("C=",(C))
   break
  else:
   print("Wrong, enter posiver number")
   continue
 except:
  print("Wrong, enter positive number")

#4
while True:
 try:
  a=float(input("Length"))
  b=float(input("Width"))
  if a>0 and b>0 and a>b:
   p=(a+b)*2
   c=a*b
   print(f"Perimeter= {p},Area= {c}")
   break
  else:
   print("Wrong, enter number again")
   continue
 except:
  print("Wrong, enter number again")

#5
while True:
 try:
  a=int(input("Number1="))
  b=int(input("Number2="))
  c=int(input("Number3="))
  d=a+b+c
  v=a*b*c
  n=d/3
  print(f"Sum= {d}, product= {v}, average= {n}")
  break
 except:
  print("Wrong, enter number again")

#6
while True:
 try:
  a=float(input("Talent = "))
  b=float(input("Pound = "))
  c=float(input("Lot  = "))
  if a>0 and b>0 and c>0:
   total=a*20*32*13.3+b*32*13.3+c*13.3
   kg=int(total/1000)
   gr=round(total-kg*1000,2)
   print(f"kg= {kg}, gr= {gr}")
   break
  else:
   print("Wrong, enter number again")
   continue
 except:
  print("Wrong, enter number again")

#7
import random
a=range(0,9)
combo=random.sample(a,3)
b=range(1,6)
combo2=random.sample(b,4)
print(f"X= {combo}, Y= {combo2}")

