from matplotlib import pyplot as plt
import numpy as np

a1 = np.array([0.1,0.4,0.3])
a2 = np.array([0.5,0.4,0.3])
plt.errorbar([0,1,2], [1,1,1], yerr=(a1,a2), capsize=5, fmt='o')
plt.show()