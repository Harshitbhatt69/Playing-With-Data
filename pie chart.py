from matplotlib import pyplot as plt
slice=[7,4,6,10,8]  #slices data
activities=['Working','Studying','Eating','Sleeping','Playing'] #name of slices
colours=['c','m','b','r','g']   #colours of slices

#syntax: plt.pie(slice data,name of slices,color of slices,shadow,startangle,explode,autppct)
"""
shadow: to enable shadow
startangle: to giving specific starting angle of pie chart to start with it.
explode: Use to show look of a piece taken out and highlight it.
autopct: convert input data into percentage and display it above pie.
"""
plt.pie(slice,labels=activities,colors=colours,shadow=True,explode=(0.1,0,0,0,0),autopct='%1.1f%%')
plt.title('Pie Plot')   #title of pie chart
plt.show()