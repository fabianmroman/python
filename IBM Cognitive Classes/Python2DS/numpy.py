import numpy as np 
import matplotlib.pyplot as plt
# %%
import sys

print(sys.version)
x=np.linspace(-np.pi,np.pi,num=5)
y=np.sin(x)
plt.plot(x,y)
#plt.show()
