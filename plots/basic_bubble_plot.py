# A bubble plot is close to scatter plot
# With the help of matlibplot library, we construct them using the same scatter function

#libraries
import matplotlib.pyplot as plt
import numpy as np

#creation of data using rand
x = np.random.rand(30)
y = np.random.rand(30)
z = np.random.rand(30)

#scatter funtion
plt.scatter(x,y,s=z*1000, alpha=0.5) #alpha bending value between 0 to 1 opaque
plt.show()
