from math import *
import matplotlib
from matplotlib.patches import *
import numpy as np

def scrit(ax,Mxz,Mxy,T,Kt,Kts):
    ''' Genera un grafico en los ejes seleccionados calculando los esfuerzos ordinarios
    a partir de los momentos flectores y torsores obtenidos de los diagramas y los 
    coeficientes geometricos de concentracion de esfuerzos.'''
    #Configuracion de los ejes de ploteo
    ax.set_axis_off()
    ax.set_aspect('equal','datalim')
    #Calcula la magnitud total de los momentos
    Mtot=sqrt(Mxz**2+Mxy**2)
    #Calcula los esfuerzos ordinarios
    sigmax=Kt*32*Mtot/pi
    tauxz=Kts*16*T/pi
    
    if round(Mtot,2) != 0: #Si existe flexion
        #Encuentra los valores unitarios
        Mxz/=Mtot
        Mxy/=Mtot
        Mtot/=Mtot
        #Define los limites superior e inferior
        ax.set_xlim(-Mtot-0.2*Mtot,Mtot+0.2*Mtot)
        ax.set_ylim(-Mtot-0.2*Mtot,Mtot+0.2*Mtot)
        #Nombra y crea los ejes y, z
        ax.text(0.1*Mtot,1.1*Mtot,'y',fontsize=8)
        ax.text(-1.7*Mtot,-0.2*Mtot,'z',fontsize=8)
        ax.axvline(x=0,linewidth=0.5,color='k',dashes=[5,2,10,2])
        ax.axhline(y=0,linewidth=0.5,color='k',dashes=[5,2,10,2])
        #Crea recta de ubicacion de esfuerzos
        ax.plot([Mxy,-Mxy],[Mxz,-Mxz],'k-o', linewidth=0.6)
        #Crea una lista de patrones a dibujar
        ps=[]
        #Agrega un circulo
        ps.append(Circle((0, 0), Mtot,facecolor='white'))
        #Cambia la escala
        Mxy*=1.2
        Mxz*=1.2
        #Proyecciones
        ax.plot([0,-Mxz],[Mxy,Mxy],'k-', linewidth=0.4)
        ax.plot([-Mxz,-Mxz],[0,Mxy],'k-', linewidth=0.4)
        #Agrega la representacion visual de los Momentos
        ps.append(Arrow(0, 0, 0, Mxy, width=0.3, color='b'))
        ps.append(Arrow(0, 0, 0, 0.8*Mxy, width=0.3, color='b'))
        ps.append(Arrow(0, 0, -Mxz, 0, width=0.3, color='b'))
        ps.append(Arrow(0, 0, -0.8*Mxz, 0, width=0.3, color='b'))
        ps.append(Arrow(0, 0, -Mxz, Mxy, width=0.3, color='r'))
        ps.append(Arrow(0, 0, -0.8*Mxz, 0.8*Mxy, width=0.3, color='r'))
        #Muestra las figuras de la lista
        for p in ps:
            ax.add_patch(p)
        #Nombra los vectores de Momento Flector
        ax.text(0.1*Mxy,.8*Mxy,'My',fontsize=8,color='b')
        ax.text(-Mxz,-0.1*Mxz,'Mz',fontsize=8,color='b')
        ax.text(-1.1*Mxz, 1.1*Mxy,'Mtot',fontsize=8,color='r')
        #Lineas de ejes girados y', z'
        ax.plot([2*Mxy,-2*Mxy],[2*Mxz,-2*Mxz],'k--', linewidth=0.3) #y'
        ax.plot([-2*Mxz,2*Mxz],[2*Mxy,-2*Mxy],'k--', linewidth=0.3) #z'
        #Nombra los ejes girados y', z'
        ax.text(-1.2*Mxy,-1.2*Mxz,"y'",fontsize=8,color='k')
        ax.text(1.2*Mxz,-1.2*Mxy,"z'",fontsize=8,color='k')
        #Nombra los Puntos Criticos
        ax.text(-1*Mxy,-1*Mxz,'A',fontsize=9,color='k')
        ax.text(1*Mxy,1*Mxz,'B',fontsize=9,color='k')
    else:
        Mtot=1
        #Define los limites superior e inferior
        ax.set_xlim(-Mtot-0.2*Mtot,Mtot+0.2*Mtot)
        ax.set_ylim(-Mtot-0.2*Mtot,Mtot+0.2*Mtot)
        #Nombra y crea los ejes y, z
        ax.text(0.1*Mtot,1.1*Mtot,'y',fontsize=8)
        ax.text(-1.7*Mtot,-0.2*Mtot,'z',fontsize=8)
        ax.axvline(x=0,linewidth=0.5,color='k',dashes=[5,2,10,2])
        ax.axhline(y=0,linewidth=0.5,color='k',dashes=[5,2,10,2])
        #Crea una lista de patrones a dibujar
        ps=[]
        #Agrega un circulo
        ps.append(Circle((0, 0), Mtot,facecolor='white'))
        for p in ps:
            ax.add_patch(p)
        #Nombra los puntos maximos
        ax.text(-1,0,'Critico en toda \n la periferia',fontsize=8,color='b')

    #Retorna los esfuerzos ordinarios
    return sigmax, tauxz

def elementos(ax,sx,txz,s1,s2,t12,sT,phi):
    '''Como entrada necesita los ejes donde se va a graficar, los esfuerzos ordinarios
    y los esfuerzos principales y otras caracteristicas. Esta funcion esquematiza tres
    elementos de estado de esfuerzos.'''
    #Configura los ejes de ploteo
    ax.set_axis_off()
    ax.set_aspect('equal','datalim')
    ax.set_xlim(-9,9)
    ax.set_ylim(-3,3)
    ax.axhline(y=0,linewidth=0.5,color='k',dashes=[5,2,10,2])

    def elemento(X,Y=0,tau=0,sigmax=0,sigmay=0,rho=0):
        '''Funcion que crea la representacion de un elemento de esfuerzos'''
        #Convierte las unidades
        rhor=rho*pi/180
        #Calcula las coordenadas relativas
        x=X-sqrt(2)*sin(pi/4-rhor)
        y=Y-sqrt(2)*cos(pi/4-rhor)
        #Grafica eje x de coordenadas absolutas
        ax.plot([X,X],[-2,2],linewidth=0.5,color='k',dashes=[5,2,10,2])
        #ax.axvline(X,linewidth=0.5,color='k',dashes=[5,2,10,2])
        #Grafica ejes de coordenadas relativas
        ax.plot([X-3*cos(rhor),X+3*cos(rhor)],[Y-3*sin(rhor),Y+3*sin(rhor)],'k--', linewidth=0.3)
        ax.plot([X-3*sin(rhor),X+3*sin(rhor)],[Y+3*cos(rhor),Y-3*cos(rhor)],'k--', linewidth=0.3)

        #Crea una lista vacia de patrones a graficar
        ps=[]
        #Agrega a los patrones un rectangulo rotado
        ps.append(Rectangle((x, y), 2, 2, angle=rho, facecolor='white'))
        #Crea y agrega las flechas que representan a los esfuerzos
        if tau > 0:
            #Inferior
            ps.append(Arrow(x+0.2*sin(rhor),y-0.2*cos(rhor), 2*cos(rhor), 2*sin(rhor), width=0.3, color='b'))
            #Izquierda
            ps.append(Arrow(x-0.2*cos(rhor) ,y-0.2*sin(rhor) , -2*sin(rhor), 2*cos(rhor), width=0.3, color='b'))
            #Superior
            ps.append(Arrow(X+1*cos(rhor)-1.2*sin(rhor),Y+1*sin(rhor)+1.2*cos(rhor), -2*cos(rhor), -2*sin(rhor), width=0.3, color='b'))
            #Derecha
            ps.append(Arrow(X+1.2*cos(rhor)-1*sin(rhor),Y+1.2*sin(rhor)+1*cos(rhor), 2*sin(rhor), -2*cos(rhor), width=0.3, color='b'))
        elif tau < 0:
            #Inferior
            ps.append(Arrow(x+2*cos(rhor)+0.2*sin(rhor),y+2*sin(rhor)-0.2*cos(rhor), -2*cos(rhor), -2*sin(rhor), width=0.3, color='b'))
            #Izquierda
            ps.append(Arrow(x-2*sin(rhor)-0.2*cos(rhor),y+2*cos(rhor)-0.2*sin(rhor) , 2*sin(rhor), -2*cos(rhor), width=0.3, color='b'))
            #Superior
            ps.append(Arrow(x-2.2*sin(rhor),y+2.2*cos(rhor), 2*cos(rhor), 2*sin(rhor), width=0.3, color='b'))
            #Derecha
            ps.append(Arrow(x+2.2*cos(rhor),y+2.2*sin(rhor), -2*sin(rhor), 2*cos(rhor), width=0.3, color='b'))
        if sigmax > 0:
            #Derecha
            ps.append(Arrow(X+1.5*cos(rhor),Y+1.5*sin(rhor), cos(rhor), sin(rhor), width=0.5, color='b'))
            #Izquierda
            ps.append(Arrow(X-1.5*cos(rhor),Y-1.5*sin(rhor), -cos(rhor), -sin(rhor), width=0.5, color='b'))
        elif sigmax < 0:
            #Derecha
            ps.append(Arrow(X+2.5*cos(rhor),Y+2.5*sin(rhor), -cos(rhor), -sin(rhor), width=0.5, color='b'))
            #Izquierda
            ps.append(Arrow(X-2.5*cos(rhor),Y-2.5*sin(rhor), cos(rhor), sin(rhor), width=0.5, color='b'))
        if sigmay > 0:
            #Superior
            ps.append(Arrow(X-1.5*sin(rhor),Y+1.5*cos(rhor), -sin(rhor), cos(rhor), width=0.5, color='b'))
            #Inferior
            ps.append(Arrow(X+1.5*sin(rhor),Y-1.5*cos(rhor), sin(rhor), -cos(rhor), width=0.5, color='b'))
        elif sigmay < 0:
            ps.append(Arrow(X-2.5*sin(rhor),Y+2.5*cos(rhor), sin(rhor), -cos(rhor), width=0.5, color='b'))
            #Inferior
            ps.append(Arrow(X+2.5*sin(rhor),Y-2.5*cos(rhor), -sin(rhor), cos(rhor), width=0.5, color='b'))
        #Muestra cada patron en los ejes de ploteo
        for p in ps:
            ax.add_patch(p)
    #Crea un elemento en la coordenada establecida
    X=-6
    elemento(X,tau=txz,sigmax=sx)
    #Rotula como corresponde
    ax.text(X-.5,-0.5,'A',fontsize=15)
    ax.text(X+2,0.2,r'$\sigma_x$',fontsize=10,fontweight='bold')
    ax.text(X+1.1,1.1,r"$\tau_{xz'}$",fontsize=10,fontweight='bold')
    #Crea un elemento rotado en la coordenada establecida
    X=0
    phir=-phi*pi/180
    elemento(X, sigmax=s1, sigmay=s2, rho=-phi)
    #Rotula como corresponde
    ax.text(X+2.4*cos(phir),2.4*sin(phir),r'$\sigma_1$',fontsize=10,fontweight='bold')
    ax.text(X-2*sin(phir),+2*cos(phir),r'$\sigma_2$',fontsize=10,fontweight='bold')
    #Crea un elemento en la coordenada establecida con la rotacion adecuada
    X=6
    phir=(-phi+45)*pi/180
    elemento(X, tau=t12, sigmax=sT, sigmay=sT, rho=(-phi+45))
    #Rotula como corresponde
    ax.text(X+2.6*cos(phir),2.6*sin(phir),r'$\sigma_\tau$',fontsize=10,fontweight='bold')
    ax.text(X+cos(phir)-sin(phir),1.2*cos(phir)+sin(phir),r'$\tau_{1,2}$',fontsize=10,fontweight='bold')


def cmohr(ax,sx,txz):
    '''Realiza una figura del circulo de Mohr para el esfuerzo uniaxial en los ejes 
    seleccionados y calcula los esfuerzos principales y otras caracteristicas del mismo.'''
    #Configuracion de los ejes de ploteo
    ax.set_aspect('equal','datalim')
    #Calculo de valores principales
    t12=sqrt((sx/2.0)**2.0+txz**2.0)
    s1=sx/2+t12
    s2=sx/2-t12
    sT=sx/2
    if round(sx,2) != 0:
        phi=atan(txz/(sx/2))*180/pi/2
    else:
        phi=90/2
    #Crea y nombra los ejes sigma y tau
    ax.axvline(x=0,linewidth=0.7,color='k',dashes=[5,2,10,2])
    ax.axhline(y=0,linewidth=0.7,color='k',dashes=[5,2,10,2])
    ax.text(s1+.5*t12,-.18*t12,r'$\sigma$',fontsize=15,fontweight='bold')
    ax.text(-.13*t12,1*t12,r'$\tau$',fontsize=15,fontweight='bold')
    #Crea y nombra recta de ubicacion de esfuerzos
    ax.plot([sx,0],[txz,-txz],'k-o', linewidth=0.6)
    ax.text(1.1*sx,1.1*txz,'X',fontsize=9,color='k')
    ax.text(-0.1*sx,-1.1*txz,'Z',fontsize=9,color='k')
    #Proyecciones
    ax.plot([0,sx],[txz,txz],'k--', linewidth=0.3)
    ax.plot([sx,sx],[0,txz],'k--', linewidth=0.3)
    ax.text(sx,.5*txz,r"$\tau_{xz'}$",fontsize=8)
    ax.text(0.5*sx,txz+.1*txz,r"$\sigma_x$",fontsize=10)
    ax.text(0.65*sx,0.15*txz,r"$2\phi$",fontsize=10)
    #Agrega un circulo
    c=Circle((sx/2, 0), t12, facecolor='white')
    ax.add_patch(c)
    ax.set_xlim(s2-.5*t12,s1+.8*t12)
    ax.set_ylim(-1.25*t12,1.25*t12)
    #Rotula como corresponde
    ax.annotate(r'$\tau_1$', xy=(sT,t12),\
         xytext=(0,2), textcoords='offset points', size=11, ha='center',\
         va='bottom', bbox=dict(boxstyle='circle', fc='yellow',alpha=0.7))
    ax.annotate(r'$\tau_2$', xy=(sT,-t12),\
         xytext=(0,-12), textcoords='offset points', size=11, ha='center',\
         va='bottom', bbox=dict(boxstyle='circle', fc='yellow',alpha=0.7))
    ax.annotate(r'$\sigma_1$', xy=(s1,0),\
         xytext=(6,-4), textcoords='offset points', size=11, ha='center',\
         va='bottom', bbox=dict(boxstyle='circle', fc='yellow',alpha=0.7))
    ax.annotate(r'$\sigma_2$', xy=(s2,0),\
         xytext=(-6,-4), textcoords='offset points', size=11, ha='center',\
         va='bottom', bbox=dict(boxstyle='circle', fc='yellow',alpha=0.7))
    ax.annotate(r'$\sigma_\tau$', xy=(sT,0),\
         xytext=(0,-4), textcoords='offset points', size=11, ha='center',\
         va='bottom', bbox=dict(boxstyle='circle', fc='green',alpha=0.7))
    #Regresa los esfuerzos principales, el esfuerzo medio y el angulo phi
    return s1,s2,t12,sT,phi

def tfallaG(ax,s1,s2,MatProp):
    '''Usa los valores de los esfuerzos principales y las propiedades del material 
    para graficar las teorias de falla en los ejes elegidos.'''
    #Almacena en variables las propiedades del material
    Sut=float(MatProp[0])
    Sy=MatProp[1]
    Suc=MatProp[2]
    Syc=MatProp[1]
    #Configuracion de los ejes de ploteo
    #ax.set_axis_off()
    ax.set_aspect('equal','datalim')
    ax.axvline(x=0,linewidth=0.5,color='k',dashes=[5,2,10,2])
    ax.axhline(y=0,linewidth=0.5,color='k',dashes=[5,2,10,2])

    if Sy!='--': #Material Ductil
        Sy=float(Sy)
        Syc=float(Syc)
        #Rotula los ejes
        ax.text(1.5*Sut,.1*Sut,r"$\sigma_A$",fontsize=12,fontweight='bold')
        ax.text(.1*Sut,1.1*Sut,r"$\sigma_B$",fontsize=12,fontweight='bold')
        #Muestra y rotula la linea de carga
        LC=ax.plot([0,Sut],[0,Sut*s2/s1],'g-', linewidth=1.2)
        ax.text(0.8*Sut,1.4*Sut*s2/s1,\
                r"$\sigma_A = \frac{\sigma_2}{\sigma_1} \cdot \sigma_B$",\
                fontsize=8,fontweight='bold')
        #Configura los limites de los ejes
        ax.set_xlim(-2*Sut,2*Sut)
        ax.set_ylim(-2*Sut,2*Sut)
        #Etiqueta en la grafica algunas cantidades
        ax.text(1.1*Sy,.1*Sy,r"$Sy$",fontsize=10)
        ax.text(-1.5*Sy,.1*Sy,r"$-Sy$",fontsize=10)
        ax.text(-.4*Sy,Sy,r"$Sy$",fontsize=10)
        ax.text(.1*Sy,-Sy,r"$-Sy$",fontsize=10)
        #Grafica la curva de la teoria de ECM
        ECM=ax.plot([-Sy,0,Sy,Sy,0,-Sy,-Sy],\
                [0,Sy,Sy,0,-Sy,-Sy,0],'k-', linewidth=0.8)
        #Grafica la curva de la teoria de ED
        ED=Ellipse((0,0),(2*sqrt(2))*Sy, (2*sqrt(2.0/3))*Sy,
                     angle=45, linewidth=0.8, fill=False)
        ax.add_patch(ED)
        #Grafica la curva de la teoria de CMD
        CMD=ax.plot([-Syc,0,Sy,Sy,0,-Syc,-Syc],\
                [0,Sy,Sy,0,-Syc,-Syc,0],'k-', linewidth=0.8)
    else: #Material Fragil
        #Convierte a numero el valor de la resistencia
        Suc=float(Suc)
        #Rotula los ejes
        ax.text(2*Sut,.1*Sut,r"$\sigma_A$",fontsize=12,fontweight='bold')
        ax.text(.1*Sut,1.5*Sut,r"$\sigma_B$",fontsize=12,fontweight='bold')
        #Crea la linea de carga
        LC=ax.plot([0,(Sut+Suc)/2],[0,(Sut+Suc)*s2/(2*s1)],'g-', linewidth=1.2)
        ax.text(0.8*(Sut+Suc),1.4*(Sut+Suc)*s2/s1,\
                r"$\sigma_A = \frac{\sigma_2}{\sigma_1} \cdot \sigma_B$",\
                fontsize=8,fontweight='bold')
        #Establece el espacio de trabajo
        ax.set_xlim(-Suc-Sut,2*Sut)
        ax.set_ylim(-Suc-Sut,2*Sut)
        #Etiqueta algunos valores a mostrarse
        ax.text(1.1*Sut,.1*Sut,r"$Sut$",fontsize=10)
        ax.text(-1.4*Suc,.1*Sut,r"$-Suc$",fontsize=10)
        ax.text(-.4*Sut,Sut,r"$Sut$",fontsize=10)
        ax.text(.1*Sut,-1.3*Suc,r"$-Suc$",fontsize=10)
        #Grafica la curva de la teoria de ENM
        ENM = Rectangle((-Suc,-Suc),Sut+Suc,Sut+Suc,facecolor='white')
        ax.add_patch(ENM)
        #Grafica la curva de la teoria de CMF
        CMF = ax.plot([-Suc,0,Sut,Sut,0,-Suc,-Suc],\
                [0,Sut,Sut,0,-Suc,-Suc,0],'k-', linewidth=0.8)
        #Grafica la curva de la teoria de MM
        MM = ax.plot([-Suc,-Sut,Sut,Sut,0,-Suc,-Suc],\
                [0,Sut,Sut,-Sut,-Suc,-Suc,0],'k-', linewidth=0.8)

def dECM(sA,sB,Sy,n): #[cm]
    '''Calcula el diametro segun la teoria ECM y un factor de disenio.'''
    if (sA>=sB and sB>=0):
        d=(n*sA/Sy)**(1.0/3)
    elif (sA>=0 and 0>=sB):
        d=(n*(sA-sB)/Sy)**(1.0/3)
    elif (0>=sA and sA>=sB):
        d=(-n*sB/Sy)**(1.0/3)
    return d

def dED(sA,sB,Sy,n): #[cm]
    '''Calcula el diametro segun la teoria ED y un factor de disenio.'''
    svm=sqrt(sA**2-sA*sB+sB**2)
    d=(n*svm/Sy)**(1/3.0)
    return d

def dCM(sA,sB,St,Sc,n): #[cm]
    '''Calcula el diametro segun la teoria CM y un factor de disenio.'''
    if (sA>=sB and sB>=0):
        d=(n*sA/St)**(1.0/3)
    elif (sA>=0 and 0>=sB):
        d=(n*(sA/St-sB/Sc))**(1.0/3)
    elif (0>=sA and sA>=sB):
        d=(-n*sB/Sc)**(1.0/3)
    return d

def dENM(sA,sB,Sut,Suc,n): #[cm]
    '''Calcula el diametro segun la teoria ENM y un factor de disenio.'''
    if (sA>=sB and sB>=0)or(sA>=0 and 0>=sB and abs(sB/sA)<=Suc/Sut):
        d=(n*sA/Sut)**(1.0/3)
        return d
    elif (0>=sA and sA>=sB)or(sA>=0 and 0>=sB and abs(sB/sA)>Suc/Sut):
        d=(-n*sB/Suc)**(1.0/3)
        return d

def dMM(sA,sB,Sut,Suc,n): #[cm]
    '''Calcula el diametro segun la teoria MM y un factor de disenio.'''
    if (sA>=sB and sB>=0)or(sA>=0 and 0>=sB and abs(sB/sA)<=1):
        d=(n*sA/Sut)**(1.0/3)
        return d
    elif (0>=sA and sA>=sB)or(sA>=0 and 0>=sB and abs(sB/sA)>Suc/Sut):
        d=(-n*sB/Suc)**(1.0/3)
        return d
    elif (sA>=sB and sB>=0)or(sA>=0 and 0>=sB and abs(sB/sA)>1):
        d=(n*(Suc-Sut)*sB/(Suc*Sut)-sB/Suc)**(1.0/3)
        return d

'''
from PySide import QtCore, QtGui
from interfaz import Ui_Kt_Kts
class KtKts_Gui(QtGui.QDialog, Ui_Kt_Kts):
   def __init__(self, parent=None):
       QtGui.QDialog.__init__(self, parent)
       self.setupUi(self)
       self.graphics_Kt.setMinimumSize(QtCore.QSize(400, 400))
       self.ax=self.graphics_Kt.canvas.fig.add_axes([0.1,0.1,0.8,0.8])
       self.ax1=self.graphics_Kt.canvas.fig.add_axes([.15,.09,0.8,0.6])
       self.ax2=self.graphics_Kt.canvas.fig.add_axes([0.05,.6,0.9,0.5])
       self.show()

p=KtKts_Gui()
s1=80
s2=-520
MatProp=['200','--','550']

#TF='ECM'
#TF='ED'
#TF='CMD'
#TF='ENM'
#TF='CMF'
#TF='MM'

#tfallaG(ax,s1,s2,MatProp)
#p.ax.set_axis_off()
p.ax1.set_axis_off()
p.ax2.set_axis_off()
#tfallaG(p.ax,s1,s2,MatProp)


#scrit(ax,Mxz,Mxy,T,Kt,Kts) Sh Ejemplo 3-9
sc=scrit(p.ax2,-2800,-400,2000,1,1)
App.Console.PrintMessage('\nSigmax='+str(sc[0]/(1.5**3))+\
                         '\nTauxz='+str(sc[1]/(1.5**3)))
'''
'''
cm=cmohr(p.ax1,sc[0]/(1.5**3),sc[1]/(1.5**3))
App.Console.PrintMessage('\nSigma1='+str(cm[0])+\
                         '\nSigma2='+str(cm[1])+\
                         '\nTau12='+str(cm[2])+\
                         '\nSigmaTau='+str(cm[3])+\
                         '\nPhi='+str(cm[4]))
'''
'''
#cmohr(ax,sx,txz) Sh Ejemplo 3-4
p.ax.set_axis_off()
#p.ax1.set_axis_off()
p.ax2.set_axis_off()

sx=80
txz=50

cm=cmohr(p.ax1,sx,txz)
s1=cm[0]
s2=cm[1]
t12=cm[2]
sT=cm[3]
phi=cm[4]

elementos(p.ax2,sx,txz,s1,s2,t12,sT,phi)
App.Console.PrintMessage('\nSigma1='+str(s1)+\
                         '\nSigma2='+str(s2)+\
                         '\nTau12='+str(t12)+\
                         '\nSigmaTau='+str(sT)+\
                         '\nPhi='+str(phi))
'''
'''
s1=758479.5
s3=-7023.71
Sy=5694
n=2

sA=s1
sB=s3
St=4393.75
Sc=13181.25

Sut=St
Suc=Sc

App.Console.PrintMessage('\nECM: ' + str(dECM(s1,s3,Sy,n)))
App.Console.PrintMessage('\nED: ' + str(dED(s1,s3,Sy,n)))
App.Console.PrintMessage('\nCMD: ' + str(dCM(sA,sB,Sy,Sy,n)))
App.Console.PrintMessage('\nENM: ' + str(dENM(sA,sB,Sut,Suc,n)))
App.Console.PrintMessage('\nCMF: ' + str(dCM(sA,sB,St,Sc,n)))
App.Console.PrintMessage('\nMM: ' + str(dMM(sA,sB,Sut,Suc,n)))

App.Console.PrintMessage('\n\nECM: ' + str(dECM(70.0,70.0,100.0,1.43)))
App.Console.PrintMessage('\nED: ' + str(dED(70.0,70.0,100.0,1.43)))

App.Console.PrintMessage('\n\nECM: ' + str(dECM(70.0,30.0,100.0,1.43)))
App.Console.PrintMessage('\nED: ' + str(dED(70.0,30.0,100.0,1.65)))

App.Console.PrintMessage('\n\nECM: ' + str(dECM(70.0,-30.0,100.0,1)))
App.Console.PrintMessage('\nED: ' + str(ED(70.0,-30.0,100.0,1.13)))

App.Console.PrintMessage('\n\nECM: ' + str(dECM(-30.0,-70.0,100.0,1.43)))
App.Console.PrintMessage('\nED: ' + str(dED(-30.0,-70.0,100.0,1.65)))

App.Console.PrintMessage('\n\nENM: ' + str(dENM(50.0,50.0,62.5,187.5,1.25)))
App.Console.PrintMessage('\nCMF: ' + str(dCM(50.0,50.0,62.5,187.5,1.25)))
App.Console.PrintMessage('\nMM: ' + str(dMM(50.0,50.0,62.5,187.5,1.25)))

App.Console.PrintMessage('\n\nENM: ' + str(dENM(50.0,30.0,62.5,187.5,1.25)))
App.Console.PrintMessage('\nCMF: ' + str(dCM(50.0,30.0,62.5,187.5,1.25)))
App.Console.PrintMessage('\nMM: ' + str(dMM(50.0,30.0,62.5,187.5,1.25)))

App.Console.PrintMessage('\n\nENM: ' + str(dENM(50.0,-30.0,62.5,187.5,1.25)))
App.Console.PrintMessage('\nCMF: ' + str(dCM(50.0,-30.0,62.5,187.5,1.05)))
App.Console.PrintMessage('\nMM: ' + str(dMM(50.0,-30.0,62.5,187.5,1.25)))

App.Console.PrintMessage('\n\nENM: ' + str(dENM(-30.0,-50.0,62.5,187.5,3.75)))
App.Console.PrintMessage('\nCMF: ' + str(dCM(-30.0,-50.0,62.5,187.5,3.75)))
App.Console.PrintMessage('\nMM: ' + str(dMM(-30.0,-50.0,62.5,187.5,3.75)))
'''