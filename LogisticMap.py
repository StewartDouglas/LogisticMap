import numpy
import matplotlib 
import matplotlib.pyplot as plt
import scipy

eps = 0.01
u = 0.0
r = 2.9
dr = 0.001
u = u + eps
r_list = []
u_list = []

while r < 4.0:
    for i in range(1,501):
        u = r*u*(1.0 - u)
    for i in range(1,100):
        u = r*u*(1.0 - u)
        r_list.append(r)
        u_list.append(u)
    r = r+dr
    u = u+eps

plt.pylot.scatter(r_list,u_list, s=1, facecolor='0.1', lw = 0)
#plt.pyplot.axis([2.9,4.0,0,1])
#plt.pyplot.show()
