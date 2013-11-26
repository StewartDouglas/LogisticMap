import matplotlib as plt
import pylab

# Used for pertubation
eps = 0.01
# u is the dependent variable here
u = 0.0
# Small perturbation in u
u = u + eps

# r is plotted on the x-axis. Different
# values of r produce very different behaviour.
# In population dynamics r represents the
# combined rate for reproduction and starvation
r = 0.0
dr = 0.005

# Stored the x-axis values in r_list,
# and the y-axis values in u_list
r_list = []
u_list = []

while r < 4.0:
    # Throw away the 1st 200 iterations so that we
    # converge to the equilibria
    for i in range(1,200):
        u = r*u*(1.0 - u)
    for i in range(1,500):
        u = r*u*(1.0 - u)
        r_list.append(r)
        u_list.append(u)
    r = r+dr
    u = u+eps

# Plot the output
plt.pyplot.scatter(r_list,u_list, s=1, facecolor='0.1', lw = 0)
plt.pyplot.axis([1.0,4.0,0,1.0])
plt.pyplot.show()
