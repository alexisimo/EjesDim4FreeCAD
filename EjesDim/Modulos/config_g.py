import Part
from FreeCAD import Base
from math import *

class Seccion(object):
	'''Una clase que crea una Seccion cilindrica.'''
	def __init__(self, radio, longitud):
		self.r = radio
		self.l = longitud

	def __str__(self): #Funcion para mostrar con print
		return 'd='+str(self.r*2)+'[mm]'+\
				'  l='+str(self.l)+'[mm]'

def addseccion(vectorSecciones,radio, longitud):
	'''Metodo para agregar al vectorSecciones una Seccion con su radio y longitud'''
	vectorSecciones.append(Seccion(radio, longitud))

def unirsecciones(vectorSecciones):
	'''Metodo para unir las secciones consecutivas del vectorSecciones y crear un solo eje solido'''
	#Direccion x
	dir=Base.Vector(1,0,0)
	#Posicion en x
	x=0
	vectorCilindros=[]
	for seccion in vectorSecciones:
		#Vector posicion
		vx=Base.Vector(x,0,0)
		x+=seccion.l
		#Creacion de cilindro
		vectorCilindros.append(Part.makeCylinder( seccion.r,seccion.l,vx,dir))
	
	eje=vectorCilindros[0]
	
	for i in range(len(vectorCilindros)-1):
		eje=eje.fuse(vectorCilindros[i+1])
	return eje

def r_deacuerdo(eje,r):
	'''Metodo para crear un radio en todos los vertices internos del eje con un radio r'''
	#Para cada arista circular comprueba la validez del radio de entalle
	for i in range(len(cambiosecc(eje)[0])-1):
        #Verifica si son entidades concentricas
		if cambiosecc(eje)[0][i].CenterOfMass == cambiosecc(eje)[0][i+1].CenterOfMass:
            #Verifica que entidad tiene mayor diametro
			if cambiosecc(eje)[0][i].Length < cambiosecc(eje)[0][i+1].Length:
				#Comprueba el radio de entalle
				if round((cambiosecc(eje)[0][i+1].Length - cambiosecc(eje)[0][i].Length)/(2*pi),2) > r:
					#Toma los cambios de seccion circulares menores
					edges=cambiosecc(eje)[2]
					#Crea un radio de entalle en todos los vertices encontrados
					eje = eje.makeFillet(r,edges)
					return eje, r
				else:
					r=0.0
					return eje, r
			else:
				#Comprueba el radio de entalle
				if round((cambiosecc(eje)[0][i].Length - cambiosecc(eje)[0][i+1].Length)/(2*pi),2) > r:
					#Toma los cambios de seccion circulares menores
					edges=cambiosecc(eje)[2]
					#Crea un radio de entalle en todos los vertices encontrados
					eje = eje.makeFillet(r,edges)
					return eje, r
				else:
					r=0.0
					return eje, r

def cambiosecc(eje):
	'''Metodo para encontrar los cambios de seccion del eje'''
	#Inicializa un vector para colocar los cambios de seccion
	edges=[]
	xedges=[]
	edgesr=[]
	#Para cada arista del eje si el centro de masa se encuentra en el eje x
	for i in range(len(eje.Edges)):
		if round(eje.Edges[i].CenterOfMass[1],2) == 0 and\
				round(eje.Edges[i].CenterOfMass[2],2) == 0:
			#Anade la ubicacion x de la arista al vector ubicacion x de aristas 
			xedges.append(round(eje.Edges[i].CenterOfMass[0],3))
	#Ordena y elimina tanto la ubicacion de la arista inicial como la final
	xedges.sort()
	xedges.pop(0)
	xedges.pop(-1)
	#Para cada arista en el vector aristas
	for	i in range(len(eje.Edges)):
		#Si el centro de masa esta en el vector de ubicacion x de aristas
		if round(eje.Edges[i].CenterOfMass[0],3) in xedges:
			#Anade la arista al vector aristas
			edges.append(eje.Edges[i])
	#Para cada arista compara con la siguiente y la anade a un vector nuevo la de menor D
	for	i in range(len(edges)-1):
		if edges[i].CenterOfMass == edges[i+1].CenterOfMass:
			if edges[i].Length < edges[i+1].Length:
					edgesr.append(edges[i])
			else:
					edgesr.append(edges[i+1])
	#Regresa todas las aristas, la ubicacion x de las aristas y las que aplica r
	return edges, xedges, edgesr

def visualapoyos(XR1,XR2,leje):
    '''Produce una representacion visual en 3D de los apoyos del eje 
    tomando la ubicacion de los mismos y la longitud total del eje para escalarlos.'''
    #Prepara la escala
    l=0.05*leje
    #Establece los valores a usar de la figura geometrica 3D
    xmin=0
    ymin=0
    zmin=0
    z2min=l
    x2min=l
    
    xmax=2*l
    ymax=2*l
    zmax=2*l
    z2max=l
    x2max=l
    #Genera vectores base para ubicar las geometrias
    pnt1=Base.Vector(XR1-l,-2*l,-l)
    pnt2=Base.Vector(XR2-l,-2*l+.4*l,-l)
    pnt3=Base.Vector(XR2-l,-2*l,-l)
    dir=Base.Vector(0,1,0)
    #Crea los solidos de los apoyos
    w1=Part.makeWedge(xmin,ymin,zmin,z2min,x2min,\
                     xmax,ymax,zmax,z2max,x2max,\
                     pnt1)

    w2=Part.makeWedge(xmin,ymin,zmin,z2min,x2min,\
                     xmax,ymax-.4*l,zmax,z2max,x2max,\
                     pnt2)
    b2= Part.makeBox(2*l,2*l,l*.2,pnt3,dir)
    w2=w2.fuse(b2)
    apoyos=w1.fuse(w2)

    return apoyos


'''
VS=[]

#Parametros Seccion 1
addseccion(VS, 10, 30)
#Parametros Seccion 2
addseccion(VS, 15, 60)
#Parametros Seccion 3
addseccion(VS, 20, 80)
#Parametros Seccion 4
addseccion(VS, 15, 40)
#Parametros Seccion 5
addseccion(VS, 10, 30)

eje=unirsecciones(VS)
App.Console.PrintMessage('\nedges'+str(cambiosecc(eje)[0])+"\n") 
App.Console.PrintMessage('\nxedges'+str(cambiosecc(eje)[1])+"\n") 
App.Console.PrintMessage('\nedgesr'+str(cambiosecc(eje)[2])+"\n") 
eje=r_deacuerdo(eje,3)[0]
Part.show(eje)
'''