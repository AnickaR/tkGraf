from scipy import interpolate
import scipy.interpolate as inp
import pylab as lab

x="0 0.3 0.5 0.8 1 2 3".split()
y="0 0.1 0.5 1   3 10 30".split()

x=list(map(float, x))
y=list(map(float, y))

"""
bagr = []
for cislo in x:
    bagr.append(float(x))
x = bagr
"""

newX = lab.linspace(0,3, 333)
spl = inp.CubicSpline(x,y)
newY = spl(newX)



lab.plot(x,y,"o", label = "měřící body")
lab.plot(newX,newY, label= "interpolace")
lab.grid()
lab.legend()
lab.show()



