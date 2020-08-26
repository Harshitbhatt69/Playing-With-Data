#Ploting with lines Graph
from matplotlib import pyplot as plt #lib for ploting

from matplotlib import style    #lib for styling graphs

style.use('ggplot') #stylesheet
x=[5,8,10]  #x coordinates for line 1
y=[12,16,6]  #y coordinates for line 1
x2=[6,9,11]    #x coordinate for line 2
y2=[6,15,7]     #y coordinates for line 2
#plt.plot() for linear graph
plt.plot(x,y,'g',label='line 1',linewidth=2)   #syntax: (x coordinates, y coordinates, colour of line, topic of the line, widthof line)
plt.plot(x2,y2,'c',label='line 2',linewidth=2) #syntax: (x coordinates, y coordinates, colour of line, topic of the line, widthof line)
plt.title('Info')   #topic of the graph
plt.ylabel('Y axis') #Name displayed in y axis
plt.xlabel('X axis') #Name displayed in x axis
plt.grid(True,color='black')  # for grids in background, syntax: plt.grid(True/False,Color='..')
plt.legend()    #displays the label of the line, Default:- top left
plt.show() #kind of print statement for graph