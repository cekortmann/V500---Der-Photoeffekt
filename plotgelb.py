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

U1,I1= np.genfromtxt('gelb.txt', unpack= True, skip_header=1, skip_footer=19)
U2,I2= np.genfromtxt('gelb.txt', unpack= True, skip_header=24)
def g(x,a,b):
    return a*x+b

def null(x):
    return 0*x

#plt.plot(-1.6649,0,'xg',linewidth = 2, label = r'U_b', alpha=1)
#plt.plot(xaxis, null(xaxis) ,'black',linewidth = 1, alpha=0.5)
#plt.plot(xx, g(xx, *para), 'orange', linewidth = 1, label = 'Ausgleichsfunktion', alpha=0.5)
plt.plot(U1, I1, 'xb', markersize=6 , label = 'Beschleunigung (V>0)', alpha=0.5)
plt.plot(U2, I2, 'xr', markersize=6 , label = 'Bremsung (V<0)', alpha=0.5)
plt.xlabel(r'$U \, / \, \mathrm{V}$')
plt.ylabel(r'$I \mathrm{/} \mathrm{pA} $')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
plt.savefig('build/plotgelb.pdf', bbox_inches = "tight")
plt.clf() 