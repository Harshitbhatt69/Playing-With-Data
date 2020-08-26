#Plotting with Histogram
from matplotlib import pyplot as plt    #import main plot header file (matplotlib)
population_ages = [25,20,30,13,45,43,16,24,42,45,23,32,56,34,53,64,19,24,19,20,72,61,23,21,45,90,11,23,100,17,71,83,91,72,81,52,13,81,71,51,31]
bins = [0,10,20,30,40,50,60,70,80,90,100,110]
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.hist(population_ages,bins, histtype="bar",rwidth=0.8) #syntax: plt.hist(x axis, y axis, histtype, width as rwidth)
plt.title("Histogram")
plt.legend()
plt.show()