from PySide import QtCore, QtGui
from math import *
import matplotlib
from matplotlib.patches import *
import numpy as np

def fluct(axs,axt,Mcrit,Tcrit,Kf,Kfs):
    '''Calcula los esfuerzos medios y amplitud tanto cortantes como normales y plotea
    en los ejes seleccionados una representacion grafica de los esfuerzos fluctuantes
    presentes en el eje diseniado.'''
    #Calculo de esfuerzos amplitud y medio
    sigmaa=Kf*32*Mcrit/(pi) #/d**3
    taum=Kfs*16*Tcrit/(pi) #/d**3
    #Prepara los ejes para plotear
    #axs.set_aspect('equal','datalim')
    axs.set_xlim(-0.2,4)
    axs.set_ylim(-1.2,1.2)
    #axt.set_aspect('equal','datalim')
    axt.set_xlim(-0.2,2)
    axt.set_ylim(-0.7,1.7)
    #Desactiva la etiqueta de los ejes
    axs.xaxis.set_visible(False)
    axs.yaxis.set_visible(False)
    axt.xaxis.set_visible(False)
    axt.yaxis.set_visible(False)
    #Para un valor de momento critico valido
    if round(Mcrit, 2) != 0:
        #Crea los ejes x, y
        axs.axhline(y=0,linewidth=0.6,color='k',dashes=[5,2,10,2])
        axs.axvline(x=0,linewidth=0.6,color='k',dashes=[5,2,10,2])
        #Funcion senoidal para el Esfuerzo Normal
        x=np.linspace(0, 10, 1000)
        y=np.sin(2*np.pi*x/2)
        axs.plot(x, y,'b',lw=1.2)
        #Agrega texto en los graficos
        axs.text(-.1,0.8,r'$\sigma$',fontsize=10)
        axs.text(3.7,-0.15,r'$t$',fontsize=10)
        axs.text(0.45,0.45,r'$\sigma_a$',fontsize=8,fontweight='bold')
        axs.text(1.2,0.1,r'$\sigma_m=0$',fontsize=8,fontweight='bold')
        #Grafica flechas de cota
        ps=[]
        ps.append(Arrow(0.5, 0.6, 0, 0.4, lw=0.3, width=0.05, color='k'))
        ps.append(Arrow(0.5, 0.4, 0, -0.4, lw=0.3, width=0.05, color='k'))
        for p in ps:
            axs.add_patch(p)
    #Para un valor de momento de torsion critico valido
    if round(Tcrit, 2) != 0:
        #Crea los ejes x, y
        axt.axvline(x=0,linewidth=0.6,color='k',dashes=[5,2,10,2])
        axt.axvline(x=0,linewidth=0.6,color='k',dashes=[5,2,10,2])
        #Funcion constante para el Esfuerzo Cortante
        axt.plot([0,30],[0.8,0.8],'r',lw=1.2)
        axt.text(-.1,1.2,r'$\tau$',fontsize=10)
        axt.text(3.7,-0.15,r'$t$',fontsize=10)
        axt.text(0.45,0.35,r'$\tau_m$',fontsize=8,fontweight='bold')
        axt.text(1.4,0.9,r'$\tau_a=0$',fontsize=8,fontweight='bold')
        #Grafica flechas de cota
        ps1=[]
        ps1.append(Arrow(0.5, 0.53, 0, 0.25, lw=0.3, width=0.05, color='k'))
        ps1.append(Arrow(0.5, 0.25, 0, -0.25, lw=0.3, width=0.05, color='k'))
        for p in ps1:
            axt.add_patch(p)
    #Retorna los esfuerzos calculados
    return sigmaa, taum


def calc_ka(acabado,Sut): #Tabla 6-2 Shigley
    '''Calcula el coeficiente modificador de la resistencia a la fatiga 
    de acabado superficial'''
    #ka - Factor de Superficie
    Sut=float(Sut)
    if acabado=='Esmerilado':
        a=1.58
        b=-0.085
    elif acabado=='Maquinado o Laminado en Frio':
        a=4.51
        b=-0.265
    elif acabado=='Laminado en Caliente':
        a=57.7
        b=-0.718
    elif acabado=='Como sale de la Forja':
        a=272.0
        b=-0.995
    ka=a*Sut**b

    return ka

def calc_kb(d):
    '''Calcula el coeficiente modificador de la resistencia a la fatiga 
    de tamanio'''
    #kb - Factor de Tamanio
    if d>=2.79 and d<=51.0:
        kb=1.24*d**-.107
    elif d>51 and d<=254.0:
        kb=1.51*d**-.157
    else:
        kb=0
    return kb

def calc_kc(carga):
    '''Calcula el coeficiente modificador de la resistencia a la fatiga 
    de carga'''
    #kc - Factor de Carga
    if carga=='Flexion':
        QtGui.QMessageBox.information(None,"kc-Factor de Carga",\
             'El eje se encuentra sometido a cargas combinadas:'+\
                                '\nkc=1')
        kc=1.0
    elif carga=='Torsion Pura':
        QtGui.QMessageBox.information(None,"kc-Factor de Carga",\
               'El eje se encuentra sometido a Torsion Pura:'+\
                                 '\nkc=0.59')
        kc=0.59
    return kc

def calc_kd(T):
    '''Calcula el coeficiente modificador de la resistencia a la fatiga 
    de acabado superficial'''
    #kd - Factor de Temperatura
    if T>20 and T<=500:
        TF=(9.0/5)*T+32
        kd=.975+.432e-3*TF-.115e-5*TF**2+.104e-8*TF**3-.595e-12*TF**4
    elif T==20:
        kd=1
    else:
        kd=0
    return kd

def calc_ke(confiabilidad):
    '''Calcula el coeficiente modificador de la resistencia a la fatiga 
    de confiabilidad'''
    #ke - Factor de Confiabilidad
    if confiabilidad=='50%':
        ke=1.0
    elif confiabilidad=='90%':
        ke=0.897
    elif confiabilidad=='95%':
        ke=0.868
    elif confiabilidad=='99%':
        ke=0.814
    elif confiabilidad=='99.9%':
        ke=0.753
    elif confiabilidad=='99.99%':
        ke=0.702
    elif confiabilidad=='99.999%':
        ke=0.659
    elif confiabilidad=='99.9999%':
        ke=0.620
    return ke

def se(ax,Sut,ks):
    ''' Calcula la resistencia a la fatiga de una probeta y tambien la resistencia a
    la fatiga para disenio de elementos a partir de la resistencia ultima a traccion
    y los factores que la modifican. '''
    #Convierte a valor numerico la resistencia a la traccion.
    Sut=float(Sut)
    #Calculos de la resistencia a la fatiga y la resistencia a la fatiga de una probeta
    if Sut<=1400.0:
        Sep=0.5*Sut
    else:
        Sep=700.0
    #Multiplica todos los coeficientes modificadores de la resistencia a la fatiga
    coef=1.0
    for k in ks.values():
        coef*=k
    Se=coef*Sep

    #Prepara los ejes para plotear
    #ax.set_aspect('equal','datalim')
    ax.set_xlim(-500,3000)
    ax.set_ylim(-400,1500)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    #Resistencia a la fatiga de una probeta
    ax.plot([0,1400,3500],[0,700,700],'r',lw=1.2)
    ax.plot([1400,2800],[700,1400],'b--',lw=0.6)
    #Crea los ejes x, y
    ax.axhline(y=0,linewidth=0.6,color='k',dashes=[5,2,10,2])
    ax.axvline(x=0,linewidth=0.6,color='k',dashes=[5,2,10,2])
    #Resistencia a la fatiga de una probeta
    ax.plot([Sut,Sut,0],[0,Sep,Sep],'k-',lw=0.4)
    #Se agrega etiquetas
    ax.text(-200,1100,r"$Se'$",fontsize=10,fontweight='bold')
    ax.text(1900,-200,r'$Sut$',fontsize=10,fontweight='bold')
    ax.text(1600,900,r"$\frac{Se'}{Sut}=0.5$",fontsize=8,fontweight='bold')
    ax.text(-150,Sep+20,str(Sep),fontsize=8)
    ax.text(Sut-80,-100,str(Sut),fontsize=8)
    #Retorba el valor de la resistencia a a la fatiga y la resistencia a la fatiga de una probeta
    return Se, Sep

def criteriosG(ax,Mcrit,Tcrit,Kf,Kfs,Se,matprop):
    ''' Agrupa los criterios de falla a la fatiga en un grafico tomando como parametros
    de entrada los ejes de ploteo, los momentos criticos, los coeficientes de concentracion
    de esfuerzos para fatiga, la resistencia a la fatiga y las propiedades del material.
    Retorna los esfuerzos equivalentes amplitud y medio.'''
    #Convierte a valor numerico y asigna las propiedades del material a variables.
    Sut=float(matprop[0])
    Sy=float(matprop[1])
    #Calcula los esfuerzos equivalentes amplitud y medio
    sap=32*Kf*Mcrit/pi #/d**3
    smp=abs(1/(sqrt(3))*16*Kfs*Tcrit/pi) #/d**3
    #Prepara los ejes para plotear
    ax.set_aspect('equal','datalim')
    ax.set_xlim(-0.2*Sut,1.2*Sut)
    ax.set_ylim(-0.2*Se,1.2*Sy)
    ax.axvline(x=0,linewidth=0.5,color='k',dashes=[5,2,10,2])
    ax.axhline(y=0,linewidth=0.5,color='k',dashes=[5,2,10,2])
    #Grafica la linea de carga
    LC=ax.plot([0,Sut],[0,Sut*sap/smp],'g-', linewidth=1.2)
    ax.text(0.11*Sut,.1*Sut*sap/smp,\
            r"$\sigma_a = \frac{\sigma_b'}{\sigma_a'} \cdot \sigma_m$",\
            fontsize=8,fontweight='bold')
    #Agrega etiquetas sobre los ejes
    ax.text(1*Sut,-.1*Sy,r'$Sut$',fontsize=10)
    ax.text(1*Sy,-.1*Sy,r'$Sy$',fontsize=10)
    ax.text(-.15*Sy,Sy,r'$Sy$',fontsize=10)
    ax.text(-.15*Sy,Se,r'$Se$',fontsize=10)
    #Dibuja las rectas de Langer, Soderberg y Goodman
    Lan=ax.plot([0,Sy],[Sy,0],'k--', lw=0.6)
    Sod=ax.plot([0,Sy],[Se,0],'k-', lw=1)
    Good=ax.plot([0,Sut],[Se,0],'k-', lw=1)
    #Obtiene los puntos para graficar la curva de Gerber
    x=np.linspace(0, round(Sut), 1000)
    y=Se*(1-(x/Sut)**2)
    #Muestra la grafica de la curva de Gerber
    Gerb=ax.plot(x, y,'k',lw=1)
    #Calcula los pares ordenados de los puntos de la curva de ASME
    x=np.linspace(0, round(Sy), 1000)
    y=Se*(1-(x/Sy)**2)**(1/2.0)
    #Plotea la curva eliptica de ASME
    ASME=ax.plot(x, y,'k',lw=1)
    #Regresa los valores de los esfuerzos equivalentes medio y amplitud
    return sap, smp

def dGoodman(sap,smp,Se,Sut,n): #[cm]
    ''' Respecto al criterio de falla de Goodman calcula el diametro dinamico del eje
    a partir de los esfuerzos equivalentes amplitud y medio y las propiedades del material.'''
    d=(n*(sap/Se+smp/Sut))**(1/3.0)
    return d

def dGerber(sap,smp,Se,Sut,n): #[cm]
    ''' Calcula el diametro dinamico del eje respecto al criterio de falla de Gerber
    a partir de los esfuerzos equivalentes amplitud y medio y las propiedades del material.'''
    d=(2*(n*smp/Sut)**2/(-n*sap/Se+sqrt((n*sap/Se)**2+4*(n*smp/Sut)**2)))**(1/3.0)
    return d

def dSoderberg(sap,smp,Se,Sy,n): #[cm]
    ''' Encuentra a partir de los esfuerzos equivalentes amplitud y medio y las 
    propiedades del material el diametro dinamico segun el criterio de falla a la 
    fatiga de Soderberg. '''
    d=(n*(sap/Se+smp/Sy))**(1/3.0)
    return d

def dASME(sap,smp,Se,Sy,n): #[cm]
    '''Usando el criterio de falla a la fatiga de ASME-eliptica, los esfuerzos equivalentes
    amplitud y medio y las propiedades del material, calcula el diametro dinamico.'''
    d=((n*sap/Se)**2+(n*smp/Sy)**2)**(1/6.0)
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
       self.ax1=self.graphics_Kt.canvas.fig.add_axes([.1,.05,0.8,0.4])
       self.ax2=self.graphics_Kt.canvas.fig.add_axes([.1,.55,0.8,0.4])
       self.show()

p=KtKts_Gui()
'''
'''
axs=p.ax2
axt=p.ax1
Mcrit=1029.03
Tcrit=600.0
Kf=1.86
Kfs=1.51

p.ax.set_axis_off()
#p.ax1.set_axis_off()
#p.ax2.set_axis_off()

fluct(axs,axt,Mcrit,Tcrit,Kf,Kfs)
'''
'''
ax=p.ax
Sut=250*6.89
acabado='Laminado en Caliente'
d=200
carga='Flexion'
T=59 #Celsius
confiabilidad='50%'
kf=1

ks={'ka':calc_ka(acabado,Sut),\
    'kb':calc_kb(d), 'kc':calc_kc(carga),\
    'kd':calc_kd(T),'ke':calc_ke(confiabilidad),\
    'kf':kf}
App.Console.PrintMessage('\nks:\n'+str(ks)) 

#p.ax.set_axis_off()
p.ax1.set_axis_off()
p.ax2.set_axis_off()

s=se(ax,Sut,ks)

Mcrit=80
Tcrit=180
Kf=1
Kfs=1
Se=200
matprop=[510,320]
crit=criteriosG(ax,Mcrit,Tcrit,Kf,Kfs,Se,matprop)

App.Console.PrintMessage('\nsigmaap:\n'+str(crit[0])+\
                         '\nsigmamp:\n'+str(crit[1])) 
'''

