from math import *

def kthombro(D,d,r):
    '''Toma como entrada la geometia del hombro y devuelve los valores de los 
    coeficientes geometricos para flexion y torsion.'''
    #Calcula el valor del parametro restante
    h=(D-d)/2.0
    #Respetando el rango de aplicacion de las ecuaciones
    if (r > 0 and h > 0) and r <= h:
        #Calculo del Kt segun Pilkey tabla 6-1
        if (h/r) >= 0.1 and (h/r) <=2.0:
            C1=0.947+1.206*(h/r)**(1.0/2)-0.131*(h/r)
            C2=0.022-3.405*(h/r)**(1.0/2)+0.915*(h/r)
            C3=0.869+1.777*(h/r)**(1.0/2)-0.555*(h/r)
            C4=-0.810+0.422*(h/r)**(1.0/2)-0.260*(h/r)
        elif (h/r) > 2.0 and (h/r) <=20.0:
            C1=1.232+0.832*(h/r)**(1.0/2)-0.008*(h/r)
            C2=-3.813+0.968*(h/r)**(1.0/2)-0.260*(h/r)
            C3=7.423-4.868*(h/r)**(1.0/2)+0.869*(h/r)
            C4=-3.839+3.070*(h/r)**(1.0/2)-0.600*(h/r)
        Kt = C1+C2*(2.0*h/D)+C3*(2.0*h/D)**2+\
                  C4*(2.0*h/D)**3
        #Calculo del Kts segun Pilkey tabla 6-1
        if (h/r) >= 0.25 and (h/r) <=4.0:
            C1=0.905+0.783*(h/r)**(1.0/2)-0.075*(h/r)
            C2=-0.437-1.969*(h/r)**(1.0/2)+0.553*(h/r)
            C3=1.557+1.073*(h/r)**(1.0/2)-0.578*(h/r)
            C4=-1.061+0.171*(h/r)**(1.0/2)+0.086*(h/r)
        Kts = C1+C2*(2.0*h/D)+C3*(2.0*h/D)**2+\
                   C4*(2.0*h/D)**3
    else: #Si se encuentra fuera del rango de aplicacion de las ecuaciones se usara
        #Kt y Kts para r/d=0.02 Shigley Tabla 7-1
        Kt=2.7
        Kts=2.2
    #Regresa los coeficientes de concentracion de esfuerzos geometricos a traccion y torsion y el parametro faltante
    return Kt, Kts, h

def kf(Kt,Kts,Sut,r):
    ''' Calcula los valores de los coeficientes de concentracion de esfuerzos 
    reducidos para fatiga tanto para flexion como para torsion a partir de los 
    coeficientes geometricos, la resistencia ultima a la traccion y el radio de 
    la muesca.'''
    Sut/=6.89 #Factor de conversion a kpsi
    #Calculo de las constantes de Neuber
    ra1=0.246-3.08e-3*Sut+1.51e-5*Sut**2-2.67e-8*Sut**3
    ra2=0.190-2.51e-3*Sut+1.35e-5*Sut**2-2.67e-8*Sut**3
    ra1*=sqrt(25.4)#Factor de conversion a raiz[mm]
    ra2*=sqrt(25.4)#Factor de conversion a raiz[mm]
    #Si el radio de la muesca es cero
    if r==0:
        Kf=Kt
        Kfs=Kts
    #Si el radio de entalle es diferente de cero
    else:
        Kf=1+(Kt-1)/(1+ra1/sqrt(r)) #Ec. de Neuber Shigley 6-33
        Kfs=1+(Kts-1)/(1+ra2/sqrt(r))
    #Regresa los coeficientes de concentracion de esfuerzos para fatiga a traccion y torsion
    return Kf, Kfs

'''
Kt=kthombro(25,20,2.5)[0]
Kts=kthombro(25,20,2.5)[1]

App.Console.PrintMessage('\nkthombro: '+str(Kt)+\
                          '\nktshombro: '+str(Kts))
'''
'''
Kf=kf(1.9,1.5,500,1)[0]
Kfs=kf(1.9,1.5,500,1)[1]
App.Console.PrintMessage('\nkfhombro: '+str(Kf)+\
                          '\nkfshombro: '+str(Kfs))

Kf=kf(1.9,1.5,500,0.5)[0]
Kfs=kf(1.9,1.5,500,0.5)[1]
App.Console.PrintMessage('\nkfcunero: '+str(Kf)+\
                          '\nkfscunero: '+str(Kfs))
'''