from math import *
from cargas import indice 
import numpy as np

def tpref(t):
    ''' Toma el tamanio calculado con todos su decimales y lo aproxima al inmediato 
    superior de la serie de Renard. '''
    #Numeros de cuarta opcion de Renard
    R40=[1, 1.06, 1.12, 1.18, 1.25, 1.32, 1.4, 1.5,\
         1.6, 1.7, 1.8, 1.9, 2, 2.12, 2.24, 2.36, 2.5,\
         2.65, 2.8, 3, 3.15, 3.35, 3.55, 3.75, 4, 4.25,\
         4.5, 4.75, 5, 5.3, 5.6, 6, 6.3, 6.7, 7.1, 7.5,\
         8, 8.5, 9, 9.5, 10]
    #Verifica el orden del numero ingresado
    for i in range(len(R40)-1):
        if t>R40[i] and t<R40[i+1]:
           t=R40[i+1]
        elif t>R40[i]*10 and t<R40[i+1]*10:
           t=R40[i+1]*10
        elif t>R40[i]*100 and t<R40[i+1]*100:
           t=R40[i+1]*100
    return t


def secpref(VSec,xcrit,d):
    ''' Para cada seccion del eje aplica la funcion anterior manteniendo las proporciones
    del eje tomando como la mayor la seccion critica y su diametro. '''
    #Si existen secciones
    if len(VSec)>0:
        #Prepara para iterar
        dsecs=[]
        lsecs=[]
        s=0 
        #Extrae los diametros y la suma de las longitudes o cambios de seccion
        for sec in VSec:
            dsecs.append(2*round(sec.r,3))
            s+=round(sec.l,3)
            lsecs.append(s)
        #Verifica si se encuentra el punto critico en los cambios de seccion
        if round(xcrit,3) in lsecs:
            i = indice(lsecs,round(xcrit,3))
            #Extrae el indice de la seccion con menor diametro
            if dsecs[i]<dsecs[i+1]:
                ind=i
            else:
                ind=i+1
        else:
            ind=0
        #Para la seccion y el diametro criticos cambia los
        #valores de los objetos seccion
        ds=dsecs[ind]
        for i in range(len(dsecs)):
            dsecs[i]=tpref((dsecs[i]/ds)*tpref(d))
        #VSec[i].r=dsecs[i]/2.0
        return dsecs
    else:
        return d

'''
from secciones import Seccion
secs=[Seccion(18,100),Seccion(20,200),Seccion(25,400),Seccion(22,200),Seccion(20,100)]
print secpref(secs,700,68.456)

    

d=68.94
#d=108.541354
#d=8.8372

dcorr=tpref(d) #71
App.Console.PrintMessage(dcorr)

#http://www.dailymotion.com/video/x1hsefd_pqam-124_shortfilms
'''