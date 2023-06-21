import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  

lam, nu, Ug= np.genfromtxt('frequenz.txt', unpack= True, skip_header=1)
lam2, nu2, Ug2= np.genfromtxt('frequenz2.txt', unpack= True, skip_header=1)

def g(x,a,b):
    return a*x+b

def null(x):
    return 0*x

para,pcov =curve_fit(g,nu,Ug)#,p0=[1,mean,sigma])
a,b = para
pcov = np.sqrt(np.diag(pcov))
fa, fb = pcov
ua = ufloat(a, fa) 
ub = ufloat(b, fb)

xx= np.linspace(0,9,1000)

print('ua','Result= {:.4u}'.format(ua))
print('ub','Result= {:.4u}'.format(ub))

plt.plot(xx, g(xx, *para), 'orange', linewidth = 1, label = 'Ausgleichsfunktion', alpha=0.5)
plt.plot(nu, Ug, 'xb', markersize=6 , label = 'Grenzspannungen', alpha=0.5)
plt.xlabel(r'$\nu \, / \, \mathrm{10^{14} Hz}$')
plt.ylabel(r'$U_{g} \mathrm{/} \mathrm{V} $')
plt.xlim(0,9)
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
plt.savefig('build/frequenz.pdf', bbox_inches = "tight")
plt.clf() 