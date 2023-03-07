import numpy as np
import matplotlib.pyplot as plt
 
N = 300 #liczba osob na wyspie
C = 15 #początkowa liczba kokosów przypadająca na mieszkańca
T = 300000 #liczba gier

x = np.ones(N) * C #tworzę tablicę dla warunków początkowych --> 1 mieszkaniec - 15 kokosóW

ludzie_bez_koko = []
nr_gry = []

for t in range(T):
    i, j = np.random.choice(N,2) #generuję losowo wybraną parę dwóch liczb (osób które grają w pnk)
    
    if x[j] > 0: #jeden warunek wystarczy - wyłącznie przypadek dla którego się odejmuje kokos
        x[i] += 1 
        x[j] -= 1
        liczba_koko_na_mieszkanca = x.tolist()
    y = 1/(1+C) * np.exp(-x/(C + 0.5))
#Wykreslanie wykresu liczby osob posiadających 0 kokosów od w funkcji liczby gier (np. co 1000 gier).

    if t %1000 == 0: #sprawdzam czy obecna gra jest wieokrotnoscią 1000
        n_zero = np.count_nonzero(liczba_koko_na_mieszkanca) #liczę ile jest liczb =/0
        n_zero = 300 - n_zero
        nr_gry.append(t)
        ludzie_bez_koko.append(n_zero)
        print('gra ', t)
        print('liczba ludzi bez kokosów:', n_zero)
    
    
plt.plot(nr_gry,ludzie_bez_koko,'r--')
plt.title("liczba osób posiadających zero kokosów w funkcji liczby gier")
plt.xlabel('numer gry ')
plt.ylabel('osoby bez kokosów')
plt.savefig('Zadanie_1B.png')
plt.show()



plt.hist(x, density=True)
#plt.show()


#y = []
#y = list(map(lambda xi: 1/(1+C) * np.exp(-xi/(C + 0.5)),liczba_koko_na_mieszkanca))
# =============================================================================
# for xi in liczba_koko_na_mieszkanca:
#     p = 1/(1+C) * np.exp(-xi/(C + 0.5))
#     y.append(p)
# =============================================================================

plt.plot(x, y, '.r')
plt.title("gęstosc prawdopodobienstwa w funkcji liczby posiadanach kokosów")
plt.xlabel('ludzie')
plt.ylabel('gęstosc prawdopodobieństwa posiadania danej liczby kokosów')
plt.savefig('Zadanie_1A.png')
plt.show()
    
