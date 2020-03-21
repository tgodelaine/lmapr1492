#!/usr/bin/env python
# coding: utf-8

# In[32]:


from pymatgen.ext.matproj import MPRester
from pymatgen.io.cif import CifWriter
#import numpy as np
#import scipy as sc
#from matplotlib import pyplot as plt
from pymatgen.analysis.diffraction.xrd import XRDCalculator

with MPRester("NrRTCZ9vfEUg8SJu") as m:
    #Téléchargement du fichier
    structure = m.get_structure_by_material_id("mp-12908")
    w = CifWriter(structure)
    w.write_file('ScAgSe2_mp-12908_symmetrized.cif')

#https://pymatgen.org/pymatgen.analysis.diffraction.xrd.html#module-pymatgen.analysis.diffraction.xrd
xdr = XRDCalculator(wavelength='CuKa',symprec=0,debye_waller_factors=None)
#Permet d'obtenir les intensités correspondantes aux pics.
a = xdr.get_pattern(structure,scaled=True,two_theta_range=([0,90]))
#Permet d'obtenir le graphe de l'intensité en fonction de 2\theta. Il renvoie également les indices hkl associés.
#Ici il renvoie les indices hkil, la maille étant hexagonale.
b = xdr.get_plot(structure,two_theta_range=([0,90]),annotate_peaks=True,ax=None, with_labels=True)
#x = [13.33914255,26.21090972,26.86345387,29.51860285,37.88356846,40.78260924,46.24922249,48.35262197,49.12828178,53.93539199,54.29523176,55.36519006,55.82526418,61.26344143,62.25624736,63.33865294,69.76383562,71.00188265,73.72666441,74.93785358,75.3305901,77.13166499,80.07808178,80.96482021,85.72356597,87.27226023,87.85587233,88.35117783,89.02248977]
#y = [8.16264303e+00,1.47390815e+01,5.69618794e-03,8.69990232e+01,1.00000000e+02,3.58323938e+00,4.95099927e+01,2.20873455e+00,1.55300185e+01,1.71817667e+00,1.71129594e-03,8.48753939e+00,1.40218835e+01,2.28693912e+01,4.12539548e+00,5.70605662e+00,5.37196876e+00,1.50215291e-02,1.21322659e+00,2.02144849e+01,1.15485465e+01,5.66690324e+00,2.07961162e+01,1.87785822e+00,8.05861515e+00,4.25847861e-01,6.05537176e+00,1.65204973e-02,4.57731164e-02]
#plt.plot(x,y,'|')
#plt.show()
#print(x,y)


# In[34]:


#Les intensités des différents pics et les indices hkil associés sont donc :
Intensites = [8.16264303e+00,1.47390815e+01,5.69618794e-03]
Angle = [13.33914255,26.21090972,26.86345387]
Indices = [[0,0,0,1],[1,0,-1,0],[0,0,0,2]]
print(Intensites)
print(Angle)
print(Indices)


# In[ ]:




