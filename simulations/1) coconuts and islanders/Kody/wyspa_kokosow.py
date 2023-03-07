import numpy as np
import matplotlib.pyplot as plt
 
N = 300 #liczba osob na wyspie
C = 15 #początkowa liczba kokosów przypadająca na mieszkańca
T = 300000 #liczba gier

x = np.ones(N) * C #tworzę tablicę dla warunków początkowych --> 1 mieszkaniec - 15 kokosóW


for t in range(T):
    i, j = np.random.choice(N,2) #generuję losowo wybraną parę dwóch liczb (osób które grają w pnk)
    
    if x[j] > 0: #jeden warunek wystarczy - wyłącznie przypadek dla którego się odejmuje kokos
        x[i] += 1 
        x[j] -= 1

    
#y = 1/(1+C) * np.exp(-x/C+0.5)

plt.hist(x)

liczba_koko_na_mieszkanca = x.tolist()

y = []
for xi in range(len(liczba_koko_na_mieszkanca)):
    p = 1/(1+C) * np.exp(-xi/(C + 0.5))
    y.append(p)

plt.plot(x, y, 'r')
#plt.show()
plt.savefig('kokosy.png')
print("Zrobione!")
    
