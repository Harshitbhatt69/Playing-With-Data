#Scatter plotting
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[5,3,4,2,5,4,2,1]
plt.scatter(x,y,label="random values",color="red") #syntax: plt.scatter(x coordinate, y coordinate, label, colour)
plt.title("Scatter Graph")  #heading of the graph
plt.legend()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()