# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np 
import pylab as pl

f=600 # FREQUENCE DU SON 
w=2*np.pi*f  
fe=80000  #FREQUENCE D'ECHANTILLONNAGE
Te=1/fe
A=4 #amplitude max detectable en volt ou le nombre d'harmonique du son
a=2*A+0.2

'On défini le son comme une somme de cos'
def son(t):
    return (np.cos(w*t)+np.cos(1.3*w*t)+np.cos(4*w*t)+np.cos(6*w*t))    

'On conscruit le signal en dent de scie'    
def scie(t):
    p=t//Te
    y=(a/Te)*t-p*a-a/2
    return(y)

'On compare nos deux signaux pour construire la mli' 
def comparateur(t):
    h=0
    if scie(t)>son(t):
        h=1
    else:
        h=-1
    return(h) 
        
u=0.00000001  #probleme de demarrage du comparateur

'Temps que le signal mli(rouge) reste négatif à la ième période'
def temps(i): 
    e=0
    T = np.linspace((Te*i)+u,Te*(i+1),5000)
    for t in T:
       if comparateur(t)<=0:
            e=t-Te*i
       else:
            return((e/Te)*100)
    return ((e/Te)*100)
    
"Enfin on reconstruit le signal audio à l'aide uniquement du comparateur"
def reconstruction(n):   #renvoie une liste des ordonnées des points de reconstruction
    R=[]
    for j in range(n):
        if temps(j)<50:
            R.append((a/2)*(-(50-temps(j)%50))/50)
        else:
            R.append((a/2)*(temps(j)%50)/50)
    return(R)    

"OBSERVATION GRAPHIQUE"

"On définit l'intervalle de temps [c,b] d'observation "
c=0
b=0.001

T = np.linspace(c,b,(b-c)/Te*1000)  
    
X = [son(t) for t in T] #bleu
Y = [scie(k) for k in T] #vert
Z = [comparateur(j) for j in T] #rouge

H = np.linspace(0,(b-c),(b-c)/Te)
L = reconstruction(len(H))

pl.plot(T,X)
pl.plot(T,Y)
pl.plot(T,Z,"r")
pl.plot(H,L,"m")
pl.show()