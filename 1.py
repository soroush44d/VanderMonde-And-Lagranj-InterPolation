import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
import sympy as sym

def frac_to_float(lst):
    lst2=[]
    for i in range(len(lst)):
        c=float(lst[i])
        lst2.append(c)
    return lst2

def x_append(x_size,xlist):
    elist=[]
    for i in range(x_size):
        for j in range(x_size):
            elist.append(xlist[i]**j)
    return elist



while(True):
    x=[Fraction(x) for x in input("input x :").split(",")]
    y=[Fraction(y) for y in input("input y :").split(",")]
    print("1)Lagranj InterPolation\n2)VanderMonde")
    if len(x)==len(y):
        method = int(input("Select:"))

        break
    print("The x and y data are not equal")



size= len(x)


a_list=x_append(size,x)
x_lst = frac_to_float(a_list)
y_lst = frac_to_float(y)


x_lst = np.array([x_lst])
x_lst=x_lst.reshape(size,size)
solved = np.linalg.solve(x_lst , y_lst)
if method==2:
    print("coefficients :",solved)
    print("*********************")
    print("The Equation is :")
    for k in range(size):
        if k==size-1:
            print(" ({})X^{} ".format(round(solved[size-k-1],2),size-k-1),end="")
        else:
            print(" ({})X^{} + ".format(round(solved[size-k-1],2),size-k-1),end="")


    def plot_func(range_num,solved,size:len(x),realx,realy):
        value=[]
        x = np.arange(-range_num , range_num,1)
        for i in range(-range_num , range_num):
            num = i
            sum=0
            for n in range(size):
                sum = solved[size-n-1]*(num**(size-n-1))+sum
            value.append(sum)
        plt.plot(x,value,'-b',realx,realy,'ro')
        plt.show()

    print("\n")
    #method2

    while(1):
        num = Fraction(input("-Type 00 for drow function \n-What is the value of equation for :"))
        if num ==00:
            plot_func(30 , solved,len(x),x,y)

        sum=0
        for n in range(size):
            sum = solved[size-n-1]*(num**(size-n-1))+sum

        print("Value for {} => {} ".format(num,sum))


def lagrange_inter(xlist,ylist):
    size = len(xlist)
    degree = size-1
    xp = sym.Symbol('xp')
    yp= sym.Symbol('yp')
    for i in range(size):
        p=1
        for j in range(size):
            if j !=i:
                p *=(xp-x[j])/(x[i]-x[j])
        yp += y[i]*p
    return (xp,yp)

if method==1:
    while(1):
        x_lst = frac_to_float(x)
        y_lst = frac_to_float(y)

        yp= sym.Symbol('yp')
        equation = lagrange_inter(x_lst,y_lst)[1]-yp
        equation = sym.simplify(equation)

        print("The Equation is :",equation)
        xp = input("Value For:")
        print(eval(str(equation).replace("xp",xp)))

        if xp =="00":
            x_r = [val for val in range(20)]
            y_r=[]
            for value in range(20):
                yvalue=eval(str(equation).replace("xp",str(value)))
                y_r.append(yvalue)
                
            plt.plot(x_r,y_r,'-b',x,y,'ro')
            plt.show()


