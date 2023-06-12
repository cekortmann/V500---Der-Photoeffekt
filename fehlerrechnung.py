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

def Nulls(a,b):
    return -b/a

uarot= ufloat(4.18,0.33)
ubrot= ufloat(3.41,0.06)
uagruen= ufloat(34.5,1.4)
ubgruen= ufloat(23.9,0.5)
ualila= ufloat(0.799,0.026)
ublila= ufloat(0.976,0.015)
uagelb= ufloat(91.35,11.55)
ubgelb= ufloat(77,8.35)

print('Nullstelle rot',Nulls(uarot,ubrot))
print('Nullstelle gruen',Nulls(uagruen,ubgruen))
print('Nullstelle lila',Nulls(ualila,ublila))
#print('Nullstelle gelb',Nulls(uagelb,ubgelb))