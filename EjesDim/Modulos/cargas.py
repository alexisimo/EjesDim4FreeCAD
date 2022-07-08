from math import *
import numpy as np
from FreeCAD import Base
import Part, FreeCAD

class CargaPlana(object):
    '''Una clase que crea una Carga y sus funciones de
    singularidad para cortantes y momento flector en el
    plano.'''
    def __init__(self, tipo, magnitud, posicionXi,\
                 posicionXf=0,magnitudi=0):
        self.tipo = tipo
        self.m = magnitud
        self.posXi = posicionXi
        #Variables de clase para cargas distribuidas
        if self.tipo == "Carga Distribuida Constante":
            self.posXf = posicionXf
            self.mi = magnitud
        if self.tipo == "Carga Distribuida Lineal":
            self.posXf = posicionXf
            self.mi = magnitudi
            
    def __str__(self):  #Funcion para mostrar con la funcion print
        if self.tipo == "Carga Distribuida Constante":
                return ' m='+str(round(self.m,2))+\
                        ' Xi='+str(self.posXi)+'[m]'+\
                        ' Xf='+str(self.posXf)+'[m]'
                        
        elif self.tipo == "Carga Distribuida Lineal":
            return ' mi='+str(round(self.mi,2))+\
                        ' m='+str(round(self.m,2))+\
                        ' Xi='+str(self.posXi)+'[m]'+\
                        ' Xf='+str(self.posXf)+'[m]'
        else:
            return ' m='+str(round(self.m,2))+' Xi='+\
                        str(self.posXi)+'[m]'
    
    def __cmp__(self, other): #Comparador segun posXi
        if self.posXi < other.posXi:  
            return 1
        elif self.posXi > other.posXi:
            return -1
        else: 
            return 0              
   
    def V(self,x):
        '''Funcion de singularidad aplicado a la carga
        para el diagrama de cortantes.'''
        if self.tipo == "Fuerza Concentrada":
            V1 = -self.m
            V2 = 0
            return V1, V2
        
        elif self.tipo == "Momento Flector":
            V1 = 0
            V2 = 0
            return V1, V2
        
        elif self.tipo == "Carga Distribuida Constante" or\
             self.tipo == "Carga Distribuida Lineal":
            V1 = -((0.5)*((self.m-self.mi)/(self.posXf-self.posXi))*\
                     (x-self.posXi)**2+self.mi*(x-self.posXi))
            V2 = ((0.5)*((self.m-self.mi)/(self.posXf-self.posXi))*\
                     (x-self.posXf)**2+self.m*(x-self.posXf))
            return V1, V2
        
        else:
            return 0
    
      
    def M(self,x):
        '''Funcion de singularidad aplicado a la carga
        para el diagrama de momentos flectores.'''
        if self.tipo == "Fuerza Concentrada":
            M1 = -self.m*(x-self.posXi)
            M2 = 0
            return M1, M2
        
        elif self.tipo == "Momento Flector":
            M1 = -self.m
            M2 = 0
            return M1, M2
        
        elif self.tipo == "Carga Distribuida Constante" or\
             self.tipo == "Carga Distribuida Lineal":
            M1 = -(((1.0/6)*((self.m-self.mi)/(self.posXf-self.posXi))*\
                     (x-self.posXi)**3)+(0.5)*self.mi*(x-self.posXi)**2)
            M2 = ((1.0/6)*((self.m-self.mi)/(self.posXf-self.posXi))*\
                     (x-self.posXf)**3)+(0.5)*self.m*(x-self.posXf)**2
            return M1, M2
        else:
            return 0


    def T(self,x):
        '''Funcion de singularidad aplicado a la carga
        para el diagrama de momentos flectores.'''
        if self.tipo == "Momento Torsor":
            Mt1 = -self.m
            Mt2 = 0
            return Mt1, Mt2
        else:
            return 0
 
def reaccion(vectorCargas,l,XR1,XR2):
    '''Calcula las reacciones usando las cargas, la longitud del eje y la 
    ubicacion de los apoyos.'''
    #Inicializa los valores para iterar
    K1=0
    K2=0
    #Para cada carga toma los valores correspondientes y los suma a los factores K1 y K2
    for carga in vectorCargas:
        K1+=(carga.V(l)[0]+carga.V(l)[1])
        K2+=(carga.M(l)[0]+carga.M(l)[1])
    #Se aplica la formula correspondiente para encontrar las reacciones
    R1=(K1*(l-XR2)-K2)/(XR1-XR2)
    R2=K1-R1
    
    return R1, R2

def addCarga(vectorCargas, plano, tipo, magnitud, posicionXi,posicionXf=0,angulo=0,mi=0):
    '''Agrega el parametro angulo y descompone en el plano las cargas espaciales 
    agregando la carga a la lista de cargas que corresponde al plano seleccionado.'''
    #Segun el plano agrega la carga a la lista descomponiendola con el angulo de inclinacion
    if plano == "XY":
        vectorCargas.append(CargaPlana(tipo,magnitud*cos(angulo*pi/180),posicionXi,posicionXf,mi*cos(angulo*pi/180)))
    elif plano == "XZ":
        vectorCargas.append(CargaPlana(tipo,magnitud*sin(angulo*pi/180),posicionXi,posicionXf,mi*sin(angulo*pi/180)))
    else:
        pass

def diagCortantes(vectorX,vectorCargas):
    '''Para cada posicion a lo largo del eje y usando la lista completa de cargas 
    genera un vector con valores del cortante para graficar el diagrama de cortantes.'''
    #Inicializa un vector del mismo tamanio que el vectorX
    V=[0]*len(vectorX)
    #Para cada carga en el vector cargas
    for carga in vectorCargas:
        #Para cada punto a lo largo del eje
        for i in range(len(vectorX)):
            #Para cada componente de la funcion de singularidad V1 y V2
            for j in range(2):
                if j == 0: #Primer Componente
                    #Si la posicion analizada esta despues de la cota inicial
                    if vectorX[i]-carga.posXi > 0:
                        #Aporta a la distribucion de cortantes
                        V[i]+=carga.V(vectorX[i])[j]
                #Segundo componente solo influye en cargas distribuidas
                elif carga.tipo == "Carga Distribuida Constante" or\
                   carga.tipo == "Carga Distribuida Lineal":
                    #Si la posicion analizada esta despues de la cota inicial
                    if vectorX[i]-carga.posXf > 0:
                        #Aporta a la distribucion de cortantes
                        V[i]+=carga.V(vectorX[i])[j]
    #Regresa el vector calculado en cada x para el diagrama de cortantes
    return V

def diagMomentos(vectorX,vectorCargas):
    '''Calcula un vector para graficar el diagrama de momento flector en base a 
    un numero discreto de valores de x, y todas las cargas aplicadas usando las 
    funciones de singularidad.'''
    #Inicializa un vector del mismo tamanio que el vectorX
    M=[0]*len(vectorX)
    #Para cada carga en el vector cargas
    for carga in vectorCargas:
        #Para cada punto a lo largo del eje
        for i in range(len(vectorX)):
            #Para cada componente de la funcion de singularidad M1 y M2
            for j in range(2):
                if j == 0: #Primer componente
                    #Si la posicion analizada esta despues de la cota inicial
                    if vectorX[i]-carga.posXi > 0:
                        #Aporta a la distribucion de momentos
                        M[i]+=carga.M(vectorX[i])[j]
				#Segundo componente solo influye en cargas distribuidas
                elif carga.tipo == "Carga Distribuida Constante" or\
                   carga.tipo == "Carga Distribuida Lineal": 
                    #Si la posicion analizada esta despues de la cota final
                    if vectorX[i]-carga.posXf > 0:
                        #Aporta a la distribucion de momentos
                        M[i]+=carga.M(vectorX[i])[j]
    #Regresa el vector calculado en cada x para el diagrama de momentos
    return M

def diagTorsion(vectorX,vectorCargas):
    '''De la misma manera que las funciones anteriores calcula para cada punto a 
    lo largo del eje el valor correspondiente al torque listo para graficar el 
    diagrama de momentos torsores.'''
    #Inicializa un vector del mismo tamanio que el vectorX
    T=[0]*len(vectorX)
    #Para cada carga en el vector cargas
    for carga in vectorCargas:
        #Para cada punto a lo largo del eje
        for i in range(len(vectorX)):
            #Si la posicion analizada esta despues de la cota de la carga
            if vectorX[i]-carga.posXi > 0:
                #Aporta a la distribucion de momentos
                T[i]+=carga.T(vectorX[i])[0]
    #Regresa el vector calculado en cada x para el diagrama de momentos
    return T

def visualcargas(vCxy,vCxz,vCT,leje):
    '''Genera una representacion grafica tridimensional de las cargas y las regresa 
    como un objeto parte de FreeCAD. La funcion escala automaticamente las representaciones
    en funcion de la longitud del eje y tambien las caracteristicas de cada carga.'''
    def escala(m):
        '''Definicion de una funcion para establecer la escala'''
        #Cuando existe mas de una carga
        if len(vCxy)>1:
            #Crea una lista vacia para iterar
            mt=[]
            #Para cada carga agrega la magnitud total obtenida usando el teorema de Pitagoras con los componentes rectangulares
            for i in range(len(vCxy)):
                if vCxy[i].tipo=='Carga Distribuida Lineal':
                    mt.append(((vCxy[i].mi)**2.0+(vCxz[i].mi)**2.0)**(1/2.0))
                mt.append(((vCxy[i].m)**2.0+(vCxz[i].m)**2.0)**(1/2.0))
            #Interpola entre valores referenciales el valor de la escala
            l=(.15*leje*(m)+.01*leje*(max(mt)-m))/(max(mt))
        #En el caso de que tenga una sola carga
        elif len(vCxy)==1:
            #Si esa carga es distribuida lineal interpola una escala especial
            if vCxy[0].tipo=='Carga Distribuida Lineal':
                mt=[]
                mt.append(((vCxy[0].mi)**2.0+(vCxz[0].mi)**2.0)**(1/2.0))
                mt.append(((vCxy[0].m)**2.0+(vCxz[0].m)**2.0)**(1/2.0))
                l=(.15*leje*(m)+.01*leje*(max(mt)-m))/(max(mt))
            #En otro caso la escala es la maxima
            else:
                l=0.15*leje
        else:
            l=0.15*leje
        #Devuelve un factor de escala
        return l

    def flecha3D(posx,my,mz):
        '''Funcion para generar flechas 3D'''
        #Cambia las unidades a milimetros
        posx*=1000
        #Encuentra la magnitud total en funcion de las componentes
        mt=sqrt(my**2+mz**2)
        #Dimensiona la flecha usando la escala
        l=escala(mt)
        rcil=0.1*.15*leje
        h=0.55*.15*leje
        rcon=.19*.15*leje
        #Si la carga resultante es cero grafica una esfera pequenia
        if mt == 0:
            flecha=Part.makeSphere(0.25*l,Base.Vector(posx,0,0),Base.Vector(1,0,0))
            return flecha
        else: #Crea la flecha
            #Direccion
            dir=Base.Vector(0,my,mz)
            #Vector posicion
            pcil=Base.Vector(posx,h*(my/mt),h*(mz/mt))
            pcon=Base.Vector(posx,0,0)
            #Crea las geometrias primitivas cilindro y cono
            cil=Part.makeCylinder(rcil,l,pcil,dir)
            con=Part.makeCone(0,rcon,h,pcon,dir)
            #Une las partes
            flecha=cil.fuse(con)
            #Regresa un objeto flecha
            return flecha

    def flechaT3D(posx,m):
        '''Funcion para generar flechas de momentos torsores 3D'''
        #Cambia las unidades a milimetros
        posx*=1000
        #Establece la escala
        l=leje*0.6
        f=escala(m)
        #Dimensiones de la flecha        
        r1tor=0.11*l
        r2tor=r1tor/5
        h=r1tor/1.2
        rcon=2*r2tor
        #Toroide:
        #   Direccion
        dirtor=Base.Vector(1,0,0)
        #   Vector posicion
        ptor=Base.Vector(posx,0,0)
        #Cono:
        if m>0: #Cuando la magnitud es positiva la grafica de forma antioraria
        #   Direccion
            dircon=Base.Vector(0,0,-1)
        #   Vector posicion
            pcon=Base.Vector(posx,r1tor,h)
        else: #Magnitud negativa se grafica de forma horaria
        #   Direccion
            dircon=Base.Vector(0,-1,0)
        #   Vector posicion
            pcon=Base.Vector(posx,h,r1tor)
        #Crea las geometrias primitivas toroide y cono
        con=Part.makeCone(0,rcon,h,pcon,dircon)
        tor=Part.makeTorus(r1tor,r2tor,ptor,dirtor,0,360,270)
        #Une las partes para crear la flecha
        flecha=tor.fuse(con)
        return flecha

    def flechaM3D(posx,my,mz):
        '''Funcion para generar flechas de momentos flectores 3D'''
        #Calcula la magnitud total a partir de las componentes rectangulares
        m=sqrt(my**2+mz**2)
        #Ubica una flecha de momento torsor y la ubica en el lugar donde va la carga
        flecha=flechaT3D(posx,m)
        #Cambia las unidades a milimetros
        posx*=1000
        #Establece las cantidades necesarias para rotar la flecha
        #Centro de rotacion
        c=Base.Vector(posx,0,0)
        #Eje
        x=Base.Vector(1,0,0)
        y=Base.Vector(0,1,0)
        z=Base.Vector(0,0,1)
        #Direccion
        a=atan(mz/my)*180/pi
        #Segun el signo de la carga gira en el sentido adecuado
        if my>=0 and mz>=0:
            flecha.rotate(c,y,-90)
        else:
            flecha.rotate(c,y,90)
        flecha.rotate(c,z,30)
        flecha.rotate(c,x,a)
        #Retorna un objeto flecha
        return flecha
    #Inicializa un vector para iterar
    cargas3D=[]
    #Si hay cargas en el vector de cargas
    if len(vCxy)>0:
        #Para cada carga que producen flexion agrega la representacion grafica al vector inicializado
        for i in range(len(vCxy)):
            if vCxy[i].tipo == "Fuerza Concentrada":
                cargas3D.append(flecha3D(vCxy[i].posXi,\
                           vCxy[i].m,vCxz[i].m))

            elif vCxy[i].tipo == "Momento Flector":
                cargas3D.append(flechaM3D(vCxy[i].posXi,\
                           vCxy[i].m,vCxz[i].m))

            elif vCxy[i].tipo == "Carga Distribuida Constante":
                fdist=[]
                d=vCxy[i].posXf-vCxy[i].posXi
                for j in range(11):
                    fdist.append(flecha3D(vCxy[i].posXi+0.1*j*d,\
                                 vCxy[i].m,vCxz[i].m))
                dist=fdist[0]
                for k in range(len(fdist)-1):
		            dist=dist.fuse(fdist[k+1])

                cargas3D.append(dist)

            elif vCxy[i].tipo == "Carga Distribuida Lineal":
                fdistl=[]
                d=vCxy[i].posXf-vCxy[i].posXi
                mxy=(vCxy[i].m-vCxy[i].mi)
                mxz=(vCxz[i].m-vCxz[i].mi)

                for j in range(11):
                    fdistl.append(flecha3D(round(vCxy[i].posXi+0.1*j*d,2),\
                                           round(vCxy[i].mi+0.1*j*mxy,2),\
                                           round(vCxz[i].mi+0.1*j*mxz,2)))
                distl=fdistl[0]
                for k in range(len(fdistl)-1):
	                distl=distl.fuse(fdistl[k+1])

                cargas3D.append(distl)
    #Si hay cargas en el vector de cargas de torsion
    if len(vCT)>0:
        #Para cada carga que produce torsion agrega la representacion grafica al vector inicializado
        for i in range(len(vCT)):
            cargas3D.append(flechaT3D(vCT[i].posXi,vCT[i].m))

    #Fusiona las cargas respectivas
    if len(cargas3D)>1:
        cargas=cargas3D[0]
        for k in range(len(cargas3D)-1):
            cargas=cargas.fuse(cargas3D[k+1])
    elif len(cargas3D)==1:
        cargas=cargas3D[0]
    else:
        cargas=Part.makeSphere(1,Base.Vector(0,0,0),Base.Vector(1,0,0))
    #Devuelve un solido completo de todas las cargas
    return cargas

def vectorX(l):
    '''Genera un vector que toma un numero discreto de valores de x a lo largo del eje.'''
    '''
    l*=10
    n*=l/10
    paso=l/n
    x=range(int(l/paso)+2)
    for i in range(len(x)):
        x[i]*=paso
    '''
    #Usa la libreria numpy para generar un vector con valores entre los limites establecidos
    #x=np.linspace(-.001,l+.001,(l+.003)*1000)
    x=np.arange(round(-.001,4),round(l+.002,4),round(0.001,4))
    xn=[]
    for i in range(len(x)):
        xn.append(round(x[i],4))
    return xn


def indice(matriz,valor):
    '''Funcion que busca un valor en una matriz y retorna su indice.'''
    #Inicializa el valor i
    i=0
    #Para cada elemento en la matriz realiza la comprobacion con una tolerancia 
    for e in matriz:
        if abs(round(e,4)) == round(valor,4):
            break
        else:
            i+=1
    #Regresa el indice
    return i


'''
cargasXY=[CargaPlana("Fuerza Concentrada",950,0),\
          CargaPlana("Carga Distribuida Lineal",3000,.2,.6,-3000),\
          CargaPlana("Carga Distribuida Constante",-80,.6,.16),\
          CargaPlana("Momento Flector",500,.10)]
cargasXZ=[CargaPlana("Fuerza Concentrada",0,0),\
          CargaPlana("Carga Distribuida Lineal",4000,.1,.6,-4000),\
          CargaPlana("Carga Distribuida Constante",0,.6,.16),\
          CargaPlana("Momento Flector",500,.10)]

cargasXY=[CargaPlana("Fuerza Concentrada",950,.100),\
          CargaPlana("Fuerza Concentrada",-300,.500),\
          CargaPlana("Fuerza Concentrada",100,.800)]
cargasXZ=[CargaPlana("Fuerza Concentrada",950,.100),\
          CargaPlana("Fuerza Concentrada",400,.500),\
          CargaPlana("Fuerza Concentrada",0,.800)]

cargasXY=[CargaPlana("Carga Distribuida Lineal",600,.15,.6,-200),\
          CargaPlana("Fuerza Concentrada",0,1.0)]
cargasXZ=[CargaPlana("Carga Distribuida Lineal",0,.6,.15,0),\
          CargaPlana("Fuerza Concentrada",0,1.0)]


#cargasXY=[CargaPlana("Momento Flector",500,.400)]
#cargasXZ=[CargaPlana("Momento Flector",500,.400)]

#cargasXY=[]
#cargasXZ=[]

cargasT=[CargaPlana("Momento Torsor",-20,.400),\
        CargaPlana("Momento Torsor",500,.140)]

#cargasT=[]

cargas=visualcargas(cargasXY,cargasXZ,cargasT,800)

#Muestra las cargas
Part.show(cargas)

Gui.ActiveDocument.Shape.Selectable=False
Gui.ActiveDocument.Shape.DisplayMode='Shaded'
Gui.ActiveDocument.Shape.Transparency=40
Gui.ActiveDocument.Shape.ShapeColor=(0.00,0.33,1.00)
'''


'''
print "Problema Ejemplo 7-2 Shigley"
l = 11.5
XR1 = 0.75
XR2 = 10.75

cargasXY=[CargaPlana("Fuerza Concentrada",197.0,2.75),\
        CargaPlana("Fuerza Concentrada",885.0,8.5)]

Rxy = reaccion(cargasXY,l,XR1,XR2)
addCarga(cargasXY, "XZ", "Fuerza Concentrada",Rxy[0],XR1)
addCarga(cargasXY, "XZ", "Fuerza Concentrada",Rxy[1],XR2)

print 'XY: \n'
cargasXY.sort()
for carga in cargasXY:
    print carga


cargasXZ=[CargaPlana("Fuerza Concentrada",-540.0,2.75),\
        CargaPlana("Fuerza Concentrada",2431.0,8.5)]

Rxz = reaccion(cargasXZ,l,XR1,XR2)
addCarga(cargasXZ, "XZ", "Fuerza Concentrada",Rxz[0],XR1)
addCarga(cargasXZ, "XZ", "Fuerza Concentrada",Rxz[1],XR2)

print '\n XZ:  \n'
cargasXZ.sort()
for carga in cargasXZ:
    print carga


cargasT=[CargaPlana("Momento Torsor",-3240,2.75),\
        CargaPlana("Momento Torsor",3240,8.5)]

print '\n T:  \n'
cargasT.sort()
for carga in cargasT:
    print carga


x=vectorX(l,500)

Vxy=diagCortantes(x,cargasXY)
Mxy=diagMomentos(x,cargasXY)

Vxz=diagCortantes(x,cargasXZ)
Mxz=diagMomentos(x,cargasXZ)

T=diagTorsion(x,cargasT)

print Rxy, Rxz
print ' '

import Plot
Plot.plot(x,Vxz)
Plot.plot(x,Mxz)
Plot.plot(x,T)


print "Problema tipo 243 Meriam"
l = 3.0
XR1 = 0.0
XR2 = 2.5

cargas=[CargaPlana("Carga Distribuida Lineal",170.0,0,1),\
        CargaPlana("Carga Distribuida Constante",170.0,1,2),\
        CargaPlana("Fuerza Concentrada",150.0,3)]

R = reaccion(cargas,l,XR1,XR2)
addCarga(cargas, "XZ", "Fuerza Concentrada",R[0],XR1)
addCarga(cargas, "XZ", "Fuerza Concentrada",R[1],XR2)

cargas.sort()
for carga in cargas:
    print carga

x=vectorX(l)
V=diagCortantes(x,cargas)
M=diagMomentos(x,cargas)

print x
print V
print M
print ' '
'''
'''
print "Ejercicio 6-19 Hibbeler"
l = 15
XR1 = 5.0
XR2 = 15.0

cargas=[CargaPlana("Carga Distribuida Constante",2.0,0.0,5.0),\
        CargaPlana("Momento Flector",-30.0,10.0)]

R = reaccion(cargas,l,XR1,XR2)
addCarga(cargas, "XY", "Fuerza Concentrada",R[0],XR1)
addCarga(cargas, "XY", "Fuerza Concentrada",R[1],XR2)

cargas.sort()
for carga in cargas:
    print carga

x=vectorX(l)
V=diagCortantes(x,cargas)
M=diagMomentos(x,cargas)

import Plot
Plot.plot(x,V)
Plot.plot(x,M)

print x
print V
print M    
print ' '

print R
'''
'''
print "Ejercicio 12-52 Hibbeler"
l = 18
XR1 = 0
XR2 = 9

cargas=[CargaPlana("Carga Distribuida Lineal",0.8,0,9),\
              CargaPlana("Fuerza Concentrada",1.5,18)]

R = reaccion(cargas,l,XR1,XR2)
addCarga(cargas, "XZ", "Fuerza Concentrada",R[0],XR1)
addCarga(cargas, "XZ", "Fuerza Concentrada",R[1],XR2)

for carga in cargas:
    print carga

x=vectorX(l)
V=diagCortantes(x,cargas)
M=diagMomentos(x,cargas)

print x
print V
print M
print ' '


print "Problema tipo tesis"
l=5.5
XR1=0.0
XR2=3.5

cargas=[CargaPlana("Fuerza Concentrada",18.0,0.5),\
        CargaPlana("Carga Distribuida Lineal",9.0,1,3,6.0),\
        CargaPlana("Carga Distribuida Constante",5.0,3,4.5),\
        CargaPlana("Fuerza Concentrada",-2.0,5.0)]

R = reaccion(cargas,l,XR1,XR2)
addCarga(cargas, "XZ", "Fuerza Concentrada",R[0],XR1)
addCarga(cargas, "XZ", "Fuerza Concentrada",R[1],XR2)

cargas.sort()
for carga in cargas:
    print carga

x=vectorX(l)
V=diagCortantes(x,cargas)
M=diagMomentos(x,cargas)

print x
print V
print M
print ' '

print "Problema tipo tesis1"
l=5.0
XR1=1.0
XR2=4.0

cargas=[CargaPlana("Carga Distribuida Constante",2.0,0.0,1.0),\
        CargaPlana("Carga Distribuida Lineal",6.0,1.0,4.0,2.0),\
        CargaPlana("Carga Distribuida Constante",2.0,4.0,5.0),\
        CargaPlana("Carga Distribuida Lineal",0.0,2.0,3.5,-3.0)]

R = reaccion(cargas,l,XR1,XR2)
addCarga(cargas, "XZ", "Fuerza Concentrada",R[0],XR1)
addCarga(cargas, "XZ", "Fuerza Concentrada",R[1],XR2)

cargas.sort()
for carga in cargas:
    print carga

x=vectorX(l)
V=diagCortantes(x,cargas)
M=diagMomentos(x,cargas)

print x
print V
print M
print ' '
'''

