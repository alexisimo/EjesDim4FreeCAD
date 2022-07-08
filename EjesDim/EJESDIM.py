import os
from PySide import QtCore, QtGui

from math import *
import numpy as np

import Modulos

from Modulos.interfaz import Ui_MainWindow
from Modulos.interfaz import Ui_Kt_Kts
import matplotlib

from Modulos.materiales import *
from Modulos.config_g import *
from Modulos.cargas import *
from Modulos.t_pref import *
from Modulos.d_estatico import *
from Modulos.d_dinamico import *
from Modulos.ktkf import *

class EjesDim_Gui(QtGui.QMainWindow, Ui_MainWindow):
   def __init__(self, parent=None):
       QtGui.QMainWindow.__init__(self, parent)
       self.setupUi(self)
       #Inicializa cantidades que se usaran en la clase
       self.mat=im_mat() #Agrega los materiales al combolist.
       self.matprop=[] #Propiedades del material seleccionado.

       self.vectorSecciones=[] #Lista de secciones vacia
       self.xcs=[] #Lista de ubicaciones donde hay concentradores de esfuerzos
       self.numsec=0 #Inicializacion del numero de secciones
       self.r=0 #Radio de entalle predeterminado

       self.vectorCargasXY=[] #Lista de cargas plano XY vacia
       self.vectorCargasXZ=[] #Lista de cargas plano XZ vacia
       self.vectorCargasT=[]  #Lista de cargas de Torsion vacia
       self.numcarga=0 #Inicializacion del numero de cargas de Flexion

       self.xcrit=0 #Ubicacion de la seccion critica inicializada
       self.Mcrit=0 #Momento Flector Critico inicializado
       self.Tcrit=0 #Momento Torsor Critico inicializado
       self.Mxzcrit=0 #Momento Flector Critico en XZ inicializado
       self.Mxycrit=0 #Momento Flector Critico en XY inicializado

       self.sigmax=0 #Inicializa el valor del esfuerzo ordinario normal
       self.tauxz=0 #Inicializa el valor del esfuerzo ordinario cortante

       self.sigma1=0 #Inicializa el valor del esfuerzo principal normal
       self.sigma2=0 #Inicializa el valor del esfuerzo principal normal
       self.sigmaT=0 #Inicializa el valor del esfuerzo principal medio
       self.tau12=0 #Inicializa el valor del esfuerzo principal cortante
       self.phi=0 #Inicializa el angulo al que se encuentran los esfuerzos principales

       self.Kt=1  #Factor teorico de Concentracion de Esfuerzos a Flexion inicializado
       self.Kts=1 #Factor teorico de Concentracion de Esfuerzos a Torsion inicializado
       self.Kf=1  #Factor teorico de Concentracion de Esfuerzos a Flexion Dinamica inicializado
       self.Kfs=1 #Factor teorico de Concentracion de Esfuerzos a Torsion Dinamica inicializado

       self.sigma_a=0 #Inicializa el valor del esfuerzo normal amplitud
       self.tau_m=0 #Inicializa el valor del esfuerzo cortante medio

       self.sigma_ap=0 #Inicializa el valor del esfuerzo equivalente amplitud
       self.sigma_mp=0 #Inicializa el valor del esfuerzo equivalente medio

       self.se=0 #Inicializa el valor de la resistencia a la fatiga
       self.sep=0 #Inicializa el valor de la resistencia a la fatiga de una probeta

       self.dcrit=3 #Inicializa el valor del diametro critico
       self.d_iter=0 #Inicializa el valor del diametro para iterar
       self.tol=0.001 #Inicializa el valor de la tolerancia

       self.ks={} #Diccionario de los coeficientes que modifican la resistencia a la fatiga

       #Inicia el formulario de Kt y Kts
       self.KtKtsUi = KtKts_Gui()

       #Ubicacion actual en el directorio
       self.dir = os.path.dirname(__file__)
       #Logotipo
       self.logo=matplotlib.image.imread(os.path.join(self.dir+"\Graficos", "Logo.png"))
       #Icono
       pixmap = QtGui.QPixmap(self.dir+'/Graficos/LogoI.png')
       icon = QtGui.QIcon(pixmap)
       self.setWindowIcon(icon)
       #-Tab Configuracion
       #	-Grupo Material
       #		-Combo Materiales
       self.combo_Mat.addItems(self.mat[0])
       QtCore.QObject.connect(self.combo_Mat,QtCore.SIGNAL('activated(int)'), self.desactradio)
       #		-Boton Propiedades
       QtCore.QObject.connect(self.button_Prop,QtCore.SIGNAL("pressed()"),self.propmat)
       #	-Grupo Configuracion Preliminar
       #		-Plot Configuracion
       self.graphics_Config.canvas.ax.imshow(self.logo)
       self.graphics_Config.canvas.draw()
       #		-Etiqueta Soporte 1
       #		-Entrada Soporte 1
       #		-Etiqueta Soporte 2
       #		-Entrada Soporte 2
       QtCore.QObject.connect(self.edit_XR2,QtCore.SIGNAL("returnPressed()"),self.creareje)
       #		-Boton Crear
       QtCore.QObject.connect(self.button_CrearEje,QtCore.SIGNAL("pressed()"),self.creareje)
       #	-Grupo Seccion
       #		-Etiqueta Diametro
       #		-Etiqueta Longitud
       #		-Entrada Diametro
       #		-Entrada Longitud
       QtCore.QObject.connect(self.edit_L,QtCore.SIGNAL("returnPressed()"),self.addseccion)
       #		-Boton Anadir
       QtCore.QObject.connect(self.button_AddSec,QtCore.SIGNAL("pressed()"),self.addseccion)
       #		-Lista Secciones
       #		-Boton Suprimir
       QtCore.QObject.connect(self.button_SupSec,QtCore.SIGNAL("pressed()"),self.supseccion)
       #	-Grupo Concentrador de Esfuerzos
       #		-Etiqueta Hombros
       #		-Entrada radio de Acuerdo
       #-Tab Cargas
       #	-Grupo Cargas
       #		-Etiqueta Tipo
       #		-Etiqueta Angulo
       #		-Combo Tipo de Carga
       self.combo_TipoCarga.addItems(['Fuerza Concentrada', 'Momento Flector', \
									'Carga Distribuida Constante', 'Carga Distribuida Lineal','Momento Torsor'])
       QtCore.QObject.connect(self.combo_TipoCarga,QtCore.SIGNAL('activated(int)'), self.desactedit)
       #		-Entrada Angulo
       #		-Etiqueta Magnitud Inicial
       #		-Etiqueta Magnitud
       #		-Etiqueta Posicion Inicial
       QtCore.QObject.connect(self.edit_PosXi,QtCore.SIGNAL("returnPressed()"),self.addcarga)
       #		-Etiqueta Posicion Final
       #		-Entrada Magnitud Inicial
       #		-Entrada Magnitud
       #		-Entrada Posicion Inicial
       #		-Entrada Posicion Final
       #		-Lista Cargas
       self.list_Cargas.addItem( 'CARGAS DE FLEXION:')
       self.list_Cargas.addItem( 'CARGAS DE TORSION:')
       #		-Boton Anadir
       QtCore.QObject.connect(self.button_AddCarga,QtCore.SIGNAL("pressed()"),self.addcarga)
       #		-Boton Suprimir
       QtCore.QObject.connect(self.button_SupCarga,QtCore.SIGNAL("pressed()"),self.supcarga)
       #	-Grupo Diagramas
       #		-Plot Diagramas
       self.graphics_Diag.canvas.ax.imshow(self.logo)
       self.graphics_Diag.canvas.draw()
       #		-Boton Calcular
       QtCore.QObject.connect(self.button_CalcDiag,QtCore.SIGNAL("pressed()"),self.calcular)
       #		-Radio PlanoXZ
       #		-Radio PlanoXY
       #		-Radio Torsion/Total
       #	-Grupo Reacciones
       #		-Etiqueta RXY1
       #		-Etiqueta RXY2
       #		-Etiqueta RXZ1
       #		-Etiqueta RXZ2
       #-Tab Disenio Estatico
       #	-Grupo Circulo de Mohr
       #		-Plot Circulo de Mohr
       self.graphics_CMohr.canvas.ax.imshow(self.logo)
       self.graphics_CMohr.canvas.draw()
       #		-Etiqueta Sigma1
       #		-Etiqueta Sigma2
       #		-Etiqueta Tau12
       #		-Etiqueta SigmaTau
       #		-Etiqueta Phi
       #	-Grupo Seccion Critica
       #		-Plot Seccion Critica
       self.graphics_SCrit.canvas.ax.imshow(self.logo)
       self.graphics_SCrit.canvas.draw()
       #		-Etiqueta TauXZ
       #		-Etiqueta SigmaX
       #		-Etiqueta Posicion de x Critica
       #		-Boton Informacion de Kt Kts
       QtCore.QObject.connect(self.button_KtKts,QtCore.SIGNAL("pressed()"),self.ver_ktkts)
   	   #	-Grupo Teorias de Falla
   	   #		-Etiqueta Material Ductil
   	   #		-Etiqueta Material Fragil
   	   #		-Radio Coulomb Mohr Fragil
       QtCore.QObject.connect(self.radio_CMF,QtCore.SIGNAL("clicked()"),self.calcularTF)
   	   #		-Radio Mohr Modificado
       QtCore.QObject.connect(self.radio_MM,QtCore.SIGNAL("clicked()"),self.calcularTF)
   	   #		-Plot Teoria de Falla
       self.graphics_TFalla.canvas.ax.imshow(self.logo)
       self.graphics_TFalla.canvas.draw()
   	   #		-Radio Esfuerzo Normal Maximo
       QtCore.QObject.connect(self.radio_ENM,QtCore.SIGNAL("clicked()"),self.calcularTF)
   	   #		-Radio Energia de Distorsion
       QtCore.QObject.connect(self.radio_ED,QtCore.SIGNAL("clicked()"),self.calcularTF)
   	   #		-Radio Coulomb Mohr Ductil
       QtCore.QObject.connect(self.radio_CMD,QtCore.SIGNAL("clicked()"),self.calcularTF)
   	   #		-Radio Esfuerzo Cortante Maximo
       QtCore.QObject.connect(self.radio_ECM,QtCore.SIGNAL("clicked()"),self.calcularTF)
   	   #	-Grupo Diametros
   	   #		-Etiqueta Secciones
   	   #		-Entrada Factor de Disenio n
   	   #		-Etiqueta Factor de Disenio
       #		-Linea vertical
   	   #		-Lista Secciones Disenio Estatico
   	   #		-Etiqueta n
   	   #		-Etiqueta Seccion Critica
   	   #		-Etiqueta Diametro de Seccion Critica
   	   #		-Boton Calcular Diametro
       QtCore.QObject.connect(self.button_CalcDiam,QtCore.SIGNAL("pressed()"),self.calcdcritDE)
   	   #		-Boton Recalcular con las Nuevas Dimensiones
       QtCore.QObject.connect(self.button_ReCalc,QtCore.SIGNAL("pressed()"),self.recalc)
       #-Tab Disenio Dinamico
       #	-Grupo Esfuerzos Fluctuantes
   	   #		-Plot Esfuerzos Fluctuantes
       self.graphics_Fluct.canvas.ax.imshow(self.logo)
       self.graphics_Fluct.canvas.draw()
   	   #		-Etiqueta Sigma Amplitud
   	   #		-Etiqueta Tau Amplitud
   	   #		-Etiqueta Tau Medio
   	   #		-Etiqueta Sigma Medio
   	   #		-Boton Kf y  Kfs
       QtCore.QObject.connect(self.button_KfKfs,QtCore.SIGNAL("pressed()"),self.ver_kfkfs)
   	   #	-Grupo Criterios de Falla a la Fatiga
   	   #		-Radio ED-Goodman
       QtCore.QObject.connect(self.radio_Goodman,QtCore.SIGNAL("clicked()"),self.calcularCF)
   	   #		-Radio ED-Gerber
       QtCore.QObject.connect(self.radio_Gerber,QtCore.SIGNAL("clicked()"),self.calcularCF)
   	   #		-Radio ED-Soderberg
       QtCore.QObject.connect(self.radio_Soderberg,QtCore.SIGNAL("clicked()"),self.calcularCF)
   	   #		-Radio ED-ASME eliptica
       QtCore.QObject.connect(self.radio_ASME,QtCore.SIGNAL("clicked()"),self.calcularCF)
   	   #		-Plot Criterios de Falla a la Fatiga
       self.graphics_CFalla.canvas.ax.imshow(self.logo)
       self.graphics_CFalla.canvas.draw()
   	   #		-Etiqueta Sigma Amplitud Prima
   	   #		-Etiqueta Sigma Medio Prima
   	   #	-Grupo Diametros Disenio Dinamico
   	   #		-Etiqueta Factor de Disenio Dinamico
       #		-Linea vertical
   	   #		-Etiqueta Diametro Seccion Critica Dinamico
   	   #		-Entrada Diametro Dinamico
   	   #		-Boton Recalcular Disenio Dinamico
       QtCore.QObject.connect(self.button_ReCalcD,QtCore.SIGNAL("pressed()"),self.recalcD)
   	   #		-Etiqueta nd
   	   #		-Entrada nd
   	   #		-Boton Calcular Diametro Dinamico
       QtCore.QObject.connect(self.button_CalcDiamD,QtCore.SIGNAL("pressed()"),self.calcdcritDD)
   	   #		-Etiqueta Secciones Disenio Dinamico
   	   #		-Lista Secciones Disenio Dinamico
       #		-Etiqueta Iteraciones
   	   #		-Tabla Iteraciones
   	   #	-Grupo Resisencia a la Fatiga
   	   #		-Etiqueta Se Prima
   	   #		-Etiqueta Sut
   	   #		-Etiqueta Coeficientes de Marin
   	   #		-Plot Resistencia a la Fatiga
       self.graphics_RFatiga.canvas.ax.imshow(self.logo)
       self.graphics_RFatiga.canvas.draw()
   	   #		-Boton ka
       QtCore.QObject.connect(self.button_ka,QtCore.SIGNAL("pressed()"),self.ka)
   	   #		-Boton kb
       QtCore.QObject.connect(self.button_kb,QtCore.SIGNAL("pressed()"),self.kb)
   	   #		-Boton kc
       QtCore.QObject.connect(self.button_kc,QtCore.SIGNAL("pressed()"),self.kc)
   	   #		-Boton kd
       QtCore.QObject.connect(self.button_kd,QtCore.SIGNAL("pressed()"),self.kd)
   	   #		-Boton ke
       QtCore.QObject.connect(self.button_ke,QtCore.SIGNAL("pressed()"),self.ke)
   	   #		-Boton kf
       QtCore.QObject.connect(self.button_kf,QtCore.SIGNAL("pressed()"),self.kf)
   	   #		-Etiqueta ka
   	   #		-Etiqueta kb
   	   #		-Etiqueta kc
   	   #		-Etiqueta kd
   	   #		-Etiqueta ke
   	   #		-Etiqueta kf
   	   #		-Etiqueta Se
   	   #		-Etiqueta Se2
       #-Barra de Menu
       #	-Menu Archivo
       #		-Salir
       QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL("triggered()"),self.close)       
       #	-Menu Ayuda
       #		-Acerca de
       QtCore.QObject.connect(self.actionAcerca_de, QtCore.SIGNAL("triggered()"),self.acerca_de)
       #-Barra de Estado
       #Muestra un mensaje de bienvenida en la barra de estado
       self.statusBar().showMessage("Bienvenido a EjesDim", 3000)


       #Crea un nuevo documento al iniciar el programa
       FreeCAD.newDocument('EjesDim')
       #Inicializa un objeto Eje
       self.miEje=FreeCAD.ActiveDocument.addObject("Part::Feature","Eje")
       #Inicializa un objeto Momentos3D
       self.miDiag=FreeCAD.ActiveDocument.addObject("Part::Feature","Momentos3D")
       #Inicializa un objeto Cargas
       self.miCarg=FreeCAD.ActiveDocument.addObject("Part::Feature","Cargas")
       #Inicializa un objeto Cargas
       self.miApoyo=FreeCAD.ActiveDocument.addObject("Part::Feature","Apoyos")

       self.show()
       #Actualiza las propiedades del material
       self.desactradio(0)

   def propmat(self):
       '''Metodo activado al presionar el boton de informacion que muestra un dialogo 
       con las propiedades del material seleccionado en el combo de seleccion de materiales.'''
       #Asigna la propiedad Sy del material a una variable
       material=self.combo_Mat.currentText()[5:]
       #Verifica si la propiedad 
       if self.mat[2][material] == '--': #Fragil
           QtGui.QMessageBox.information(None,"Propiedades del Material: Fragil",\
                                     self.combo_Mat.currentText()+\
                                     '\n\t\tSut: '+str(im_mat()[1][material])+' [MPa]'+\
                                     '\tSuc: '+str(im_mat()[3][material])+' [MPa]')
       else: #Ductil
           QtGui.QMessageBox.information(None,"Propiedades del Material: Ductil",\
                                     self.combo_Mat.currentText()+\
                                     '\n\t\tSut: '+str(im_mat()[1][material])+' [MPa]'+\
                                     '\tSy: '+str(im_mat()[2][material])+' [MPa]')

   def addseccion(self):
       '''Metodo para agregar una seccion a la lista de secciones que toma los valores de
       los cajones de diametro y longitud; se activa con el boton aniadir.'''
       try:
           #Valida si los datos de entrada son numericos
           D = float(self.edit_D.text())  #[mm]
           L = float(self.edit_L.text())  #[mm]
           #Comprueba el signo
           (D)**(-1/2.0)
           (L)**(-1/2.0)
       except ValueError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Error: Ingrese valores numericos validos.", 2000)
       except ZeroDivisionError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Error: Los valores no pueden ser cero.", 2000)
       else:
           #Anade una seccion a partir de los valores de D y L al vectorSecciones
           addseccion(self.vectorSecciones, D/2, L)
		   #Anade un item de la seccion anadida a la lista
           self.numsec+=1
           self.list_Secciones.addItem('S'+str(self.numsec)+': '+\
										str(self.vectorSecciones[-1]))
		   #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Anadido: "+str(self.vectorSecciones[-1]), 2000)
		   #Limpia los cajones de entrada
           self.edit_D.setText("")
           self.edit_L.setText("")
		   #Muestra informacion de las secciones en la consola
           self.infosecciones()

   def supseccion(self):
       '''Metodo activado por el boton suprimir que sirve
       para suprimir una seccion seleccionada de la lista de secciones.'''
	   #Remover seccion de la lista y verifica si esta seleccionada una.
       row=self.list_Secciones.currentRow()
       if row == -1:
           self.statusBar().showMessage("Seleccione una seccion a suprimir", 2000)
       else:
           self.list_Secciones.takeItem(row)
	       #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Suprimida seccion : "+str(self.vectorSecciones[row]), 2000)
           #Remover seccion del vectorSecciones
           self.vectorSecciones.pop(row)
 	   #Muestra informacion de las secciones en la consola
       self.infosecciones()

   def infosecciones(self):
       '''Muestra informacion de las secciones en la consola.'''
       #Toma cada seccion y muestra sus propiedades en la consola
       App.Console.PrintMessage("SECCIONES:\n") 
       for seccion in self.vectorSecciones:
           App.Console.PrintMessage(str(seccion)+"\n") 
       App.Console.PrintMessage("----\n") 

   def creareje(self):
       '''Crea una parte eje en funcion de las secciones del vectorSecciones
       y el radio de acuerdo establecido.'''
       try:
           #Valida los datos de entrada
           self.r = round(float(self.dspinbox_rda.value()),2) #[mm]
           VS = self.vectorSecciones
           XR1 = float(self.edit_XR1.text()) #[mm]
           XR2 = float(self.edit_XR2.text()) #[mm]
           #Comprueba el signo
           self.r**(1/2.0)
           (XR1)**(1/2.0)
           (XR2)**(-1/2.0)
           1/len(VS)
       except ValueError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Error: Ingrese valores numericos validos.", 2000)
       except ZeroDivisionError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Error: No puede crearse un eje sin secciones.", 2000)
       else:
           #Verifica si los apoyos se encuentran a lo largo del eje
           if XR1<XR2 and XR2<=self.longeje():
               #Une las secciones creando un solo solido
               eje=unirsecciones(self.vectorSecciones)
               #Guarda los valores de x en los cambios de seccion
               self.xcs=cambiosecc(eje)[1] #[mm]
               #Realiza un redondeado en las aristas del eje si es el caso
               if len(self.vectorSecciones) > 1 and self.r >= 0.05:
                   eje0=unirsecciones(self.vectorSecciones)
                   eje=r_deacuerdo(eje0,self.r)[0]
                   r=r_deacuerdo(eje0,self.r)[1]
                   #Verifica el radio de entalle
                   self.r=r
                   self.dspinbox_rda.setValue(r)
                   if r == 0.0:
                       self.statusBar().showMessage("Error: Radio de entalle no valido.", 2000)
               #Asigna el eje a la forma inicializada
               self.miEje.Shape = eje

               #Cambiar a vista Frontal para la captura
               Gui.activeDocument().getObject("Momentos3D").Visibility = False
               Gui.activeDocument().getObject("Cargas").Visibility = False
               Gui.activeDocument().getObject("Apoyos").Visibility = False
               #Gui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii\n\n\nOrthographicCamera {\n  viewportMapping ADJUST_CAMERA'+
				#											'\n  position 359.5 -30.460846 363.66174'+
				#											'\n  orientation 0 0 1  0\n  nearDistance 125.19504'+
				#											'\n  farDistance 400.01138\n  aspectRatio 1'+
				#											'\n  focalDistance 363.66174\n  height 399.16367\n\n}\n')
               Gui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii\n\n\nOrthographicCamera {\n  viewportMapping ADJUST_CAMERA'+
                                                                     '\n  position 9 -9.0275707 0.0019717829'+
                                                                     '\n  orientation -1 0 0  4.712389\n  nearDistance 8.5199633'+
                                                                     '\n  farDistance 17.269949\n  aspectRatio 1'+
                                                                     '\n  focalDistance 9.0275717\n  height 18.055143\n\n}\n')
               Gui.SendMsgToActiveView("ViewFit")
               vista = Gui.activeDocument().activeView().getCamera()
               Gui.activeDocument().activeView().setCamera(vista[:-22]+'height '+str(self.longeje()/1.235)+'\n\n}\n')
               self.statusBar().showMessage('Creando vista...', 2000)
               #Guarda una captura
               #Gui.activeDocument().activeView().saveImage(os.path.join(self.dir+"\Graficos", 'Captura.png'),2000,1600,'White')
               Gui.activeDocument().getObject("Momentos3D").Visibility = True
               Gui.activeDocument().getObject("Cargas").Visibility = True
               Gui.activeDocument().getObject("Apoyos").Visibility = True
               #Carga la captura realizada y la muestra en la vista preliminar
               img=matplotlib.image.imread(os.path.join(self.dir+"\Graficos", 'Captura.png'))
               #Limpia y crea los ejes de ploteo
               #self.graphics_Config.canvas.ax.set_axis_off()
               ax=self.graphics_Config.canvas.fig.add_axes([0.06,0.06,.9,.9])
               ax.clear()
               #Establece las etiquetas segun la longitud del eje
               ax.set_xticks(np.linspace(0,2000,10))

               xticklabels=[]
               for xt in np.linspace(0,self.longeje(),10):
                   xticklabels.append(round(xt/1000,2)) #[m]

               ax.set_xticklabels(xticklabels)
               #Quita las etiquetas del eje y           
               for yt in ax.get_yticklabels():
                   yt.set_visible(False)
               #Muestra la linea y=0
               ax.axhline(y=800,linewidth=0.5,color='k',dashes=[5,2,10,5])
               #Muestra las lineas x en cada cambio de seccion
               for xcs in self.xcs:
                   ax.axvline(x=2000*xcs/self.longeje(),linewidth=0.5,color='k',dashes=[5,2,10,5])
               xd=0
               for i in range(len(self.vectorSecciones)):
                   #Muestra los diametros de las secciones
                   ax.text(xd+(2000/self.longeje())*self.vectorSecciones[i].l/3,810+4*self.vectorSecciones[i].r*(-1)**i,r"$\phi$"+str(self.vectorSecciones[i].r*2),fontsize=10)
                   xd+=(2000/self.longeje())*(self.vectorSecciones[i].l)
               #Muestra el material en la vista preliminar de la configuracion
               ax.text(20,80,"Material: "+str(self.combo_Mat.currentText()),fontsize=10)
               #Crea una lista vacia de patrones a graficar
               pts=[]
               #Agrega a los patrones para los apoyos
               pts.append(matplotlib.patches.RegularPolygon((2000*XR1/self.longeje(), 880), 3, radius=80,orientation=3.14,alpha=0.5))
               pts.append(matplotlib.patches.RegularPolygon((2000*XR2/self.longeje(), 880), 3, radius=80,orientation=3.14,alpha=0.5))
               ax.plot([2000*XR2/self.longeje()-80,2000*XR2/self.longeje()+80],[940,940],'b', linewidth=1,alpha=0.5)
               #Muestra cada patron en los ejes de ploteo
               for p in pts:
                   ax.add_patch(p)
               #Muestra la rejilla vertical
               ax.xaxis.grid()
               #Establece la imagen en los ejes correspondientes
               ax.imshow(img)
               #Fuerza a redibujar el lienzo
               self.graphics_Config.canvas.fig.autofmt_xdate()
               self.graphics_Config.canvas.draw()

               #Cambiar a vista Axonometrica
               Gui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii\n\n\nOrthographicCamera {\n  viewportMapping ADJUST_CAMERA'+
                                                                      '\n  position 14.349236 4.1479731 5.974998'+
                                                                      '\n  orientation -0.52468312 0.82658482 0.20363043  0.86714548'+
                                                                      '\n  nearDistance -5.5198398\n  farDistance 15.053202'+
                                                                      '\n  aspectRatio 1\n  focalDistance 9.0275717\n  height 18.055143\n\n}\n')
               Gui.SendMsgToActiveView("ViewFit")
	           #Activar visibilidad de ejes
               Gui.ActiveDocument.ActiveView.setAxisCross(True)

               #Muestra la longitud total del eje en el boton Crear
               self.button_CrearEje.setText('Ltot= '+str(self.longeje()))
               #Funcion de representacion visual de los apoyos
               self.visualapoyos()
           else:
               self.statusBar().showMessage("Error: Apoyos fuera del eje.", 2000)

   def desactedit(self,n):
       '''Metodo para activar y desactivar las casillas segun
       la carga seleccionada y establece las unidades adecuadas'''
       #Predeterminada Fuerza Concentrada
       self.edit_Mi.setEnabled(False)
       self.edit_PosXf.setEnabled(False)
       self.dspinbox_Angulo.setEnabled(True)
       self.label_M.setText("M [N]")
       if n == 1: #Momento Flector
           self.label_M.setText("M [Nm]")
       elif n == 2: #Carga distribuida constante
           self.edit_PosXf.setEnabled(True)
       elif n == 3: #Carga distribuida lineal
           self.edit_Mi.setEnabled(True)
           self.edit_PosXf.setEnabled(True)
           self.label_M.setText("M [N]")
       elif n == 4: #Momento Torsor
           self.dspinbox_Angulo.setEnabled(False)
           self.label_M.setText("M [Nm]")


   def addcarga(self):
       '''Metodo para agregar una carga al eje.'''
       try:
           #Valida si los datos de entrada son numericos
           mi = float(self.edit_Mi.text()) #[N]
           m = float(self.edit_M.text())   #[N] o [Nm]
           posXi = float(self.edit_PosXi.text())/1000 #[m]
           posXf = float(self.edit_PosXf.text())/1000 #[m]
           angulo = float(self.dspinbox_Angulo.value()) #[grados]
           #Comprueba el signo y ceros
           1.0/(m)
           (posXi)**(1/2.0)
           (posXf)**(1/2.0)
       except ValueError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Error: Ingrese valores numericos validos.", 2000)
       except ZeroDivisionError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Error: Los valores no pueden ser cero.", 2000)
       else:
           #Establece como la posicion final la longitud del eje para las cargas concentradas.
           if self.combo_TipoCarga.currentText() == 'Fuerza Concentrada' or\
              self.combo_TipoCarga.currentText() == 'Momento Flector' or\
              self.combo_TipoCarga.currentText() == 'Momento Torsor':
               posXf = self.longeje()/1000
           #Verifica si la posicion final es mayor a la inicial y si se encuentra dentro de la longitud del eje.
           if posXf>=posXi and posXf<=self.longeje()/1000:
               if self.combo_TipoCarga.currentText() == 'Momento Torsor':
                   #Anade una carga de torsion a partir de los valores de m, posXi al vectorCargasT
                   self.vectorCargasT.append(CargaPlana(self.combo_TipoCarga.currentText(),m ,posXi))
                   #Anade un item al final de la lista de cargas
                   self.list_Cargas.addItem( str(self.combo_TipoCarga.currentText())+\
                                            '\n T: '+str(self.vectorCargasT[-1]))
                   #Muestra un mensaje en la barra de estado
                   self.statusBar().showMessage('Anadido: T '+str(self.vectorCargasT[-1]), 2000)
               else:
                   self.numcarga+=1
                   #Anade una carga a partir de los valores de m, posXi,posXf y el angulo respecto al plano XZ al vectorCargas
                   addCarga(self.vectorCargasXY, "XY", self.combo_TipoCarga.currentText(),m, posXi,posXf,angulo,mi)
                   addCarga(self.vectorCargasXZ, "XZ", self.combo_TipoCarga.currentText(),m, posXi,posXf,angulo,mi)
		           #Anade un item a continuacion del anterior
                   self.list_Cargas.insertItem( self.numcarga,str(self.combo_TipoCarga.currentText())+\
                                            '\n M= '+str(m)+' ang= '+str(angulo)+' Mi= '+ str(mi)+\
                                            '\n XY: '+str(self.vectorCargasXY[-1])+\
					    			        '\n XZ: '+str(self.vectorCargasXZ[-1]))
                   #Muestra un mensaje en la barra de estado
                   self.statusBar().showMessage('Anadido: XY '+str(self.vectorCargasXY[-1])+'  XZ '+str(self.vectorCargasXZ[-1]), 2000)
               #Limpia los cajones de entrada
               self.edit_Mi.setText("0")
               self.edit_M.setText(" ")
               self.edit_PosXi.setText(" ")
               self.edit_PosXf.setText(str(self.longeje()))
               self.dspinbox_Angulo.setValue(0)

           else:
               #Muestra un mensaje de error en la barra de estado
               self.statusBar().showMessage('La carga no se puede crear.'+'  PosXf= '+str(posXf)+'  Leje= '+str(self.longeje()), 2500)
           #Muestra informacion de las cargas en la consola
           self.infocargas()
           #Funcion de representacion visual de las cargas
           self.visualcargas()
           #Bloquea la supresion de secciones
           self.button_SupSec.setEnabled(False)

   def visualapoyos(self):
       '''Metodo para representacion visual de los apoyos.'''
       #Toma los valores de los cajones
       XR1 = float(self.edit_XR1.text()) #[mm]
       XR2 = float(self.edit_XR2.text())
       #Crea las representaciones visuales de los apoyos
       apoyos=visualapoyos(XR1,XR2,self.longeje()) #[mm]
       #Asigna la pieza cargas a la forma inicializada
       self.miApoyo.Shape=apoyos
       #Configura la visualizacion de las cargas
       Gui.ActiveDocument.Apoyos.Selectable=False
       Gui.ActiveDocument.Apoyos.DisplayMode='Shaded'
       Gui.ActiveDocument.Apoyos.Transparency=40
       Gui.ActiveDocument.Apoyos.ShapeColor=(0.33,0.33,0.50)

   def visualcargas(self):
       '''Metodo para representacion visual de las cargas.'''
       #Crea una pieza con las representaciones visuales de las cargas
       cargas=visualcargas(self.vectorCargasXY,self.vectorCargasXZ,self.vectorCargasT,self.longeje()) #[mm]
       #Asigna la pieza cargas a la forma inicializada
       self.miCarg.Shape=cargas
       #Configura la visualizacion de las cargas
       Gui.ActiveDocument.Cargas.Selectable=False
       Gui.ActiveDocument.Cargas.DisplayMode='Shaded'
       Gui.ActiveDocument.Cargas.Transparency=40
       Gui.ActiveDocument.Cargas.ShapeColor=(0.00,0.33,1.00)
   
   def infocargas(self):
       '''Muestra informacion de las cargas en la consola.'''
       #Toma la informacion de cada carga y la muestra en la consola.
       App.Console.PrintMessage("CARGAS:\n")
       App.Console.PrintMessage("XY:\n")            
       for carga in self.vectorCargasXY:
           App.Console.PrintMessage(str(carga)+"\n") 
       App.Console.PrintMessage("XZ:\n")            
       for carga in self.vectorCargasXZ:
           App.Console.PrintMessage(str(carga)+"\n")
       App.Console.PrintMessage("T:\n")            
       for carga in self.vectorCargasT:
           App.Console.PrintMessage(str(carga)+"\n")
       App.Console.PrintMessage("----\n") 

   def supcarga(self):
       '''Remueve una carga de la lista.'''
       #Verifica la seleccion
       row=self.list_Cargas.currentRow()
       if row == -1 or row == 0 or row == self.numcarga+1:
           self.statusBar().showMessage("Seleccione una carga a suprimir", 2000)
       else:
           if row >= self.numcarga+2:
               rowT=row-(self.numcarga+2)
               #Remover carga del vectorCargasT
               self.vectorCargasT.pop(rowT)
           else:
               #Remover carga del vectorCargas
               self.vectorCargasXY.pop(row-1)
               self.vectorCargasXZ.pop(row-1)
               #Resta 1 al contador de cargas
               self.numcarga-=1
           #Retira el item seleccionado de la lista
           self.list_Cargas.takeItem(row)
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Suprimida carga seleccionada", 2000)
       #Muestra informacion de las cargas en la consola
       self.infocargas()
       #Funcion de representacion visual de las cargas
       self.visualcargas()

   def longeje(self):
       '''Metodo que calcula el total de la longitud del eje [mm]
       sumando las longitudes de las secciones en vectorSecciones.'''
       #Inicializa la longitud del eje en cero
       longEje = 0
       #Para cada seccion extrae su longitud y la suma a longEje
       for seccion in self.vectorSecciones:
           longEje+=seccion.l
       return longEje
       
   def calcular(self):
       '''Con la lista de cargas y sus propiedades calcula las reacciones y
        los diagramas de cortantes, momentos flector y torsor, crea tambien 
        una representacion 3D de los diagramas de momento flector. 
        Ademas grafica la seccion critica, el circulo de Mohr y las teorias 
        de falla con sus cantidades respectivas para el disenio estatico, para 
        el disenio dinamico deja listo los esfuerzos fluctuantes, para completar 
        con la resistencia a la fatiga y lo que sigue.'''
       try:
           #Valida si los datos de entrada son numericos
           XR1 = float(self.edit_XR1.text())/1000 #[m]
           XR2 = float(self.edit_XR2.text())/1000 #[m]
       except ValueError:
           self.statusBar().showMessage("Ingrese valores numericos validos en los apoyos", 2000)
       else:
           #----Calculo de reacciones, fuerzas cortantes y momentos flectores----
           longEje = self.longeje()/1000 #[m]
           #Verifica si los apoyos se encuentran a lo largo del eje
           if XR1<XR2 and XR2<=longEje:
               #Calcula las reacciones en cada plano
               Rxy = reaccion(self.vectorCargasXY,longEje,XR1,XR2)
               Rxz = reaccion(self.vectorCargasXZ,longEje,XR1,XR2)
               #Muestra la magnitud de las reaccion calculadas
               self.label_RXY1.setText('RY1: '+str(round(Rxy[0],2))+'[N]')
               self.label_RXY2.setText('RY2: '+str(round(Rxy[1],2))+'[N]')
               self.label_RXZ1.setText('RZ1: '+str(round(Rxz[0],2))+'[N]')
               self.label_RXZ2.setText('RZ2: '+str(round(Rxz[1],2))+'[N]')
               #Crea una copia del vector de cargas para anadirle las reacciones
               vectorCargasRxy=self.vectorCargasXY[:]
               vectorCargasRxz=self.vectorCargasXZ[:]
               vectorCargasT=self.vectorCargasT[:]
               #Agrega las reacciones en cada plano y apoyo a un nuevo vector de cargas
               addCarga(vectorCargasRxy,"XY","Fuerza Concentrada",Rxy[0],XR1)
               addCarga(vectorCargasRxy,"XY","Fuerza Concentrada",Rxy[1],XR2)
               addCarga(vectorCargasRxz,"XY","Fuerza Concentrada",Rxz[0],XR1)
               addCarga(vectorCargasRxz,"XY","Fuerza Concentrada",Rxz[1],XR2)
               #Ordena las cargas y muestra informacion de las mismas en la consola
               vectorCargasRxy.sort()
               vectorCargasRxz.sort()
               vectorCargasT.sort()
               #Crea un vector con valores de x a lo largo de la longitud del eje
               x = vectorX(longEje) #[m]
               #Calcula los valores para los diagramas V, M y T en cada plano
               Vxy = diagCortantes(x,vectorCargasRxy) #[N]
               Mxy = diagMomentos(x,vectorCargasRxy)  #[Nm]
               Vxz = diagCortantes(x,vectorCargasRxz) #[N]
               Mxz = diagMomentos(x,vectorCargasRxz)  #[Nm]
               T = diagTorsion(x,vectorCargasT)       #[Nm]
               #Calcula el valor de los Momentos Totales
               Mtot = []                              #[Nm]
               for i in range(len(x)):
                   Mtot.append(sqrt(Mxy[i]**2+Mxz[i]**2))
               #Encuentra los valores maximos absolutos en cada diagrama
               maxVxy = max(abs(max(Vxy)),abs(min(Vxy))) #[N]
               maxVxz = max(abs(max(Vxz)),abs(min(Vxz))) #[N]
               maxMxy = max(abs(max(Mxy)),abs(min(Mxy))) #[Nm]
               maxMxz = max(abs(max(Mxz)),abs(min(Mxz))) #[Nm]
               maxMtot = max(abs(max(Mtot)),abs(min(Mtot))) #[Nm]
               maxT = max(abs(max(T)),abs(min(T)))       #[Nm]
               #Encuentra el indice del valor maximo
               iVxy=indice(Vxy,maxVxy)
               iVxz=indice(Vxz,maxVxz)
               iMxy=indice(Mxy,maxMxy)
               iMxz=indice(Mxz,maxMxz)
               iMtot=indice(Mtot,maxMtot)
               iT=indice(T,maxT)
               #Muestra en la consola los valores maximos
               App.Console.PrintMessage('\nVALORES MAXIMOS:'+\
                                        '\n maxVxy='+str(maxVxy)+'  x='+str(x[iVxy])+\
                                        '\n maxVxz='+str(maxVxz)+' x='+str(x[iVxz])+\
                                        '\n maxMxy='+str(maxMxy)+' x='+str(x[iMxy])+\
                                        '\n maxMxz='+str(maxMxz)+' x='+str(x[iMxz])+\
                                        '\n maxMtot='+str(maxMtot)+' x='+str(x[iMtot])+\
                                        '\n maxT='+str(maxT)+' x='+str(x[iT]))
               #Encuentra el valor critico en funcion del momento de torsion maximo
               if len(self.vectorCargasXY) == 0 and len(self.vectorCargasT) != 0 : #Solo torsion
                   Txcs=[]
                   for xcs in self.xcs:
                       ixcs=indice(x,xcs/1000)
                       Txcs.append(T[ixcs])
                  #Establece Tcrit como el momento en la seccion critica o el maximo
                   if len(self.vectorSecciones)==1:
                       self.Tcrit=maxT
                   else:
                       self.Tcrit=max(Txcs)
                   #Establece xcrit
                   self.xcrit=x[indice(T,self.Tcrit)]      #[m]
                   #Establece Tcrit, Mxzcrit y Mxycrit en donde es critico
                   self.Mxzcrit=0  #[Nm]
                   self.Mxycrit=0  #[Nm]
                   self.Tcrit=max(abs(T[indice(T,self.Tcrit)]),\
                              abs(T[indice(T,self.Tcrit)+5]),\
                              abs(T[indice(T,self.Tcrit)-5])) #[Nm]

               #Encuentra el valor critico en funcion del momento total maximo
               else: # Torsion y/o Flexion
                   Mtotxcs=[]
                   for xcs in self.xcs:
                       ixcs=indice(x,xcs/1000) #[m]
                       Mtotxcs.append(Mtot[ixcs])
                       App.Console.PrintMessage('\n'+str(xcs)+' '+ str(Mtot[ixcs]))
                   #Establece Mcrit como el momento en la seccion critica o el maximo
                   if len(self.vectorSecciones)==1:
                       self.Mcrit=maxMtot
                   else:
                       self.Mcrit=max(Mtotxcs)
                   #Establece xcrit
                   self.xcrit=x[indice(Mtot,self.Mcrit)]      #[m]
                   #Establece Tcrit, Mxzcrit y Mxycrit en donde es critico
                   self.Mxzcrit=Mxz[indice(Mtot,self.Mcrit)]  #[Nm]
                   self.Mxycrit=Mxy[indice(Mtot,self.Mcrit)]  #[Nm]
                   self.Tcrit=max(abs(T[indice(Mtot,self.Mcrit)]),\
                              abs(T[indice(Mtot,self.Mcrit)+10]),\
                              abs(T[indice(Mtot,self.Mcrit)-10])) #[Nm]

               #Muestra en la consola los valores criticos
               App.Console.PrintMessage('\nVALORES CRITICOS:'+\
                                        '\n xcrit='+str(self.xcrit)+'\n Mcrit='+str(self.Mcrit)+'\n Tcrit='+str(self.Tcrit)+\
                                        '\n Mxzcrit='+str(self.Mxzcrit)+'\n Mxycrit='+str(self.Mxycrit))

               #----Grafica los diagramas de fuerza cortante y momento flector----
               #Limpia y crea los ejes de ploteo
               self.graphics_Diag.canvas.ax.clear()
               self.graphics_Diag.canvas.ax.set_axis_off()
               ax1 = self.graphics_Diag.canvas.fig.add_subplot(211)
               ax2 = self.graphics_Diag.canvas.fig.add_subplot(212, sharex=ax1)
               ax1.clear()
               ax2.clear()
               ax1.tick_params(labelsize=8)
               ax2.tick_params(labelsize=8)
               #Muestra el titulo de los graficos
               ax1.set_title('Fuerza Cortante vs X',fontsize=10)
               ax2.set_title('Momento Flector vs X',fontsize=10)
               #Nombra los ejes
               ax1.set_ylabel('V[N]',fontsize=8,labelpad=-2)
               ax2.set_xlabel('x[m]',fontsize=8,labelpad=-1)
               #Define una funcion para mostrar una anotacion de los valores en los graficos
               def anotacion(ax,matriz,i):
                   #Muestra los valores maximos
                   ax.annotate(str(round(abs(matriz[i]),2)), xy=(x[i], matriz[i]),\
                                xytext=(0,2), textcoords='offset points', size=8, ha='center',\
                                va='bottom', bbox=dict(boxstyle='round,pad=0.2', fc='yellow'))
                   #Muestra los valores para los cambios de seccion
                   for xcs in self.xcs:
                       ixcs=indice(x,xcs/1000) #[m]
                       ax.annotate(str(round(abs(matriz[ixcs]),2)), xy=(x[ixcs], matriz[ixcs]),\
                                    xytext=(0,2), textcoords='offset points', size=8, ha='center',\
                                    va='bottom', bbox=dict(boxstyle='round,pad=0.2', fc='white'))
               #Selecciona que se va a graficar
               if self.radio_XZ.isChecked():
                   #Grafica los diagramas en el plano XZ
                   ax1.fill(x,Vxz,alpha=0.5)
                   ax2.fill(x,Mxz,'r',alpha=0.5)
                   #Establece los limites del eje y de los graficos
                   ax1.set_ylim(-maxVxz-0.2*maxVxz,maxVxz+0.2*maxVxz)
                   ax2.set_ylim(-maxMxz-0.2*maxMxz,maxMxz+0.2*maxMxz)
                   #Muestra los valores maximos
                   anotacion(ax1,Vxz,iVxz)
                   anotacion(ax2,Mxz,iMxz)
                   #Nombra los ejes
                   ax1.set_ylabel('Vz[N]',fontsize=10,labelpad=-2)
                   ax2.set_ylabel('My[Nm]',fontsize=10,labelpad=-2)
               elif self.radio_XY.isChecked():
                   #Grafica los diagramas en el plano XY
                   ax1.fill(x,Vxy,alpha=0.5)
                   ax2.fill(x,Mxy,'r',alpha=0.5)
                   #Establece los limites del eje y de los graficos
                   ax1.set_ylim(-maxVxy-0.2*maxVxy,maxVxy+0.2*maxVxy)
                   ax2.set_ylim(-maxMxy-0.2*maxMxy,maxMxy+0.2*maxMxy)
                   #Indica los valores maximos
                   anotacion(ax1,Vxy,iVxy)
                   anotacion(ax2,Mxy,iMxy)
                   #Nombra los ejes
                   ax1.set_ylabel('Vy[N]',fontsize=10,labelpad=-2)
                   ax2.set_ylabel('Mz[Nm]',fontsize=10,labelpad=-2)
               elif self.radio_TT.isChecked():
                   #Verifica el equilibrio en las cargas de Torsion
                   sumT=0
                   for carga in vectorCargasT:
                      sumT+=carga.m
                   if round(sumT,1) == 0 and len(vectorCargasT) > 1:
                       #Grafica el diagrama de Torsion
                       ax1.fill(x,T,'g',alpha=0.8)
                       #Indica los valores maximos
                       anotacion(ax1,T,iT)
                       #Establece los limites del eje y del grafico
                       ax1.set_ylim(-maxT-0.2*maxT,maxT+0.2*maxT)
                   else:
                       self.statusBar().showMessage('Las cargas de Torsion no se encuentran en equilibrio.', 2000)
                   #Grafica el diagrama de Momentos Totales
                   ax2.fill(x,Mtot,'r',alpha=0.8)
                   #Establece los limites del eje y del grafico
                   ax2.set_ylim(-maxMtot/2-0.2*maxMtot,maxMtot+0.3*maxMtot)
                   #Indica los valores maximos
                   anotacion(ax2,Mtot,iMtot)
                   #Muestra el titulo de los graficos
                   ax1.set_title('Momento Torsor vs X',fontsize=10)
                   ax2.set_title('Momento Flector Total vs X',fontsize=10)
                   #Nombra los ejes
                   ax1.set_ylabel('Mx[Nm]',fontsize=10,labelpad=-2)
                   ax2.set_ylabel('Mtot[Nm]',fontsize=10,labelpad=-2)

               #Muestra una linea vertical por cada cambio de seccion
               for xcs in self.xcs:
                   ax1.axvline(x=xcs/1000,linewidth=0.5,color='k',dashes=[5,2,10,5]) #[m]
                   ax2.axvline(x=xcs/1000,linewidth=0.5,color='k',dashes=[5,2,10,5]) #[m]
               #Establece los limites del eje x en los graficos
               ax2.set_xlim(0, self.longeje()/1000) #[m]
               #Activa las rejillas en ambos subgraficos
               ax1.grid(True)
               ax2.grid(True)
               #Desactiva la etiqueta del eje x del diagrama de cortante o torsion
               ax1.xaxis.set_visible(False)
               #Redibuja el lienzo
               self.graphics_Diag.canvas.draw()

               #----Representa en 3D los diagramas de momentos flectores----
               #Inicializa un vector para los diagramas de momento flector en 3D
               puntos = []
               #Agrega el punto de origen
               puntos.append(FreeCAD.Vector(0,0,0))
               #Anade los puntos calculados a lo largo de x para el plano XY
               for i in range(len(x)):
                   puntos.append(FreeCAD.Vector(x[i]*1000,Mxy[i],0)) #[mm]
               #Anade al vector el punto final x, y el origen para cerrar la curva
               puntos.append(FreeCAD.Vector(x[-1]*1000,0,0))
               puntos.append(FreeCAD.Vector(0,0,0))
               #Anade los puntos calculados a lo largo de x para el plano XY
               for i in range(len(x)):
                   puntos.append(FreeCAD.Vector(x[i]*1000,0,Mxz[i])) #[mm]
               #Anade al vector el punto final x para cerrar la curva
               puntos.append(FreeCAD.Vector(x[-1]*1000,0,0))
               #Crea una curva a partir de los puntos
               curva = Part.makePolygon(puntos)
               #Asigna el eje a la forma inicializada
               self.miDiag.Shape = curva

               #----Grafica la seccion critica, el punto critico y el circulo de Mohr----
               self.calcularDE()

               #----Calcula los graficos de la pestana Diseno Dinamico----
               #Para Material Ductil
               if self.mat[2][self.combo_Mat.currentText()[5:]] != '--':
                   self.calcularDD()

           else:
               self.statusBar().showMessage("Error: Apoyos fuera del eje.", 2000)

   def desactradio(self,n):
       '''Metodo para activar y desactivar los radios de las teorias de falla
       segun el tipo de material seleccionado y habilita o deshabilita el disenio
       dinamico.'''
       #Asigna las propiedades del material actual
       self.matprop=[]
       for i in range(1,4):
           self.matprop.append(self.mat[i][self.combo_Mat.currentText()[5:]])
       #Activa y desactiva los radios
       if self.mat[2][self.mat[0][n][5:]]!='--':
           #Material Ductil
           self.radio_ED.setChecked(True)
           self.radio_ECM.setEnabled(True)
           self.radio_ED.setEnabled(True)
           self.radio_CMD.setEnabled(True)
           self.radio_ENM.setEnabled(False)
           self.radio_CMF.setEnabled(False)
           self.radio_MM.setEnabled(False)
           self.dDinamicoTab.setEnabled(True)
           self.checkBox.setEnabled(True)
           self.checkBox.setChecked(False)
       else:
           #Material Fragil
           self.radio_CMF.setChecked(True)
           self.radio_ECM.setEnabled(False)
           self.radio_ED.setEnabled(False)
           self.radio_CMD.setEnabled(False)
           self.radio_ENM.setEnabled(True)
           self.radio_CMF.setEnabled(True)
           self.radio_MM.setEnabled(True)
           self.dDinamicoTab.setEnabled(False)
           self.checkBox.setEnabled(False)
           self.checkBox.setChecked(True)
           
   def calcularDE(self):
       '''Metodo que calcula los coeficientes de concentracion de esfuerzos,
       la seccion critica, el circulo de Mohr y las teorias de falla.'''
       #----Calculo de Kt y Kts----
       #Comprueba el tipo de material
       #Material Ductil sin coeficientes
       if self.mat[2][self.combo_Mat.currentText()[5:]] != '--' and self.checkBox.isChecked() == False: 
           self.Kt=1
           self.Kts=1
       #Verifica si existe concentrador de esfuerzos en el Material Fragil o Material Ductil con concentradores
       elif self.xcrit*1000 in self.xcs: 
           d1=self.vectorSecciones[indice(self.xcs,self.xcrit*1000)/2].r*2
           d2=self.vectorSecciones[indice(self.xcs,self.xcrit*1000)/2+1].r*2
           if d1 > d2:
               D=d1
               d=d2
           else:
               D=d2
               d=d1
           self.KtKtsUi.D=D      
           self.KtKtsUi.d=d
           self.KtKtsUi.r=self.r

           self.KtKtsUi.hombro()
           self.Kt=self.KtKtsUi.Kt
           self.Kts=self.KtKtsUi.Kts
       #Barra Solida sin cambios de seccion
       else:
           self.Kt=1
           self.Kts=1

       #----Calculo de Seccion Critica----
       #Limpia y crea los ejes de ploteo
       ax_scrit=self.graphics_SCrit.canvas.ax
       ax_scrit.clear()
       s=scrit(ax_scrit,self.Mxycrit,self.Mxzcrit,self.Tcrit,self.Kt,self.Kts)
       #Extrae los valores de sigma x y tauxz de la funcion
       self.sigmax=s[0]
       self.tauxz=s[1]
       #Muestra en las etiquetas respectivas los valores calculados
       self.label_Sigmax.setText(self.label_Sigmax.text()[0:3]+\
                                 '\n'+str(round(self.sigmax,2))+'/d^3')
       self.label_Tauxz.setText(self.label_Tauxz.text()[0:6]+\
                                 ' \n'+str(round(self.tauxz,2))+'/d^3')
       self.label_xcrit.setText('x:\n'+str(round(self.xcrit*1000,2))+'[mm]')

       App.Console.PrintMessage('\nSigmax='+str(self.sigmax)+\
                                '\nTauxz='+str(self.tauxz)+\
                                 '\nxcrit='+str(self.xcrit))

       #----Calculo de Esfuerzos Principales----
       #Prepara los ejes de ploteo
       self.graphics_CMohr.canvas.ax.clear()
       self.graphics_CMohr.canvas.ax.set_axis_off()
       ax_cmohr=self.graphics_CMohr.canvas.fig.add_axes([.15,.09,0.8,0.6])
       #ax_cmohr.canvas.fig.autofmt_xdate()
       ax_pcrit=self.graphics_CMohr.canvas.fig.add_axes([0.05,.6,0.9,0.5])#1.8
       ax_cmohr.clear()
       ax_pcrit.clear()
       ax_cmohr.tick_params(labelsize=8)
       #Grafica el Circulo de Mohr
       cm=cmohr(ax_cmohr,self.sigmax,self.tauxz)
       #Extrae los valores calculados
       self.sigma1=cm[0]
       self.sigma2=cm[1]
       self.tau12=cm[2]
       self.sigmaT=cm[3]
       self.phi=cm[4]
       #Grafica los Elementos de Esfuerzo
       elementos(ax_pcrit,self.sigmax,self.tauxz,self.sigma1,self.sigma2,\
                 self.tau12,self.sigmaT,self.phi)
       #Muestra en las etiquetas respectivas los valores calculados
       self.label_Sigma1.setText(self.label_Sigma1.text()[0:3]+\
                                 '\n'+str(round(self.sigma1,2))+'/d^3')
       self.label_Sigma2.setText(self.label_Sigma2.text()[0:3]+\
                                 '\n '+str(round(self.sigma2,2))+'/d^3')
       self.label_SigmaTau.setText(self.label_SigmaTau.text()[0:3]+\
                                 '\n'+str(round(self.sigmaT,2))+'/d^3')
       self.label_Tau12.setText(self.label_Tau12.text()[0:6]+\
                                 '\n'+str(round(self.tau12,2))+'/d^3')
       self.label_phi.setText(self.label_phi.text()[0:2]+\
                                 '\n'+str(round(self.phi,2))+'[grad]')

       App.Console.PrintMessage('\nSigma1='+str(self.sigma1)+\
                                '\nSigma2='+str(self.sigma2)+\
                                '\nSigmaTau='+str(self.sigmaT)+\
                                '\nTau12='+str(self.tau12)+\
                                '\nPhi='+str(self.phi))

       self.graphics_CMohr.canvas.draw()
       self.graphics_SCrit.canvas.draw()
       #Grafica las teorias de falla segun el material
       self.calcularTF()

   def ka(self):
       '''Calcula el factor modificador de la resistencia a la fatiga por
       acabado superficial.'''
       #Muestra un dialogo con un combo y botones de aceptar y cancelar
       ka_acabado=QtGui.QInputDialog.getItem(None, "ka-Factor de Superficie",\
                                   "Seleccione el acabado superficial:",\
                                   ('Esmerilado','Maquinado o Laminado en Frio',\
                                    'Laminado en Caliente','Como sale de la Forja'),\
                                    editable=False)
       if ka_acabado[1]: #Al presionar Aceptar
           #Extrae la informacion del dialogo
           acabado=ka_acabado[0]
           #Calcula el coeficiente de correccion
           Sut=self.matprop[0]
           ka=calc_ka(acabado,Sut)
           #Agrega a la lista de coeficientes
           self.ks['ka']=ka
           #Actualiza el valor de la etiqueta
           self.label_ka.setText(str(round(ka,3)))
           #Recalcula la resistencia a la fatiga
           self.calcularRF()
           #Muestra la informacion en la consola
           App.Console.PrintMessage('\nAcabado:\n'+str(acabado)+\
                                    '\nka='+str(round(ka,3)))

   def kb(self):
       '''Calcula el factor modificador de la resistencia a la fatiga por
       tamanio.'''
       #Muestra un dialogo que toma un dato de entrada
       kb_d=QtGui.QInputDialog.getDouble(None, "kb-Factor de Tamano",\
                                   "Establezca el diametro para iterar:",\
                                   value=round(self.dcrit,2),\
                                   minValue=2.8,maxValue=254,decimals=2)
       if kb_d[1]: #Al presionar Aceptar
           #Extrae la informacion del dialogo
           self.d_iter=kb_d[0]
           #Calcula el coeficiente de correccion
           kb=calc_kb(self.d_iter)
           #Agrega a la lista de coeficientes
           self.ks['kb']=kb
           #Actualiza el valor de la etiqueta
           self.label_kb.setText(str(round(kb,3)))
           #Recalcula la resistencia a la fatiga
           self.calcularRF()
           #Muestra la informacion en la consola
           App.Console.PrintMessage('\nDiametro iteracion:\n'+\
                                     str(self.d_iter)+'\nkb='+str(round(kb,3)))
            
   def kc(self):
       '''Calcula el factor modificador de la resistencia a la fatiga por
       tipo de carga.'''
       carga='Flexion'
       #Calcula el coeficiente de correccion
       kc=calc_kc(carga)
       #Agrega a la lista de coeficientes
       self.ks['kc']=kc
       #Actualiza el valor de la etiqueta
       self.label_kc.setText(str(round(kc,3)))
       #Recalcula la resistencia a la fatiga
       self.calcularRF()
       #Muestra la informacion en la consola
       App.Console.PrintMessage('\nkc='+str(round(kc,3)))
            

   def kd(self):
       '''Calcula el factor modificador de la resistencia a la fatiga por
       temperatura.'''
       #Muestra un dialogo que toma un dato de entrada
       kd_T=QtGui.QInputDialog.getDouble(None, "kb-Factor de Temperatura",\
                                   "Establezca la temperatura de trabajo:",\
                                   value=20,minValue=20,maxValue=500,decimals=2)
       if kd_T[1]: #Al presionar Aceptar
           #Extrae la informacion del dialogo
           Temp=kd_T[0]
           #Calcula el coeficiente de correccion
           kd=calc_kd(Temp)
           #Agrega a la lista de coeficientes
           self.ks['kd']=kd
           #Actualiza el valor de la etiqueta
           self.label_kd.setText(str(round(kd,3)))
           #Recalcula la resistencia a la fatiga
           self.calcularRF()
           
           #Muestra la informacion en la consola
           App.Console.PrintMessage('\nTemperatura de trabajo:\n'+str(Temp)+\
                                    '\nkd='+str(round(kd,3)))

   def ke(self):
       '''Calcula el factor modificador de la resistencia a la fatiga por
       confiabilidad.'''
       #Muestra un dialogo con un combo y botones de aceptar y cancelar
       ke_confiabilidad=QtGui.QInputDialog.getItem(None, "ke-Factor de Confiabilidad",\
                                   "Seleccione el porcentaje de Confiabilidad:",\
                                   ('50%','90%','95%','99%','99.9%',\
                                    '99.99%','99.999%','99.9999%'),editable=False)
       if ke_confiabilidad[1]: #Al presionar Aceptar
           #Extrae la informacion del dialogo
           confiabilidad=ke_confiabilidad[0]
           #Calcula el coeficiente de correccion
           ke=calc_ke(confiabilidad)
           #Agrega a la lista de coeficientes
           self.ks['ke']=ke
           #Actualiza el valor de la etiqueta
           self.label_ke.setText(str(round(ke,3)))
           #Recalcula la resistencia a la fatiga
           self.calcularRF()
           #Muestra la informacion en la consola
           App.Console.PrintMessage('\nConfiabilidad:\n'+str(confiabilidad)+\
                                     '\nke='+str(round(ke,3)))

   def kf(self):
       '''Calcula el factor modificador de la resistencia a la fatiga por
       otros factores.'''
       #Muestra un dialogo que toma un dato de entrada
       kf_varios=QtGui.QInputDialog.getDouble(None, "kf-Factor de Efectos Varios",\
                                   "Establezca el valor del coeficiente kf:",\
                                   value=1,minValue=0,decimals=2)
       if kf_varios[1]: #Al presionar Aceptar
           #Extrae la informacion del dialogo
           kf=kf_varios[0]
           #Agrega a la lista de coeficientes
           self.ks['kf']=kf
           #Actualiza el valor de la etiqueta
           self.label_kf.setText(str(round(kf,3)))
           #Recalcula la resistencia a la fatiga
           self.calcularRF()
           #Muestra la informacion en la consola
           App.Console.PrintMessage('\nkf:\n'+str(round(kf,3)))


   def calcularDD(self):
       '''Metodo que calcula los coeficientes de concentracion de esfuerzos 
       corregidos para fatiga, los esfuerzos fluctuantes y la resistencia a la fatiga.'''
       #----Calculo de Kf y Kfs----
       #Verifica si existe concentrador de esfuerzos
       if self.xcrit*1000 in self.xcs: 
           d1=self.vectorSecciones[indice(self.xcs,self.xcrit*1000)/2].r*2
           d2=self.vectorSecciones[indice(self.xcs,self.xcrit*1000)/2+1].r*2
           if d1 > d2:
               D=d1
               d=d2
           else:
               D=d2
               d=d1
           self.KtKtsUi.D=D      
           self.KtKtsUi.d=d
           self.KtKtsUi.r=self.r

           self.KtKtsUi.hombro()
           self.Kt=self.KtKtsUi.Kt
           self.Kts=self.KtKtsUi.Kts
           
           self.dcrit=d
           #Calculo de los concentradores de esfuerzos a Fatiga
           Sut=self.matprop[0]
           r=self.KtKtsUi.r
           self.Kf=kf(self.Kt,self.Kts,Sut,r)[0]
           self.Kfs=kf(self.Kt,self.Kts,Sut,r)[1]

       #Barra Solida sin cambios de seccion
       else:
           self.Kt=1
           self.Kts=1
           self.Kf=1
           self.Kfs=1

           self.dcrit=self.vectorSecciones[0].r*2

       App.Console.PrintMessage('\nKf='+str(self.Kf)+\
                                '\nKfs='+str(self.Kfs))

       #----Calculo de Esfuerzos Fluctuantes----
       #Prepara los ejes de ploteo
       self.graphics_Fluct.canvas.ax.clear()
       self.graphics_Fluct.canvas.ax.set_axis_off()
       ax=self.graphics_Fluct.canvas.fig.add_axes([0.05,0.03,.9,.9])
       ax_ftau=self.graphics_Fluct.canvas.fig.add_axes([0.05,0.03,.9,.45])
       ax_fsigma=self.graphics_Fluct.canvas.fig.add_axes([0.05,.52,.9,.45])
       ax_ftau.clear()
       ax_fsigma.clear()
       #Verifica si se encuentra sometido solo a torsion, solo a flexion o a ambas
       if len(self.vectorCargasXY) == 0: #Solo Torsion
           #Grafica los Esfuerzos Fluctuantes
           self.graphics_Fluct.canvas.ax.clear()
           f=fluct(ax_fsigma,ax,self.Mcrit,self.Tcrit,self.Kf,self.Kfs)
           ax_fsigma.set_axis_off()
       elif len(self.vectorCargasT) == 0: #Solo Flexion
           #Grafica los Esfuerzos Fluctuantes
           ax_fsigma.set_axis_off()
           ax_ftau.set_axis_off()
           f=fluct(ax,ax_ftau,self.Mcrit,self.Tcrit,self.Kf,self.Kfs)
           ax_ftau.set_axis_off()
       else: # Torsion y Flexion
           #Grafica los Esfuerzos Fluctuantes
           ax.set_axis_off()
           f=fluct(ax_fsigma,ax_ftau,self.Mcrit,self.Tcrit,self.Kf,self.Kfs)
           #f=fluct(ax_fsigma,ax_ftau,1000,600,1,1)
       #Extrae los valores calculados
       self.sigma_a=f[0]
       self.tau_m=f[1]
           #Muestra en las etiquetas respectivas los valores calculados
       self.label_Sigma_a.setText(self.label_Sigma_a.text()[0:3]+\
                                 '\n'+str(round(self.sigma_a,2))+'/d^3')
       self.label_Tau_m.setText(self.label_Tau_m.text()[0:3]+\
                                 '\n'+str(round(self.tau_m,2))+'/d^3')
       App.Console.PrintMessage('\nSigma_a='+str(self.sigma_a)+\
                                '\nTau_m='+str(self.tau_m))
       #----Calculo de la Resistencia a la Fatiga----
       self.calcularRF()

       self.graphics_Fluct.canvas.draw()

   def calcularTF(self):
       '''Este metodo calcula y grafica las teorias de falla tomando en cuenta 
       el radio seleccionado.'''
       #----Grafica de Teorias de Falla----
       #Prepara los ejes de ploteo
       self.graphics_TFalla.canvas.ax.clear()
       ax_tfalla=self.graphics_TFalla.canvas.ax
       #self.graphics_TFalla.canvas.ax.set_axis_off()
       #ax_tfalla=self.graphics_TFalla.canvas.fig.add_axes([0.05,.1,0.9,0.8])
       ax_tfalla.clear()
       ax_tfalla.tick_params(labelsize=8)
       #Extrae las propiedades del material seleccionado

       Sut=self.matprop[0]
       Sy=self.matprop[1]
       Suc=self.matprop[2]
       Syc=Sy

       #Grafica las teorias de falla segun el material
       tfallaG(ax_tfalla,self.sigma1,self.sigma2,self.matprop)
       #Resalta la teoria de falla seleccionada
       if self.radio_ECM.isChecked():
           ax_tfalla.plot([-Sy,0,Sy,Sy,0,-Sy,-Sy],\
                [0,Sy,Sy,0,-Sy,-Sy,0],'r-', linewidth=1.5)
       elif self.radio_ED.isChecked():
           ED=Ellipse((0,0),(2*sqrt(2))*Sy, (2*sqrt(2.0/3))*Sy,\
                     angle=45,linewidth=1.5,fill=False)
           ED.set_edgecolor('r')
           ax_tfalla.add_patch(ED)
       elif self.radio_CMD.isChecked():
           ax_tfalla.plot([-Syc,0,Sy,Sy,0,-Syc,-Syc],\
                [0,Sy,Sy,0,-Syc,-Syc,0],'r-', linewidth=1.5)
       elif self.radio_ENM.isChecked():
           ENM = Rectangle((-Suc,-Suc),Sut+Suc,Sut+Suc,\
                            facecolor='white',linewidth=1.5)
           ENM.set_edgecolor('r')
           ax_tfalla.add_patch(ENM)
       elif self.radio_CMF.isChecked():
           ax_tfalla.plot([-Suc,0,Sut,Sut,0,-Suc,-Suc],\
                    [0,Sut,Sut,0,-Suc,-Suc,0],'r-', linewidth=1.5)
       elif self.radio_MM.isChecked():
           ax_tfalla.plot([-Suc,-Sut,Sut,Sut,0,-Suc,-Suc],\
                [0,Sut,Sut,-Sut,-Suc,-Suc,0],'r-', linewidth=1.5)

       self.graphics_TFalla.canvas.draw()

   def calcularRF(self):
       '''Genera un grafico a partir de los calculos de la resistencia a la fatiga
       que tambien se realizan con esta funcion.'''
       #----Calculo de la Resistencia a la Fatiga----
       try:
           #Valida si los datos de entrada son numericos
           float(self.label_ka.text())
           float(self.label_kb.text())
           float(self.label_kc.text())
           float(self.label_kd.text())
           float(self.label_ke.text())
           float(self.label_kf.text())
       except ValueError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Establezca los valores de los coeficientes de Marin.", 2000)
       else:
           ks=self.ks.values()
           #Prepara los ejes de ploteo
           self.graphics_RFatiga.canvas.ax.clear()
           self.graphics_RFatiga.canvas.ax.set_axis_off()
           ax_RF=self.graphics_RFatiga.canvas.fig.add_axes([0.05,0.05,.9,.9])
           ax_RF.clear()
           #Grafica la Resistencia a la Fatiga de una Probeta
           App.Console.PrintMessage('\nks:\n'+str(self.ks)) 
           Sut=self.matprop[0]
           rf=se(ax_RF,Sut,self.ks)
           #Extrae los valores calculados
           self.se=rf[0]
           self.sep=rf[1]
           #Muestra en las etiquetas respectivas los valores calculados
           self.label_Sut.setText('Sut:\n'+str(round(Sut,2))+'[MPa]')
           self.label_Sep.setText("Se':\n"+str(round(self.sep,2))+'[MPa]')
           self.label_Se_2.setText("Se: "+str(round(self.se,2))+'[MPa]')
           #Habilita el uso de los criterios de Falla
           self.group_CFalla.setEnabled(True)
           self.calcularCF()

           App.Console.PrintMessage('\nSe='+str(self.se)+\
                                    "\nSe'="+str(self.sep))
           self.graphics_RFatiga.canvas.draw()

   def calcularCF(self):
       '''Segun el criterio de falla seleccionado calcula y grafica las curvas
       correspondientes.'''
       #----Grafica de Criterios de Falla----
       #Prepara los ejes de ploteo
       self.graphics_CFalla.canvas.ax.clear()
       self.graphics_CFalla.canvas.ax.set_axis_off()
       ax_CF=self.graphics_CFalla.canvas.fig.add_axes([0.15,0.15,.8,.8])
       #ax_CF=self.graphics_CFalla.canvas.ax
       ax_CF.clear()

       #Extrae las propiedades del material seleccionado
       '''
       self.Mcrit=1000
       self.Tcrit=600
       self.Kf=1
       self.Kfs=1
       self.Se=150
       self.matprop=[300,200,500]
       '''
       #Grafica las teorias de falla segun el material
       c=criteriosG(ax_CF,self.Mcrit,self.Tcrit,\
                    self.Kf,self.Kfs,self.se,self.matprop)
       #Extrae los valores calculados
       self.sigma_ap=c[0]
       self.sigma_mp=c[1]
       App.Console.PrintMessage("\ns_a'="+str(self.sigma_ap)+\
                                "\ns_m'="+str(self.sigma_mp))
       #Muestra en las etiquetas respectivas los valores calculados
       self.label_Sigma_ap.setText(self.label_Sigma_ap.text()[0:4]+\
                                 '\n'+str(round(self.sigma_ap,2))+'/d^3')
       self.label_Sigma_mp.setText(self.label_Sigma_mp.text()[0:4]+\
                                 '\n'+str(round(self.sigma_mp,2))+'/d^3')
       #Resalta la teoria de falla seleccionada
       Sut=float(self.matprop[0])
       Sy=float(self.matprop[1])
       Se=self.se
       if self.radio_Goodman.isChecked():
           ax_CF.plot([0,Sut],[Se,0],'r-', lw=1.2)
       elif self.radio_Gerber.isChecked():
           x=np.linspace(0, round(Sut), 1000)
           y=Se*(1-(x/Sut)**2)
           ax_CF.plot(x, y,'r-',lw=1.2)
       elif self.radio_Soderberg.isChecked():
           ax_CF.plot([0,Sy],[Se,0],'r-', lw=1.2)
       elif self.radio_ASME.isChecked():
           x=np.linspace(0, round(Sy), 1000)
           y=Se*(1-(x/Sy)**2)**(1/2.0)
           ax_CF.plot(x, y,'r',lw=1.2)

       self.graphics_CFalla.canvas.draw()

   def calcdcritDE(self):
       '''Calcula el diametro estatico segun la teoria de falla seleccionada.'''
       try:
           #Valida si los datos de entrada son numericos
           n = float(self.edit_n.text())
           n**(-1/2.0)
       except ValueError:
           self.statusBar().showMessage("Ingrese valores numericos validos para n", 2000)
       except ZeroDivisionError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Error: Los valores no pueden ser cero.", 2000)
       else:
           #Recalcula todos los valores
           self.calcularDE()
           #Calcula el diametro para la teoria de falla seleccionada
           Sut=self.matprop[0]
           Sy=self.matprop[1]
           Suc=self.matprop[2]
           Syc=Sy

           if self.radio_ECM.isChecked():
               self.dcrit=dECM(self.sigma1,self.sigma2,float(Sy),n)*10
               self.edit_dEstatico.setText(str(round(self.dcrit,3))+'[mm]')
           elif self.radio_ED.isChecked():
               self.dcrit=dED(self.sigma1,self.sigma2,float(Sy),n)*10
               self.edit_dEstatico.setText(str(round(self.dcrit,3))+'[mm]')
           elif self.radio_CMD.isChecked():
               self.dcrit=dCM(self.sigma1,self.sigma2,float(Sy),float(Syc),n)*10
               self.edit_dEstatico.setText(str(round(self.dcrit,3))+'[mm]')
           elif self.radio_ENM.isChecked():
               self.dcrit=dENM(self.sigma1,self.sigma2,float(Sut),float(Suc),n)*10
               self.edit_dEstatico.setText(str(round(self.dcrit,3))+'[mm]')
           elif self.radio_CMF.isChecked():
               self.dcrit=dCM(self.sigma1,self.sigma2,float(Sut),float(Suc),n)*10
               self.edit_dEstatico.setText(str(round(self.dcrit,3))+'[mm]')
           elif self.radio_MM.isChecked():
               self.dcrit=dMM(self.sigma1,self.sigma2,float(Sut),float(Suc),n)*10
               self.edit_dEstatico.setText(str(round(self.dcrit,3))+'[mm]')
           App.Console.PrintMessage('\nd='+str(self.dcrit)+'[mm]')
           #Anade las secciones preferidas a la lista
           self.list_Secciones_DE.clear()
           secs=secpref(self.vectorSecciones,1000*self.xcrit,self.dcrit)
           for i in range(len(secs)):
               self.list_Secciones_DE.addItem('S'+str(i+1)+': '+str(secs[i])+'[mm]')
 
   def calcdcritDD(self):
       '''Calcula el diametro dinamico segun el criterio de falla a la fatiga 
       seleccionado.'''
       try:
           #Valida si los datos de entrada son numericos
           n = float(self.edit_nD.text())
           tol = float(self.tol)
           n**(-1/2.0)
           tol**(-1/2.0)

       except ValueError:
           self.statusBar().showMessage("Ingrese valores numericos validos para n o tol", 2000)
       except ZeroDivisionError:
           #Muestra un mensaje en la barra de estado
           self.statusBar().showMessage("Error: Los valores no pueden ser cero ni negativos.", 2000)
       else:
           #Recalcula todos los valores
           self.calcularDD()
           #Calcula el diametro para el criterio de falla seleccionado
           Sut=self.matprop[0]
           Sy=self.matprop[1]
           Suc=self.matprop[2]
           Syc=Sy

           if self.radio_Goodman.isChecked():
               self.d_iter=dGoodman(self.sigma_ap,self.sigma_mp,self.se,Sut,n)*10
               self.edit_dDinamico.setText(str(round(self.d_iter,3))+'[mm]')
           elif self.radio_Gerber.isChecked():
               self.d_iter=dGerber(self.sigma_ap,self.sigma_mp,self.se,Sut,n)*10
               self.edit_dDinamico.setText(str(round(self.d_iter,3))+'[mm]')
           elif self.radio_Soderberg.isChecked():
               self.d_iter=dSoderberg(self.sigma_ap,self.sigma_mp,self.se,Sy,n)*10
               self.edit_dDinamico.setText(str(round(self.d_iter,3))+'[mm]')
           elif self.radio_ASME.isChecked():
               self.d_iter=dASME(self.sigma_ap,self.sigma_mp,self.se,Sy,n)*10
               self.edit_dDinamico.setText(str(round(self.d_iter,3))+'[mm]')
           App.Console.PrintMessage('\nd='+str(self.d_iter)+'[mm]')
           #Anade las secciones preferidas a la lista
           self.list_Secciones_DD.clear()
           secs=secpref(self.vectorSecciones,1000*self.xcrit,self.d_iter)
           for i in range(len(secs)):
               self.list_Secciones_DD.addItem('S'+str(i+1)+': '+str(secs[i])+'[mm]')


       
   def recalc(self):
       '''Toma el diametro estatico y lo usa como referencia para dimensionar 
       las otras secciones. Crea un nuevo solido con las nuevas secciones.'''
       #Extrae el diametro de cada seccion y calcula su tamanio preferido
       secs=secpref(self.vectorSecciones,1000*self.xcrit,self.dcrit)
       #Vacia la lista y encera los valores de las secciones mostradas en configuracion.
       self.list_Secciones.clear()
       self.numsec=0
       #Agrega los diametros preferidos a la configuracion
       for i in range(len(self.vectorSecciones)):
           self.vectorSecciones[i].r=secs[i]/2
           self.numsec+=1
           self.list_Secciones.addItem('S'+str(self.numsec)+': '+\
            							str(self.vectorSecciones[i]))
       #Mantiene la relacion h/r
       rhr = self.KtKtsUi.h / self.KtKtsUi.r
       #Cambia a la ventana de configuracion
       self.tabWidget.setCurrentIndex(0)
       #Crea el eje con las nuevas secciones
       self.creareje()
       #Calcula nuevamente con las nuevas dimensiones
       self.calcdcritDE()
       #Establece el valor del radio para que se mantenga la relacion h/r
       self.dspinbox_rda.setValue(round(self.KtKtsUi.h/rhr,2))
       #Crea el eje con el nuevo radio de entalle
       self.creareje()
       #Cambia a la ventana de  disenio estatico
       self.tabWidget.setCurrentIndex(2)
       #Recalcula con ese radio
       self.calcdcritDE()
 
   def recalcD(self):
       '''Toma el diametro dinamico y lo usa como referencia para dimensionar 
       las otras secciones. Crea un nuevo solido con las nuevas secciones.'''
       #Extrae el diametro de cada seccion y calcula su tamanio preferido
       secs=secpref(self.vectorSecciones,1000*self.xcrit,self.d_iter)
       #Vacia la lista y encera los valores de las secciones mostradas en configuracion.
       self.list_Secciones.clear()
       self.numsec=0
       #Agrega los diametros preferidos a la configuracion
       for i in range(len(self.vectorSecciones)):
           self.vectorSecciones[i].r=secs[i]/2
           self.numsec+=1
           self.list_Secciones.addItem('S'+str(self.numsec)+': '+\
            							str(self.vectorSecciones[i]))
       #Mantiene la relacion h/r
       rhr = self.KtKtsUi.h / self.KtKtsUi.r
       #Cambia a la ventana de configuracion
       self.tabWidget.setCurrentIndex(0)
       #Crea el eje con las nuevas secciones
       self.creareje()
       #Calcula nuevamente con las nuevas dimensiones
       self.calcdcritDD()
       #Establece el valor del radio para que se mantenga la relacion h/r
       self.dspinbox_rda.setValue(round(self.KtKtsUi.h/rhr,2))
       #Crea el eje con el nuevo radio de entalle
       self.creareje()
       #Muestra para actualizar el valor de kb
       self.kb()
       #Cambia a la ventana de  disenio dinamico
       self.tabWidget.setCurrentIndex(3)
       #Recalcula con ese radio
       self.calcdcritDD()

   def ver_ktkts(self):
       '''Muestra el formulario que corresponde a los coeficientes de concentracion 
       de esfuerzos.'''
       self.calcular()
       #Comprueba el tipo de material
       if self.mat[2][self.combo_Mat.currentText()[5:]] != '--' and self.checkBox.isChecked() == False:
           #Muestra un mensaje si el material es ductil
           QtGui.QMessageBox.information(None,"Kt-Kts:",\
             'Para el material seleccionado y cargas estaticas no se aplican los factores de concentracion de esfuerzos.'+\
             '\tKt=1\tKts=1')
       #Verifica si existe concentrador de esfuerzos
       elif self.xcrit*1000 in self.xcs:
           #Muestra el formulario si el material es fragil y posee concentradores.
           self.KtKtsUi.actualizar()
           self.KtKtsUi.show()
       else:
           #Muestra un mensaje si no existen concentradores.
           QtGui.QMessageBox.information(None,"Kt-Kts:",\
             'El eje no presenta concentradores de esfuerzos en la seccion critica'+\
             '\tKt=1\tKts=1')

   def ver_kfkfs(self):
       '''Muestra el formulario que corresponde a los coeficientes de concentracion 
       de esfuerzos corregidos para fatiga.'''
       #Verifica si existe concentrador de esfuerzos
       if self.xcrit*1000 in self.xcs:
           self.KtKtsUi.actualizar()
           self.KtKtsUi.label_Kt.setText('Kf: '+str(round(self.Kf,2)))
           self.KtKtsUi.label_Kts.setText('Kfs: '+str(round(self.Kfs,2)))
           #Muestra el formulario actualizado
           self.KtKtsUi.show()
           
       else:
           #Muestra un mensaje si no existen concentradores
           QtGui.QMessageBox.information(None,"Kt-Kts:",\
             'El eje no presenta concentradores de esfuerzos en la seccion critica'+\
             '\tKt=1\tKts=1')
   def acerca_de(self):
       QtGui.QMessageBox.about(self, "Acerca de EjesDim",
              "EjesDim es un software creado para facilitar \n el diseno de Ejes "+\
              "sometidos tanto a cargas \n estaticas como dinamicas.\n"+\
              "\n	Autor: Edgar Alexis Martinez S."+\
              "\n	Version: 1.0.0 \n	Fecha de Version: 2016-02")


class KtKts_Gui(QtGui.QDialog, Ui_Kt_Kts):
   def __init__(self, parent=None):
       QtGui.QDialog.__init__(self, parent)
       self.setupUi(self)
       #Inicializa cantidades que se usaran en todo el programa
       self.d=0.0
       self.D=0.0
       self.h=0.0
       #Por defecto el radio de entalle r=0
       self.r=0.0
       #Kt y Kts por defecto sin concentradores de tension
       self.Kt=1
       self.Kts=1

       self.dir = os.path.dirname(__file__)
       self.img=matplotlib.image.imread(os.path.join(self.dir+"\Graficos", "Hombro.png"))

       #		-Entrada h
       self.edit_h.setText(str(round(self.h,2)))
       #		-Etiqueta r
       #		-Entrada D
       self.edit_D.setText(str(round(self.D,2)))
       #		-Entrada d
       self.edit_d.setText(str(round(self.d,2)))
       #		-Etiqueta D
       #		-Etiqueta h
       #		-Etiqueta d
       #		-Entrada r
       self.edit_r.setText(str(round(self.r,2)))
       #		-Plot Kt
       self.graphics_Kt.canvas.ax.clear()
       self.graphics_Kt.canvas.ax.set_axis_off()
       ax=self.graphics_Kt.canvas.fig.add_axes([0,0,1,1])
       ax.set_axis_off()
       ax.imshow(self.img)
       #		-Etiqueta Kts
       self.label_Kts.setText('Kt: '+str(round(self.Kts,2)))
       #		-Etiqueta Kt
       self.label_Kt.setText('Kt: '+str(round(self.Kt,2)))
       
   def hombro(self):
       self.Kt=kthombro(self.D,self.d,self.r)[0]
       self.Kts=kthombro(self.D,self.d,self.r)[1]
       self.h=kthombro(self.D,self.d,self.r)[2]
       self.actualizar()

   def actualizar(self):
       #Establece los valores de Kt y Kts en las etiquetas
       self.label_Kt.setText('Kt: '+str(round(self.Kt,2)))
       self.label_Kts.setText('Kts: '+str(round(self.Kts,2)))
       #Muestra los valores geometricos en los cajones
       self.edit_h.setText(str(round(self.h,2)))
       self.edit_D.setText(str(round(self.D,2)))
       self.edit_d.setText(str(round(self.d,2)))
       self.edit_r.setText(str(round(self.r,2)))
       #Muestra los valores en la consola
       App.Console.PrintMessage('\nr:'+str(self.r))
       App.Console.PrintMessage('\nKt:'+str(self.Kt))
       App.Console.PrintMessage('\nKts:'+str(self.Kts))

#Muestra la pantalla de entrada
import time
splashPixmap = QtGui.QPixmap(os.path.dirname(__file__)+'/Graficos/LogoI.png')
splash = QtGui.QSplashScreen(splashPixmap, QtCore.Qt.WindowStaysOnTopHint)
splash.show()
QtGui.QApplication.processEvents()
time.sleep(2)
MW=EjesDim_Gui() #Objeto de inicio de aplicacion
splash.finish(MW)
