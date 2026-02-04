#1
def length():
    while True:
        try:
            a=float(input("Enter length:"))
            b=42-a
            if a<42 and a>0:
                print("release the fish, centimeters below the size limit =", b)
                break
            elif a>=42:
                print("you can catch the fish")
                break
            else:
                print("please enter positive number")
        except:
            print("please enter number")
length()

#2
def class_():
    while True:
        a=input("enter class:").upper()
        if a=="B" or a=="C":
            print("windowless cabin above the car deck.")
            break
        elif a=="LUX":
            print("upper-deck cabin with a balcony.")
            break
        elif a=="A":
            print("above the car deck, equipped with a window.")
            break
        else:
            print("Invalid cabin class")
class_()

#3
def hemoglobin():
    while True:
        try:
            a=input("sex:")
            b=float(input("hemoglobin value:"))
            if a=="female" and b>=117 and b<=155 or a=="male" and b<=167 and b>=134:
                print("normal hemoglobin")
                break
            elif a=="female" and b<117 or a=="male" and b<134:
                print("low hemoglobin ")
                break
            elif a=="female" and b>155 or a=="male" and b>167:
                print("high hemoglobin ")
                break
            else:
                print("invalid value")
        except:
            print("invalid value")
hemoglobin()

#4
def year():
    while True:
        try:
            a=int(input("year:"))
            if a>0 and a%4==0 and a%100!=0:
                print("A year is a leap year")
                break
            elif a>0 and a%100==0 and a%400==0:
                print("A year is a leap year")
                break
            elif a>0:
                print("A year is not a leap year")
                break
            else:
                print("please enter positive number")
        except:
            print("please enter a year")
year()

#5
import math
def pizza(f,h):
    unit_price=h/((f/200)**2)*math.pi
    return unit_price
while True:
    try:
        a=float(input("pizza diameter 1:"))
        b=float(input("pizza's price 1:"))
        c=float(input("pizza diameter 2:"))
        d=float(input("pizza's price 2:"))
        n=pizza(a,b)
        m=pizza(c,d)
        if a>0 and b>0 and c>0 and d>0 and n>m:
            print ("Pizza 2 has better value")
            break
        elif a>0 and b>0 and c>0 and d>0 and n<m:
            print ("Pizza 1 has better value")
            break
        elif a>0 and b>0 and c>0 and d>0 and n==m:
            print ("2 Pizza have same value")
            break
        else:
            print("please enter positive number")
    except:
        print("please enter number")





