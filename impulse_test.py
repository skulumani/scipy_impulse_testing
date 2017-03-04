import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# @befelix Here's how the related functions in scipy seem to handle initial conditions

# * [`scipy.integrate.odeint`](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.integrate.odeint.html) - highest order to lowest i.e `[xd0, x0]` from the example. In the end it seems it only has to match the order of states in the ode function.

# As a comparison, Matlab uses the following convention

# * [`lsim` ](https://www.mathworks.com/help/control/ref/lsim.html)
# ~~~
# lsim(sys,u,t,x0) further specifies an initial condition x0 for the system states. This syntax applies only when sys is a state-space model. x0 is a vector whose entries are the initial values of the corresponding states of sys.
# ~~~
# * 


num = 1
den = [1, 4, 5]
time = np.linspace(0,5,100)
sys = signal.TransferFunction(num,den)

x0 = 1
xd0 = 2

# impulse
# t, im = signal.impulse(sys,X0=(xd0, x0), T=time) # doesn't work
# t, im = signal.impulse(sys, X0=np.array([xd0, x0]), T=time) # doesn't work
t, im = signal.impulse(sys, X0=np.array([[xd0],[x0]]), T=time)

# impulse2
# t, im2 = signal.impulse2(sys,X0=(xd0, x0), T=time)
t, im2 = signal.impulse2(sys, X0=np.array([x0, xd0]), T=time)
# t, im2 = signal.impulse2(sys, X0=np.array([[xd0],[x0]]), T=time) # doesn't work

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(time,im, label='Impulse1')
ax.plot(time,im2, label='Impulse2')
ax.legend()
plt.show()