"""

"""

import numpy as np
import matplotlib.pyplot as plt

N = 300
C = 15 
T = 100000

x = np.ones(N)*C

for t in range(T):
    i,j = np.random.choice(N,2)
    if x[i] > 0:
        x[i] -= 1
        x[j] += 1       
    y = 1/(1+C) * np.exp(-x/(C + 0.5))
    

plt.hist(x, bins='auto', density=True, alpha=0.75, rwidth = 0.7)
plt.plot(x, y, '.r')

plt.grid()
plt.title('Histogram of coconuts amounts')
plt.xlabel('Number of coconuts', fontsize=12)
plt.ylabel('Percentage of islanders', fontsize=12)

plt.savefig('Kokosy_hist.png', format = 'png')

