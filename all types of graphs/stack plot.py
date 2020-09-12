#Area Graph/ stack Graph
from matplotlib import pyplot as plt #importing libs

days=[1,2,3,4,5,6,7]    #Tracking days

#===============Data to be tracked================
sleeping=[7,8,6,11,7,15,7]
eating=[2,3,4,3,2,5,8]
working=[7,8,7,2,2,9,7]
playing=[8,5,7,8,13,8,10]

#==============Using it like a linear line for legend function================
plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)

#syntax: plt.stackplot(data to be tracked, name of data....,...,...upto last data, colour)
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel('x axis') #label of x axis
plt.ylabel('y axis')    #label of y axis
plt.title('Area/Stack plot')    #label of Plot
plt.legend()
plt.show()