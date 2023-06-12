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

U1,I1= np.genfromtxt('lila.txt', unpack= True, skip_header=1, skip_footer=25)
U2,I2= np.genfromtxt('lila.txt', unpack= True, skip_header=22, skip_footer=8)
U3,I3= np.genfromtxt('lila3.txt', unpack= True, skip_header=1, skip_footer=0)
def g(x,a,b):
    return a*x+b

def null(x):
    return 0*x

para,pcov =curve_fit(g,U3,sqrt(I3))#,p0=[1,mean,sigma])
a,b = para
pcov = np.sqrt(np.diag(pcov))
fa, fb = pcov
ua = ufloat(a, fa) 
ub = ufloat(b, fb)

xx= np.linspace(-1.4,0.5,100)
xaxis=np.linspace(-2,2,10)

print('ua',ua)
print('ub',ub)
plt.plot(-1.2215,0,'xg',linewidth = 2, label = r'U_g', alpha=1)
plt.plot(xaxis, null(xaxis) ,'black',linewidth = 1, alpha=0.5)
plt.plot(xx, g(xx, *para), 'orange', linewidth = 1, label = 'Ausgleichsfunktion', alpha=0.5)
plt.plot(U1, sqrt(I1), 'xb', markersize=6 , label = 'Beschleunigung (V>0)', alpha=0.5)
plt.plot(U2, (I2)**(1/2), 'xr', markersize=6 , label = 'Bremsung (V<0)', alpha=0.5)
plt.xlabel(r'$U \, / \, \mathrm{V}$')
plt.ylabel(r'$\sqrt{I} \mathrm{/} \mathrm{nA}^{1/2} $')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
plt.savefig('build/plotlila.pdf', bbox_inches = "tight")
plt.clf() 