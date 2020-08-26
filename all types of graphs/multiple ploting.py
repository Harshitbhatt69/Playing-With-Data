import matplotlib.pyplot as plt #imported only pyplt
import numpy as np #imported all numpy

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t) #calculation

t1=np.arange(0.0,5.0,0.1) #Defiening: from 0.0 to 5.0 in step of 0.1
t2=np.arange(0.0,5.0,0.02)  #Defiening: from 0.0 to 5.0 in step of 0.02

plt.subplot(211) #syntax: plt.subplot(total number of graph || graph present vertically || current graph no.)
plt.plot(t1,f(t1),'o',t2,f(t2)) #arguments of domain

plt.subplot(212)    #syntax: plt.subplot(total number of graph || graph present vertically || current graph no.)
plt.plot(t2,np.cos(2*np.pi*t2)) #arguments of domain
plt.show()

