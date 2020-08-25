#Plotting with Bar Graph
from matplotlib import pyplot as plt  #lib for ploting
#plt.bar() for bar graph
plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example 1")  #syntax: plt.bar(value of x, value of y, name or bars, color)

plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example 2", color="g")
plt.legend()  #to show labels
plt.xlabel("Bar numbers")   #display name on x axis
plt.ylabel("Bar height")    ##display name on y axis

plt.title("Bar Graph")      #heading of bar graph
plt.show()  #kind of print statement for graph
