from matplotlib import pyplot as plt
import numpy as np
#As we need a 3-dimensional array we need 3 arrays to plot a 3d graph  
x=np.array([50,40,57,23,45,90,78,56,12,99,80])   # first array 
y=np.array([12,45,77,99,45,34,90,55,32,55,76])   # second array 
z=np.array([34,56,56,2,5,3,2,8,2,62,25])          #Third array 
'''
Once this submodule is imported, a three-dimensional axes 
can be created by passing the keyword projection='3d' to any of
 the normal axes creation routines:

'''
a=plt.axes(projection='3d')            
a.scatter3D(x,y,z)
a.plot3D(x,y,z)
'''
Notice that by default, the scatter points have their transparency adjusted
to give  a sense of depth on the page.
While the three-dimensional effect is sometimes
difficult to see within a static image,
an interactive view can lead to some nice intuition
about the layout of the points.
'''

for angle in range(0, 360):
    a.view_init(30, angle)


#The above loop is used to look at that graph at suitable angle . B
# But its fixed in this progarm if you want it to move
#another function is used to move that 
