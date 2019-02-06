# A scattterplot made using matlibplot

#libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Dataset creation

datafr = pd.DataFrame({'x': range(1,101), 'y': np.random.rand(100)*15+range(1,101)})

#Plot
plt.plot('x','y',data=datafr,linestyle='none',markers='o')
plt.show()
