# -*- coding: utf-8 -*-
# Created by: PyQt4 UI code generator 4.11.4

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
		#Ventana Principal
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(665, 493)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
		#Zona Central
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(665, 366))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		#Zona Tabs
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

		#-Tab Configuracion
        self.configTab = QtGui.QWidget()
        self.configTab.setObjectName(_fromUtf8("configTab"))
        self.gridLayout = QtGui.QGridLayout(self.configTab)
        self.gridLayout.setContentsMargins(1, 5, 1, 1)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

		#	-Grupo Material
        self.group_Material = QtGui.QGroupBox(self.configTab)
        self.group_Material.setMinimumSize(QtCore.QSize(211, 57))
        self.group_Material.setMaximumSize(QtCore.QSize(211, 57))
        self.group_Material.setObjectName(_fromUtf8("group_Material"))
        self.gridLayout_12 = QtGui.QGridLayout(self.group_Material)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
		#		-Combo Materiales
        self.combo_Mat = QtGui.QComboBox(self.group_Material)
        self.combo_Mat.setObjectName(_fromUtf8("combo_Mat"))
        self.gridLayout_12.addWidget(self.combo_Mat, 2, 0, 1, 2)
		#		-Boton Propiedades
        self.button_Prop = QtGui.QPushButton(self.group_Material)
        self.button_Prop.setMinimumSize(QtCore.QSize(20, 0))
        self.button_Prop.setMaximumSize(QtCore.QSize(20, 16777215))
        self.button_Prop.setObjectName(_fromUtf8("button_Prop"))
        self.gridLayout_12.addWidget(self.button_Prop, 2, 2, 1, 1)

        self.gridLayout.addWidget(self.group_Material, 0, 0, 1, 1)

		#	-Grupo Configuracion Preliminar
        self.group_PrevConfig = QtGui.QGroupBox(self.configTab)
        self.group_PrevConfig.setObjectName(_fromUtf8("group_PrevConfig"))
        self.gridLayout_7 = QtGui.QGridLayout(self.group_PrevConfig)
        self.gridLayout_7.setContentsMargins(1, 0, 1, 5)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
		#		-Plot Configuracion
        self.graphics_Config = Mpl(self.group_PrevConfig)
        self.graphics_Config.setObjectName(_fromUtf8("graphics_Config"))
        self.gridLayout_7.addWidget(self.graphics_Config, 0, 0, 4, 10)
		#		-Etiqueta Soporte 1
        self.label_XR1 = QtGui.QLabel(self.group_PrevConfig)
        self.label_XR1.setObjectName(_fromUtf8("label_XR1"))
        self.gridLayout_7.addWidget(self.label_XR1, 4, 2, 1, 1)
		#		-Entrada Soporte 1
        self.edit_XR1 = QtGui.QLineEdit(self.group_PrevConfig)
        self.edit_XR1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edit_XR1.setObjectName(_fromUtf8("edit_XR1"))
        self.gridLayout_7.addWidget(self.edit_XR1, 4, 3, 1, 1)
		#		-Etiqueta Soporte 2
        self.label_XR2 = QtGui.QLabel(self.group_PrevConfig)
        self.label_XR2.setObjectName(_fromUtf8("label_XR2"))
        self.gridLayout_7.addWidget(self.label_XR2, 4, 5, 1, 1)
		#		-Entrada Soporte 2
        self.edit_XR2 = QtGui.QLineEdit(self.group_PrevConfig)
        self.edit_XR2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.edit_XR2.setObjectName(_fromUtf8("edit_XR2"))
        self.gridLayout_7.addWidget(self.edit_XR2, 4, 6, 1, 1)
		#		-Boton Crear
        self.button_CrearEje = QtGui.QPushButton(self.group_PrevConfig)
        self.button_CrearEje.setObjectName(_fromUtf8("button_CrearEje"))
        self.gridLayout_7.addWidget(self.button_CrearEje, 4, 9, 1, 1)

        self.gridLayout.addWidget(self.group_PrevConfig, 0, 1, 5, 1)

		#	-Grupo Seccion
        self.group_Sec = QtGui.QGroupBox(self.configTab)
        self.group_Sec.setMinimumSize(QtCore.QSize(211, 0))
        self.group_Sec.setMaximumSize(QtCore.QSize(211, 16777215))
        self.group_Sec.setObjectName(_fromUtf8("group_Sec"))
        self.gridLayout_2 = QtGui.QGridLayout(self.group_Sec)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		#		-Etiqueta Diametro
        self.label_D = QtGui.QLabel(self.group_Sec)
        self.label_D.setObjectName(_fromUtf8("label_D"))
        self.gridLayout_2.addWidget(self.label_D, 0, 0, 1, 1)
		#		-Etiqueta Longitud
        self.label_L = QtGui.QLabel(self.group_Sec)
        self.label_L.setObjectName(_fromUtf8("label_L"))
        self.gridLayout_2.addWidget(self.label_L, 0, 3, 1, 1)
		#		-Entrada Diametro
        self.edit_D = QtGui.QLineEdit(self.group_Sec)
        self.edit_D.setObjectName(_fromUtf8("edit_D"))
        self.gridLayout_2.addWidget(self.edit_D, 1, 0, 1, 1)
		#		-Entrada Longitud
        self.edit_L = QtGui.QLineEdit(self.group_Sec)
        self.edit_L.setObjectName(_fromUtf8("edit_L"))
        self.gridLayout_2.addWidget(self.edit_L, 1, 3, 1, 1)
		#		-Boton Añadir
        self.button_AddSec = QtGui.QPushButton(self.group_Sec)
        self.button_AddSec.setObjectName(_fromUtf8("button_AddSec"))
        self.gridLayout_2.addWidget(self.button_AddSec, 3, 0, 1, 2)
		#		-Lista Secciones
        self.list_Secciones = QtGui.QListWidget(self.group_Sec)
        self.list_Secciones.setObjectName(_fromUtf8("list_Secciones"))
        self.gridLayout_2.addWidget(self.list_Secciones, 2, 0, 1, 4)
		#		-Boton Suprimir
        self.button_SupSec = QtGui.QPushButton(self.group_Sec)
        self.button_SupSec.setObjectName(_fromUtf8("button_SupSec"))
        self.gridLayout_2.addWidget(self.button_SupSec, 3, 2, 1, 2)

        self.gridLayout.addWidget(self.group_Sec, 1, 0, 1, 1)

		#	-Grupo Concentrador de Esfuerzos
        self.group_CEsf = QtGui.QGroupBox(self.configTab)
        self.group_CEsf.setMinimumSize(QtCore.QSize(211, 60))
        self.group_CEsf.setMaximumSize(QtCore.QSize(211, 60))
        self.group_CEsf.setObjectName(_fromUtf8("group_CEsf"))
        self.gridLayout_13 = QtGui.QGridLayout(self.group_CEsf)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        #		-Etiqueta Hombros
        self.label_Hombros = QtGui.QLabel(self.group_CEsf)
        self.label_Hombros.setObjectName(_fromUtf8("label_Hombros"))
        self.gridLayout_13.addWidget(self.label_Hombros, 0, 3, 1, 1)
        #		-Entrada Radio de Acuerdo
        self.dspinbox_rda = QtGui.QDoubleSpinBox(self.group_CEsf)
        self.dspinbox_rda.setDecimals(2)
        self.dspinbox_rda.setMinimum(0.0)
        self.dspinbox_rda.setMaximum(100.0)
        self.dspinbox_rda.setSingleStep(0.05)
        self.dspinbox_rda.setProperty("value", 0.0)
        self.dspinbox_rda.setObjectName(_fromUtf8("dspinbox_rda"))
        self.gridLayout_13.addWidget(self.dspinbox_rda, 0, 4, 1, 1)

        self.gridLayout.addWidget(self.group_CEsf, 2, 0, 1, 1)

        self.tabWidget.addTab(self.configTab, _fromUtf8(""))


		#-Tab Cargas
        self.cargasTab = QtGui.QWidget()
        self.cargasTab.setObjectName(_fromUtf8("cargasTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.cargasTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

		#	-Grupo Cargas
        self.group_Cargas = QtGui.QGroupBox(self.cargasTab)
        self.group_Cargas.setMinimumSize(QtCore.QSize(231, 0))
        self.group_Cargas.setMaximumSize(QtCore.QSize(231, 16777215))
        self.group_Cargas.setObjectName(_fromUtf8("group_Cargas"))
        self.gridLayout_5 = QtGui.QGridLayout(self.group_Cargas)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
		#		-Etiqueta Tipo
        self.label_Tipo = QtGui.QLabel(self.group_Cargas)
        self.label_Tipo.setObjectName(_fromUtf8("label_Tipo"))
        self.gridLayout_5.addWidget(self.label_Tipo, 0, 0, 1, 1)
		#		-Etiqueta Angulo    
        self.label_Angulo = QtGui.QLabel(self.group_Cargas)
        self.label_Angulo.setObjectName(_fromUtf8("label_Angulo"))
        self.gridLayout_5.addWidget(self.label_Angulo, 0, 3, 1, 1)
		#		-Combo Tipo de Carga
        self.combo_TipoCarga = QtGui.QComboBox(self.group_Cargas)
        self.combo_TipoCarga.setObjectName(_fromUtf8("combo_TipoCarga"))
        self.gridLayout_5.addWidget(self.combo_TipoCarga, 1, 0, 1, 3)
		#		-Entrada Angulo
        self.dspinbox_Angulo = QtGui.QDoubleSpinBox(self.group_Cargas)
        self.dspinbox_Angulo.setDecimals(2)
        self.dspinbox_Angulo.setMinimum(-90.0)
        self.dspinbox_Angulo.setMaximum(90.0)
        self.dspinbox_Angulo.setSingleStep(0.05)
        self.dspinbox_Angulo.setProperty("value", 0.0)
        self.dspinbox_Angulo.setObjectName(_fromUtf8("dspinbox_Angulo"))
        self.gridLayout_5.addWidget(self.dspinbox_Angulo, 1, 3, 1, 1)
        #		-Etiqueta Magnitud Inicial
        self.label_Mi = QtGui.QLabel(self.group_Cargas)
        self.label_Mi.setObjectName(_fromUtf8("label_Mi"))
        self.gridLayout_5.addWidget(self.label_Mi, 2, 0, 1, 1)
		#		-Etiqueta Magnitud
        self.label_M = QtGui.QLabel(self.group_Cargas)
        self.label_M.setObjectName(_fromUtf8("label_M"))
        self.gridLayout_5.addWidget(self.label_M, 2, 1, 1, 1)
		#		-Etiqueta Posicion Inicial
        self.label_PosXi = QtGui.QLabel(self.group_Cargas)
        self.label_PosXi.setObjectName(_fromUtf8("label_PosXi"))
        self.gridLayout_5.addWidget(self.label_PosXi, 2, 2, 1, 1)
		#		-Etiqueta Posicion Final
        self.label_PosXf = QtGui.QLabel(self.group_Cargas)
        self.label_PosXf.setObjectName(_fromUtf8("label_PosXf"))
        self.gridLayout_5.addWidget(self.label_PosXf, 2, 3, 1, 1)
        #		-Entrada Magnitud Inicial
        self.edit_Mi = QtGui.QLineEdit(self.group_Cargas)
        self.edit_Mi.setEnabled(False)
        self.edit_Mi.setObjectName(_fromUtf8("edit_Mi"))
        self.gridLayout_5.addWidget(self.edit_Mi, 3, 0, 1, 1)
		#		-Entrada Magnitud
        self.edit_M = QtGui.QLineEdit(self.group_Cargas)
        self.edit_M.setEnabled(True)
        self.edit_M.setObjectName(_fromUtf8("edit_M"))
        self.gridLayout_5.addWidget(self.edit_M, 3, 1, 1, 1)
		#		-Entrada Posicion Inicial
        self.edit_PosXi = QtGui.QLineEdit(self.group_Cargas)
        self.edit_PosXi.setEnabled(True)
        self.edit_PosXi.setObjectName(_fromUtf8("edit_PosXi"))
        self.gridLayout_5.addWidget(self.edit_PosXi, 3, 2, 1, 1)
		#		-Entrada Posicion Final
        self.edit_PosXf = QtGui.QLineEdit(self.group_Cargas)
        self.edit_PosXf.setEnabled(False)
        self.edit_PosXf.setObjectName(_fromUtf8("edit_PosXf"))
        self.gridLayout_5.addWidget(self.edit_PosXf, 3, 3, 1, 1)
		#		-Lista Cargas
        self.list_Cargas = QtGui.QListWidget(self.group_Cargas)
        self.list_Cargas.setObjectName(_fromUtf8("list_Cargas"))
        self.gridLayout_5.addWidget(self.list_Cargas, 4, 0, 1, 4)
		#		-Boton Anadir
        self.button_AddCarga = QtGui.QPushButton(self.group_Cargas)
        self.button_AddCarga.setObjectName(_fromUtf8("button_AddCarga"))
        self.gridLayout_5.addWidget(self.button_AddCarga, 5, 0, 1, 2)
		#		-Boton Suprimir
        self.button_SupCarga = QtGui.QPushButton(self.group_Cargas)
        self.button_SupCarga.setObjectName(_fromUtf8("button_SupCarga"))
        self.gridLayout_5.addWidget(self.button_SupCarga, 5, 2, 1, 2)

        self.gridLayout_3.addWidget(self.group_Cargas, 0, 0, 1, 1)

		#	-Grupo Diagramas
        self.group_Diag = QtGui.QGroupBox(self.cargasTab)
        self.group_Diag.setObjectName(_fromUtf8("group_Diag"))
        self.gridLayout_4 = QtGui.QGridLayout(self.group_Diag)
        self.gridLayout_4.setContentsMargins(1, 0, 1, 3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
		#		-Plot Diagramas
        self.graphics_Diag = Mpl(self.group_Diag)
        self.graphics_Diag.setObjectName(_fromUtf8("graphics_Diag"))
        self.gridLayout_4.addWidget(self.graphics_Diag, 0, 0, 1, 6)
		#		-Boton Calcular
        self.button_CalcDiag = QtGui.QPushButton(self.group_Diag)
        self.button_CalcDiag.setObjectName(_fromUtf8("button_CalcDiag"))
        self.gridLayout_4.addWidget(self.button_CalcDiag, 1, 5, 1, 1)
		#		-Radio PlanoXZ
        self.radio_XZ = QtGui.QRadioButton(self.group_Diag)
        self.radio_XZ.setObjectName(_fromUtf8("radio_XZ"))
        self.gridLayout_4.addWidget(self.radio_XZ, 1, 1, 1, 1)
		#		-Radio PlanoXY
        self.radio_XY = QtGui.QRadioButton(self.group_Diag)
        self.radio_XY.setChecked(True)
        self.radio_XY.setObjectName(_fromUtf8("radio_XY"))
        self.gridLayout_4.addWidget(self.radio_XY, 1, 0, 1, 1)
		#		-Radio Torsion/Total
        self.radio_TT = QtGui.QRadioButton(self.group_Diag)
        self.radio_TT.setObjectName(_fromUtf8("radio_TT"))
        self.gridLayout_4.addWidget(self.radio_TT, 1, 2, 1, 1)

        self.gridLayout_3.addWidget(self.group_Diag, 0, 1, 2, 1)

		#	-Grupo Reacciones
        self.group_R = QtGui.QGroupBox(self.cargasTab)
        self.group_R.setMinimumSize(QtCore.QSize(231, 101))
        self.group_R.setMaximumSize(QtCore.QSize(231, 101))
        self.group_R.setObjectName(_fromUtf8("group_R"))
        self.gridLayout_6 = QtGui.QGridLayout(self.group_R)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
		#		-Etiqueta RXY1
        self.label_RXY1 = QtGui.QLabel(self.group_R)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_RXY1.setFont(font)
        self.label_RXY1.setObjectName(_fromUtf8("label_RXY1"))
        self.gridLayout_6.addWidget(self.label_RXY1, 0, 0, 1, 2)
		#		-Etiqueta RXY2
        self.label_RXY2 = QtGui.QLabel(self.group_R)
        self.label_RXY2.setFont(font)
        self.label_RXY2.setObjectName(_fromUtf8("label_RXY2"))
        self.gridLayout_6.addWidget(self.label_RXY2, 0, 2, 1, 2)
		#		-Etiqueta RXZ1
        self.label_RXZ1 = QtGui.QLabel(self.group_R)
        self.label_RXZ1.setFont(font)
        self.label_RXZ1.setObjectName(_fromUtf8("label_RXZ1"))
        self.gridLayout_6.addWidget(self.label_RXZ1, 1, 0, 1, 2)
		#		-Etiqueta RXZ2
        self.label_RXZ2 = QtGui.QLabel(self.group_R)
        self.label_RXZ2.setFont(font)
        self.label_RXZ2.setObjectName(_fromUtf8("label_RXZ2"))
        self.gridLayout_6.addWidget(self.label_RXZ2, 1, 2, 1, 2)

        self.gridLayout_3.addWidget(self.group_R, 1, 0, 1, 1)

        self.tabWidget.addTab(self.cargasTab, _fromUtf8(""))

		#-Tab Disenio Estatico
        self.dEstaticoTab = QtGui.QWidget()
        self.dEstaticoTab.setObjectName(_fromUtf8("dEstaticoTab"))
        self.gridLayout_11 = QtGui.QGridLayout(self.dEstaticoTab)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
   		#	-Grupo Circulo de Mohr
        self.group_CMohr = QtGui.QGroupBox(self.dEstaticoTab)
        self.group_CMohr.setMaximumSize(QtCore.QSize(700, 16777215))
        self.group_CMohr.setObjectName(_fromUtf8("group_CMohr"))
        self.gridLayout_9 = QtGui.QGridLayout(self.group_CMohr)
        self.gridLayout_9.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
   		#		-Plot Circulo de Mohr
        self.graphics_CMohr = Mpl(self.group_CMohr)
        self.graphics_CMohr.setMinimumSize(QtCore.QSize(240, 135))
        self.graphics_CMohr.setObjectName(_fromUtf8("graphics_CMohr"))
        self.gridLayout_9.addWidget(self.graphics_CMohr, 0, 0, 6, 1)
   		#		-Etiqueta Sigma1
        self.label_Sigma1 = QtGui.QLabel(self.group_CMohr)
        self.label_Sigma1.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_Sigma1.setFont(font)
        self.label_Sigma1.setObjectName(_fromUtf8("label_Sigma1"))
        self.gridLayout_9.addWidget(self.label_Sigma1, 0, 1, 1, 1)
   		#		-Etiqueta Sigma2
        self.label_Sigma2 = QtGui.QLabel(self.group_CMohr)
        self.label_Sigma2.setFont(font)
        self.label_Sigma2.setObjectName(_fromUtf8("label_Sigma2"))
        self.gridLayout_9.addWidget(self.label_Sigma2, 1, 1, 1, 1)
   		#		-Etiqueta Tau12
        self.label_Tau12 = QtGui.QLabel(self.group_CMohr)
        self.label_Tau12.setFont(font)
        self.label_Tau12.setObjectName(_fromUtf8("label_Tau12"))
        self.gridLayout_9.addWidget(self.label_Tau12, 2,1, 1, 1)
   		#		-Etiqueta SigmaTau
        self.label_SigmaTau = QtGui.QLabel(self.group_CMohr)
        self.label_SigmaTau.setFont(font)
        self.label_SigmaTau.setObjectName(_fromUtf8("label_SigmaTau"))
        self.gridLayout_9.addWidget(self.label_SigmaTau, 3, 1, 1, 1)
   		#		-Etiqueta Phi
        self.label_phi = QtGui.QLabel(self.group_CMohr)
        self.label_phi.setFont(font)
        self.label_phi.setObjectName(_fromUtf8("label_phi"))
        self.gridLayout_9.addWidget(self.label_phi, 4, 1, 1, 1)

        self.gridLayout_11.addWidget(self.group_CMohr, 0, 2, 2, 1)
        
   		#	-Grupo Seccion Critica
        self.group_SecCrit = QtGui.QGroupBox(self.dEstaticoTab)
        self.group_SecCrit.setObjectName(_fromUtf8("group_SecCrit"))
        self.gridLayout_15 = QtGui.QGridLayout(self.group_SecCrit)
        self.gridLayout_15.setContentsMargins(1, 1, 1, 5)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
   		#		-Plot Seccion Critica
        self.graphics_SCrit = Mpl(self.group_SecCrit)
        self.graphics_SCrit.setMinimumSize(QtCore.QSize(160, 90))
        self.graphics_SCrit.setObjectName(_fromUtf8("graphics_SCrit"))
        self.gridLayout_15.addWidget(self.graphics_SCrit, 0, 0, 4, 1)
   		#		-Etiqueta TauXZ
        self.label_Tauxz = QtGui.QLabel(self.group_SecCrit)
        self.label_Tauxz.setMinimumSize(QtCore.QSize(80, 0))
        font.setPointSize(8)
        self.label_Tauxz.setFont(font)
        self.label_Tauxz.setObjectName(_fromUtf8("label_Tauxz"))
        self.gridLayout_15.addWidget(self.label_Tauxz, 1, 1, 1, 2)
   		#		-Etiqueta SigmaX
        self.label_Sigmax = QtGui.QLabel(self.group_SecCrit)
        self.label_Sigmax.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Sigmax.setFont(font)
        self.label_Sigmax.setObjectName(_fromUtf8("label_Sigmax"))
        self.gridLayout_15.addWidget(self.label_Sigmax, 0, 1, 1, 2)
   		#		-Etiqueta Posicion de x Critica 
        self.label_xcrit = QtGui.QLabel(self.group_SecCrit)
        self.label_xcrit.setFont(font)
        self.label_xcrit.setObjectName(_fromUtf8("label_xcrit"))
        self.gridLayout_15.addWidget(self.label_xcrit, 2, 1, 1, 1)
   		#		-Boton Informacion de Kt Kts
        self.button_KtKts = QtGui.QPushButton(self.group_SecCrit)
        self.button_KtKts.setMaximumSize(QtCore.QSize(55, 16777215))
        self.button_KtKts.setObjectName(_fromUtf8("button_KtKts"))
        self.gridLayout_15.addWidget(self.button_KtKts, 3, 1, 1, 1)
        #		-CheckBox Ductil
        self.checkBox = QtGui.QCheckBox(self.group_SecCrit)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox.setChecked(False)
        self.gridLayout_15.addWidget(self.checkBox, 3, 2, 1, 1)

        self.gridLayout_11.addWidget(self.group_SecCrit, 0, 0, 1, 2)
        
   		#	-Grupo Teorias de Falla
        self.group_TFalla = QtGui.QGroupBox(self.dEstaticoTab)
        self.group_TFalla.setObjectName(_fromUtf8("group_TFalla"))
        self.gridLayout_8 = QtGui.QGridLayout(self.group_TFalla)
        self.gridLayout_8.setContentsMargins(2, 5, 2, 0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
   		#		-Etiqueta Material Ductil
        self.label_MDuctil = QtGui.QLabel(self.group_TFalla)
        self.label_MDuctil.setObjectName(_fromUtf8("label_MDuctil"))
        self.gridLayout_8.addWidget(self.label_MDuctil, 0, 1, 1, 2)
   		#		-Etiqueta Material Fragil
        self.label_MFragil = QtGui.QLabel(self.group_TFalla)
        self.label_MFragil.setObjectName(_fromUtf8("label_MFragil"))
        self.gridLayout_8.addWidget(self.label_MFragil, 2, 1, 1, 2)
   		#		-Radio Coulomb Mohr Fragil
        self.radio_CMF = QtGui.QRadioButton(self.group_TFalla)
        self.radio_CMF.setEnabled(False)
        self.radio_CMF.setObjectName(_fromUtf8("radio_CMF"))
        self.gridLayout_8.addWidget(self.radio_CMF, 2, 4, 1, 1)
   		#		-Radio Mohr Modificado
        self.radio_MM = QtGui.QRadioButton(self.group_TFalla)
        self.radio_MM.setEnabled(False)
        self.radio_MM.setObjectName(_fromUtf8("radio_MM"))
        self.gridLayout_8.addWidget(self.radio_MM, 2, 5, 1, 1)
   		#		-Plot Teoria de Falla
        self.graphics_TFalla = Mpl(self.group_TFalla)
        self.graphics_TFalla.setMinimumSize(QtCore.QSize(265, 125))
        self.graphics_TFalla.setObjectName(_fromUtf8("graphics_TFalla"))
        self.gridLayout_8.addWidget(self.graphics_TFalla, 3, 1, 1, 6)
   		#		-Radio Esfuerzo Normal Maximo
        self.radio_ENM = QtGui.QRadioButton(self.group_TFalla)
        self.radio_ENM.setEnabled(False)
        self.radio_ENM.setObjectName(_fromUtf8("radio_ENM"))
        self.gridLayout_8.addWidget(self.radio_ENM, 2, 3, 1, 1)
   		#		-Radio Energia de Distorsion
        self.radio_ED = QtGui.QRadioButton(self.group_TFalla)
        self.radio_ED.setChecked(True)
        self.radio_ED.setObjectName(_fromUtf8("radio_ED"))
        self.gridLayout_8.addWidget(self.radio_ED, 0, 4, 1, 1)
   		#		-Radio Coulomb Mohr Ductil
        self.radio_CMD = QtGui.QRadioButton(self.group_TFalla)
        self.radio_CMD.setObjectName(_fromUtf8("radio_CMD"))
        self.gridLayout_8.addWidget(self.radio_CMD, 0, 5, 1, 1)
   		#		-Radio Esfuerzo Cortante Maximo
        self.radio_ECM = QtGui.QRadioButton(self.group_TFalla)
        self.radio_ECM.setObjectName(_fromUtf8("radio_ECM"))
        self.gridLayout_8.addWidget(self.radio_ECM, 0, 3, 1, 1)
        
        self.gridLayout_11.addWidget(self.group_TFalla, 1, 0, 2, 2)
        
   		#	-Grupo Diametros
        self.group_Diametros = QtGui.QGroupBox(self.dEstaticoTab)
        self.group_Diametros.setMaximumSize(QtCore.QSize(700, 115))
        self.group_Diametros.setObjectName(_fromUtf8("group_Diametros"))
        self.gridLayout_10 = QtGui.QGridLayout(self.group_Diametros)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
   		#		-Etiqueta Secciones
        self.label_Secciones = QtGui.QLabel(self.group_Diametros)
        self.label_Secciones.setObjectName(_fromUtf8("label_Secciones"))
        self.gridLayout_10.addWidget(self.label_Secciones, 1, 3, 1, 1)
   		#		-Entrada Factor de Disenio n
        self.edit_n = QtGui.QLineEdit(self.group_Diametros)
        self.edit_n.setObjectName(_fromUtf8("edit_n"))
        self.gridLayout_10.addWidget(self.edit_n, 1, 1, 1, 1)
   		#		-Etiqueta Factor de Disenio
        self.label_FacDis = QtGui.QLabel(self.group_Diametros)
        self.label_FacDis.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_FacDis.setObjectName(_fromUtf8("label_FacDis"))
        self.gridLayout_10.addWidget(self.label_FacDis, 0, 0, 1, 2)
        #		-Linea vertical
        self.line = QtGui.QFrame(self.group_Diametros)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_10.addWidget(self.line, 0, 2, 3, 1)
   		#		-Lista Secciones Disenio Estatico
        self.list_Secciones_DE = QtGui.QListWidget(self.group_Diametros)
        self.list_Secciones_DE.setFont(font)
        self.list_Secciones_DE.setObjectName(_fromUtf8("list_Secciones_DE"))
        self.gridLayout_10.addWidget(self.list_Secciones_DE, 1, 4, 2, 2)
   		#		-Etiqueta n
        self.label_n = QtGui.QLabel(self.group_Diametros)
        self.label_n.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_n.setObjectName(_fromUtf8("label_n"))
        self.gridLayout_10.addWidget(self.label_n, 1, 0, 1, 1)
   		#		-Etiqueta Seccion Critica
        self.label_SecCrit = QtGui.QLabel(self.group_Diametros)
        self.label_SecCrit.setObjectName(_fromUtf8("label_SecCrit"))
        self.gridLayout_10.addWidget(self.label_SecCrit, 0, 3, 1, 1)
   		#		-Entrada Diametro de Seccion Critica
        self.edit_dEstatico = QtGui.QLineEdit(self.group_Diametros)
        self.edit_dEstatico.setEnabled(False)
        self.edit_dEstatico.setFont(font)
        self.edit_dEstatico.setObjectName(_fromUtf8("edit_dEstatico"))
        self.gridLayout_10.addWidget(self.edit_dEstatico, 0, 4, 1, 1)
   		#		-Boton Calcular Diametro
        self.button_CalcDiam = QtGui.QPushButton(self.group_Diametros)
        self.button_CalcDiam.setObjectName(_fromUtf8("button_CalcDiam"))
        self.gridLayout_10.addWidget(self.button_CalcDiam, 2, 0, 1, 2)
   		#		-Boton Recalcular con las Nuevas Dimensiones
        self.button_ReCalc = QtGui.QPushButton(self.group_Diametros)
        self.button_ReCalc.setObjectName(_fromUtf8("button_ReCalc"))
        self.gridLayout_10.addWidget(self.button_ReCalc, 0, 5, 1, 1)
        
        self.gridLayout_11.addWidget(self.group_Diametros, 2, 2, 1, 1)
        
        self.tabWidget.addTab(self.dEstaticoTab, _fromUtf8(""))
        

		#-Tab Disenio Dinamico
        self.dDinamicoTab = QtGui.QWidget()
        self.dDinamicoTab.setObjectName(_fromUtf8("dDinamicoTab"))
        self.gridLayout_14 = QtGui.QGridLayout(self.dDinamicoTab)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))

   		#	-Grupo Esfuerzos Fluctuantes
        self.group_Fluctuantes = QtGui.QGroupBox(self.dDinamicoTab)
        self.group_Fluctuantes.setObjectName(_fromUtf8("group_Fluctuantes"))
        self.gridLayout_17 = QtGui.QGridLayout(self.group_Fluctuantes)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
   		#		-Plot Esfuerzos Fluctuantes
        self.graphics_Fluct = Mpl(self.group_Fluctuantes)
        self.graphics_Fluct.setMinimumSize(QtCore.QSize(165, 140))
        self.graphics_Fluct.setObjectName(_fromUtf8("graphics_Fluct"))
        self.gridLayout_17.addWidget(self.graphics_Fluct, 0, 0, 5, 1)
   		#		-Etiqueta Sigma Amplitud
        self.label_Sigma_a = QtGui.QLabel(self.group_Fluctuantes)
        self.label_Sigma_a.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Sigma_a.setFont(font)
        self.label_Sigma_a.setObjectName(_fromUtf8("label_Sigma_a"))
        self.gridLayout_17.addWidget(self.label_Sigma_a, 0, 1, 1, 1)
   		#		-Etiqueta Sigma Medio
        self.label_Sigma_m = QtGui.QLabel(self.group_Fluctuantes)
        self.label_Sigma_m.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Sigma_m.setFont(font)
        self.label_Sigma_m.setObjectName(_fromUtf8("label_Sigma_m"))
        self.gridLayout_17.addWidget(self.label_Sigma_m, 1, 1, 1, 1)
   		#		-Etiqueta Tau Amplitud
        self.label_Tau_a = QtGui.QLabel(self.group_Fluctuantes)
        self.label_Tau_a.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Tau_a.setFont(font)
        self.label_Tau_a.setObjectName(_fromUtf8("label_Tau_a"))
        self.gridLayout_17.addWidget(self.label_Tau_a, 2, 1, 1, 1)
   		#		-Etiqueta Tau Medio
        self.label_Tau_m = QtGui.QLabel(self.group_Fluctuantes)
        self.label_Tau_m.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Tau_m.setFont(font)
        self.label_Tau_m.setObjectName(_fromUtf8("label_Tau_m"))
        self.gridLayout_17.addWidget(self.label_Tau_m, 3, 1, 1, 1)
   		#		-Boton Kf y  Kfs
        self.button_KfKfs = QtGui.QPushButton(self.group_Fluctuantes)
        self.button_KfKfs.setMaximumSize(QtCore.QSize(55, 16777215))
        self.button_KfKfs.setObjectName(_fromUtf8("button_KfKfs"))
        self.gridLayout_17.addWidget(self.button_KfKfs, 4, 1, 1, 1)

        self.gridLayout_14.addWidget(self.group_Fluctuantes, 0, 0, 1, 1)

   		#	-Grupo Criterios de Falla a la Fatiga
        self.group_CFalla = QtGui.QGroupBox(self.dDinamicoTab)
        self.group_CFalla.setEnabled(False)
        self.group_CFalla.setMaximumSize(QtCore.QSize(800, 16777215))
        self.group_CFalla.setObjectName(_fromUtf8("group_CFalla"))
        self.gridLayout_18 = QtGui.QGridLayout(self.group_CFalla)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
   		#		-Radio ED-Goodman
        self.radio_Goodman = QtGui.QRadioButton(self.group_CFalla)
        self.radio_Goodman.setChecked(True)
        self.radio_Goodman.setObjectName(_fromUtf8("radio_Goodman"))
        self.gridLayout_18.addWidget(self.radio_Goodman, 0, 0, 1, 1)
   		#		-Radio ED-Gerber
        self.radio_Gerber = QtGui.QRadioButton(self.group_CFalla)
        self.radio_Gerber.setObjectName(_fromUtf8("radio_Gerber"))
        self.gridLayout_18.addWidget(self.radio_Gerber, 0, 1, 1, 1)
   		#		-Radio ED-Soderberg
        self.radio_Soderberg = QtGui.QRadioButton(self.group_CFalla)
        self.radio_Soderberg.setObjectName(_fromUtf8("radio_Soderberg"))
        self.gridLayout_18.addWidget(self.radio_Soderberg, 0, 2, 1, 1)
   		#		-Radio ED-ASME eliptica
        self.radio_ASME = QtGui.QRadioButton(self.group_CFalla)
        self.radio_ASME.setObjectName(_fromUtf8("radio_ASME"))
        self.gridLayout_18.addWidget(self.radio_ASME, 0, 3, 1, 1)
   		#		-Plot Criterios de Falla a la Fatiga
        self.graphics_CFalla = Mpl(self.group_CFalla)
        self.graphics_CFalla.setMinimumSize(QtCore.QSize(250, 220))
        self.graphics_CFalla.setObjectName(_fromUtf8("graphics_CFalla"))
        self.gridLayout_18.addWidget(self.graphics_CFalla, 1, 0, 2, 3)
   		#		-Etiqueta Sigma Amplitud Prima
        self.label_Sigma_ap = QtGui.QLabel(self.group_CFalla)
        self.label_Sigma_ap.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Sigma_ap.setFont(font)
        self.label_Sigma_ap.setObjectName(_fromUtf8("label_Sigma_ap"))
        self.gridLayout_18.addWidget(self.label_Sigma_ap, 1, 3, 1, 1)
   		#		-Etiqueta Sigma Medio Prima
        self.label_Sigma_mp = QtGui.QLabel(self.group_CFalla)
        self.label_Sigma_mp.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Sigma_mp.setFont(font)
        self.label_Sigma_mp.setObjectName(_fromUtf8("label_Sigma_mp"))
        self.gridLayout_18.addWidget(self.label_Sigma_mp, 2, 3, 1, 1)

        self.gridLayout_14.addWidget(self.group_CFalla, 0, 1, 2, 1)

   		#	-Grupo Diametros Disenio Dinamico
        self.group_DiametrosD = QtGui.QGroupBox(self.dDinamicoTab)
        self.group_DiametrosD.setMaximumSize(QtCore.QSize(800, 115))
        self.group_DiametrosD.setObjectName(_fromUtf8("group_DiametrosD"))
        self.gridLayout_19 = QtGui.QGridLayout(self.group_DiametrosD)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
   		#		-Etiqueta Factor de Disenio Dinamico
        self.label_FacDisD = QtGui.QLabel(self.group_DiametrosD)
        self.label_FacDisD.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_FacDisD.setObjectName(_fromUtf8("label_FacDisD"))
        self.gridLayout_19.addWidget(self.label_FacDisD, 0, 0, 1, 2)
        #		-Linea vertical
        self.line_2 = QtGui.QFrame(self.group_DiametrosD)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_19.addWidget(self.line_2, 0, 2, 3, 1)
   		#		-Etiqueta Diametro Seccion Critica Dinamico
        self.label_SecCritD = QtGui.QLabel(self.group_DiametrosD)
        self.label_SecCritD.setObjectName(_fromUtf8("label_SecCritD"))
        self.gridLayout_19.addWidget(self.label_SecCritD, 0, 3, 1, 1)
   		#		-Entrada Diametro Dinamico
        self.edit_dDinamico = QtGui.QLineEdit(self.group_DiametrosD)
        self.edit_dDinamico.setEnabled(False)
        self.edit_dDinamico.setFont(font)
        self.edit_dDinamico.setObjectName(_fromUtf8("edit_dDinamico"))
        self.gridLayout_19.addWidget(self.edit_dDinamico, 0, 4, 1, 1)
   		#		-Boton Recalcular Disenio Dinamico
        self.button_ReCalcD = QtGui.QPushButton(self.group_DiametrosD)
        self.button_ReCalcD.setObjectName(_fromUtf8("button_ReCalcD"))
        self.gridLayout_19.addWidget(self.button_ReCalcD, 0, 5, 1, 1)
   		#		-Etiqueta nd
        self.label_nD = QtGui.QLabel(self.group_DiametrosD)
        self.label_nD.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_nD.setObjectName(_fromUtf8("label_nD"))
        self.gridLayout_19.addWidget(self.label_nD, 1, 0, 1, 1)
   		#		-Entrada nd
        self.edit_nD = QtGui.QLineEdit(self.group_DiametrosD)
        self.edit_nD.setObjectName(_fromUtf8("edit_nD"))
        self.gridLayout_19.addWidget(self.edit_nD, 1, 1, 1, 1)
   		#		-Boton Calcular Diametro Dinamico
        self.button_CalcDiamD = QtGui.QPushButton(self.group_DiametrosD)
        self.button_CalcDiamD.setObjectName(_fromUtf8("button_CalcDiamD"))
        self.gridLayout_19.addWidget(self.button_CalcDiamD, 2, 0, 1, 2)
   		#		-Etiqueta Secciones Disenio Dinamico
        self.label_SeccionesD = QtGui.QLabel(self.group_DiametrosD)
        self.label_SeccionesD.setObjectName(_fromUtf8("label_SeccionesD"))
        self.gridLayout_19.addWidget(self.label_SeccionesD, 1, 3, 1, 1)
   		#		-Lista Secciones Disenio Dinamico
        self.list_Secciones_DD = QtGui.QListWidget(self.group_DiametrosD)
        self.list_Secciones_DD.setFont(font)
        self.list_Secciones_DD.setObjectName(_fromUtf8("list_Secciones_DD"))
        self.gridLayout_19.addWidget(self.list_Secciones_DD, 1, 4, 2, 2)


        self.gridLayout_14.addWidget(self.group_DiametrosD, 2, 1, 1, 1)

   		#	-Grupo Resisencia a la Fatiga
        self.group_RFatiga = QtGui.QGroupBox(self.dDinamicoTab)
        self.group_RFatiga.setObjectName(_fromUtf8("group_RFatiga"))
        self.gridLayout_16 = QtGui.QGridLayout(self.group_RFatiga)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
   		#		-Etiqueta Se Prima
        self.label_Sep = QtGui.QLabel(self.group_RFatiga)
        self.label_Sep.setFont(font)
        self.label_Sep.setObjectName(_fromUtf8("label_Sep"))
        self.gridLayout_16.addWidget(self.label_Sep, 0, 0, 1, 2)
   		#		-Etiqueta Sut
        self.label_Sut = QtGui.QLabel(self.group_RFatiga)
        self.label_Sut.setFont(font)
        self.label_Sut.setObjectName(_fromUtf8("label_Sut"))
        self.gridLayout_16.addWidget(self.label_Sut, 1, 0, 1, 2)
   		#		-Etiqueta Coeficientes de Marin
        self.label_Coef = QtGui.QLabel(self.group_RFatiga)
        self.label_Coef.setObjectName(_fromUtf8("label_Coef"))
        self.gridLayout_16.addWidget(self.label_Coef, 3, 0, 1, 3)
   		#		-Plot Resistencia a la Fatiga
        self.graphics_RFatiga = Mpl(self.group_RFatiga)
        self.graphics_RFatiga.setMinimumSize(QtCore.QSize(120, 100))
        self.graphics_RFatiga.setObjectName(_fromUtf8("graphics_RFatiga"))
        self.gridLayout_16.addWidget(self.graphics_RFatiga, 0, 2, 2, 5)
   		#		-Boton ka
        self.button_ka = QtGui.QPushButton(self.group_RFatiga)
        self.button_ka.setMinimumSize(QtCore.QSize(30, 0))
        self.button_ka.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_ka.setObjectName(_fromUtf8("button_ka"))
        self.gridLayout_16.addWidget(self.button_ka, 4, 0, 1, 1)
   		#		-Boton kb
        self.button_kb = QtGui.QPushButton(self.group_RFatiga)
        self.button_kb.setMinimumSize(QtCore.QSize(30, 0))
        self.button_kb.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_kb.setObjectName(_fromUtf8("button_kb"))
        self.gridLayout_16.addWidget(self.button_kb, 4, 1, 1, 1)
   		#		-Boton kc
        self.button_kc = QtGui.QPushButton(self.group_RFatiga)
        self.button_kc.setMinimumSize(QtCore.QSize(30, 0))
        self.button_kc.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_kc.setObjectName(_fromUtf8("button_kc"))
        self.gridLayout_16.addWidget(self.button_kc, 4, 2, 1, 1)
   		#		-Boton kd
        self.button_kd = QtGui.QPushButton(self.group_RFatiga)
        self.button_kd.setMinimumSize(QtCore.QSize(30, 0))
        self.button_kd.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_kd.setObjectName(_fromUtf8("button_kd"))
        self.gridLayout_16.addWidget(self.button_kd, 4, 3, 1, 1)
   		#		-Boton ke
        self.button_ke = QtGui.QPushButton(self.group_RFatiga)
        self.button_ke.setMinimumSize(QtCore.QSize(30, 0))
        self.button_ke.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_ke.setObjectName(_fromUtf8("button_ke"))
        self.gridLayout_16.addWidget(self.button_ke, 4, 4, 1, 1)
   		#		-Boton kf
        self.button_kf = QtGui.QPushButton(self.group_RFatiga)
        self.button_kf.setMinimumSize(QtCore.QSize(30, 0))
        self.button_kf.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_kf.setObjectName(_fromUtf8("button_kf"))
        self.gridLayout_16.addWidget(self.button_kf, 4, 5, 1, 1)
   		#		-Etiqueta ka
        self.label_ka = QtGui.QLabel(self.group_RFatiga)
        self.label_ka.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ka.setObjectName(_fromUtf8("label_ka"))
        self.gridLayout_16.addWidget(self.label_ka, 5, 0, 1, 1)
   		#		-Etiqueta kb
        self.label_kb = QtGui.QLabel(self.group_RFatiga)
        self.label_kb.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kb.setObjectName(_fromUtf8("label_kb"))
        self.gridLayout_16.addWidget(self.label_kb, 5, 1, 1, 1)
   		#		-Etiqueta kc
        self.label_kc = QtGui.QLabel(self.group_RFatiga)
        self.label_kc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kc.setObjectName(_fromUtf8("label_kc"))
        self.gridLayout_16.addWidget(self.label_kc, 5, 2, 1, 1)
   		#		-Etiqueta kd
        self.label_kd = QtGui.QLabel(self.group_RFatiga)
        self.label_kd.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kd.setObjectName(_fromUtf8("label_kd"))
        self.gridLayout_16.addWidget(self.label_kd, 5, 3, 1, 1)
   		#		-Etiqueta ke
        self.label_ke = QtGui.QLabel(self.group_RFatiga)
        self.label_ke.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ke.setObjectName(_fromUtf8("label_ke"))
        self.gridLayout_16.addWidget(self.label_ke, 5, 4, 1, 1)
   		#		-Etiqueta kf
        self.label_kf = QtGui.QLabel(self.group_RFatiga)
        self.label_kf.setAlignment(QtCore.Qt.AlignCenter)
        self.label_kf.setObjectName(_fromUtf8("label_kf"))
        self.gridLayout_16.addWidget(self.label_kf, 5, 5, 1, 1)
   		#		-Etiqueta Se
        self.label_Se = QtGui.QLabel(self.group_RFatiga)
        self.label_Se.setObjectName(_fromUtf8("label_Se"))
        self.gridLayout_16.addWidget(self.label_Se, 6, 0, 1, 4)
   		#		-Etiqueta Se2
        self.label_Se_2 = QtGui.QLabel(self.group_RFatiga)
        self.label_Se_2.setFont(font)
        self.label_Se_2.setObjectName(_fromUtf8("label_Se_2"))
        self.gridLayout_16.addWidget(self.label_Se_2, 6, 4, 1, 3)

        self.gridLayout_14.addWidget(self.group_RFatiga, 1, 0, 2, 1)

        self.tabWidget.addTab(self.dDinamicoTab, _fromUtf8(""))

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

		#-Barra de Menu
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
		#	-Menu Archivo
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
		#	-Menu Ayuda
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))

        MainWindow.setMenuBar(self.menubar)


		#-Barra de Estado
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
		#		-Salir
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
		#		-Acerca de
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))

        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setTabOrder(self.tabWidget, self.combo_Mat)
        MainWindow.setTabOrder(self.combo_Mat, self.button_Prop)
        MainWindow.setTabOrder(self.button_Prop, self.edit_D)
        MainWindow.setTabOrder(self.edit_D, self.edit_L)
        MainWindow.setTabOrder(self.edit_L, self.button_AddSec)
        MainWindow.setTabOrder(self.button_AddSec, self.dspinbox_rda)
        MainWindow.setTabOrder(self.dspinbox_rda, self.edit_XR1)
        MainWindow.setTabOrder(self.edit_XR1, self.edit_XR2)
        MainWindow.setTabOrder(self.edit_XR2, self.button_CrearEje)
        MainWindow.setTabOrder(self.button_CrearEje, self.list_Secciones)
        MainWindow.setTabOrder(self.list_Secciones, self.button_SupSec)
        MainWindow.setTabOrder(self.button_SupSec, self.combo_TipoCarga)
        MainWindow.setTabOrder(self.combo_TipoCarga, self.dspinbox_Angulo)
        MainWindow.setTabOrder(self.dspinbox_Angulo, self.edit_M)
        MainWindow.setTabOrder(self.edit_M, self.edit_PosXi)
        MainWindow.setTabOrder(self.edit_PosXi, self.edit_Mi)
        MainWindow.setTabOrder(self.edit_Mi, self.edit_PosXf)
        MainWindow.setTabOrder(self.edit_PosXf, self.button_AddCarga)
        MainWindow.setTabOrder(self.button_AddCarga, self.list_Cargas)
        MainWindow.setTabOrder(self.list_Cargas, self.button_SupCarga)
        MainWindow.setTabOrder(self.button_SupCarga, self.radio_XY)
        MainWindow.setTabOrder(self.radio_XY, self.radio_XZ)
        MainWindow.setTabOrder(self.radio_XZ, self.radio_TT)
        MainWindow.setTabOrder(self.radio_TT, self.button_CalcDiag)
        MainWindow.setTabOrder(self.button_CalcDiag, self.button_KtKts)
        MainWindow.setTabOrder(self.button_KtKts, self.radio_ECM)
        MainWindow.setTabOrder(self.radio_ECM, self.radio_ED)
        MainWindow.setTabOrder(self.radio_ED, self.radio_CMD)
        MainWindow.setTabOrder(self.radio_CMD, self.radio_ENM)
        MainWindow.setTabOrder(self.radio_ENM, self.radio_CMF)
        MainWindow.setTabOrder(self.radio_CMF, self.radio_MM)
        MainWindow.setTabOrder(self.radio_MM, self.edit_n)
        MainWindow.setTabOrder(self.edit_n, self.button_CalcDiam)
        MainWindow.setTabOrder(self.button_CalcDiam, self.edit_dEstatico)
        MainWindow.setTabOrder(self.edit_dEstatico, self.list_Secciones_DE)
        MainWindow.setTabOrder(self.list_Secciones_DE, self.button_ReCalc)
        MainWindow.setTabOrder(self.button_ReCalc, self.button_KfKfs)
        MainWindow.setTabOrder(self.button_KfKfs, self.button_ka)
        MainWindow.setTabOrder(self.button_ka, self.button_kb)
        MainWindow.setTabOrder(self.button_kb, self.button_kc)
        MainWindow.setTabOrder(self.button_kc, self.button_kd)
        MainWindow.setTabOrder(self.button_kd, self.button_ke)
        MainWindow.setTabOrder(self.button_ke, self.button_kf)
        MainWindow.setTabOrder(self.button_kf, self.radio_Goodman)
        MainWindow.setTabOrder(self.radio_Goodman, self.radio_Gerber)
        MainWindow.setTabOrder(self.radio_Gerber, self.radio_Soderberg)
        MainWindow.setTabOrder(self.radio_Soderberg, self.radio_ASME)
        MainWindow.setTabOrder(self.radio_ASME, self.edit_nD)
        MainWindow.setTabOrder(self.edit_nD, self.button_CalcDiamD)
        MainWindow.setTabOrder(self.button_CalcDiamD, self.edit_dDinamico)
        MainWindow.setTabOrder(self.edit_dDinamico, self.button_ReCalcD)
        MainWindow.setTabOrder(self.button_ReCalcD, self.list_Secciones_DD)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "EjesDim", None))
        self.group_PrevConfig.setTitle(_translate("MainWindow", "Configuración Preliminar", None))
        self.label_XR1.setText(_translate("MainWindow", "Soporte 1 [mm]", None))
        self.label_XR2.setText(_translate("MainWindow", "Soporte 2 [mm]", None))
        self.button_CrearEje.setText(_translate("MainWindow", "Crear", None))
        self.group_Material.setTitle(_translate("MainWindow", " Material", None))
        self.button_Prop.setText(_translate("MainWindow", "i", None))
        self.group_Sec.setTitle(_translate("MainWindow", "Secciones", None))
        self.label_D.setText(_translate("MainWindow", "Diámetro [mm]", None))
        self.button_AddSec.setText(_translate("MainWindow", "Añadir", None))
        self.button_SupSec.setText(_translate("MainWindow", "Suprimir", None))
        self.label_L.setText(_translate("MainWindow", "Longitud [mm]", None))
        self.group_CEsf.setTitle(_translate("MainWindow", "Concentradores de Esfuerzos", None))
        self.label_Hombros.setText(_translate("MainWindow", "Hombros:              r [mm]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configTab), _translate("MainWindow", "Configuración", None))

        self.group_Cargas.setTitle(_translate("MainWindow", "Cargas", None))
        self.label_Tipo.setText(_translate("MainWindow", "Tipo", None))
        self.label_Angulo.setText(_translate("MainWindow", "Angulo [º]", None))
        self.label_Mi.setText(_translate("MainWindow", "Mi [N]", None))
        self.label_M.setText(_translate("MainWindow", "M [N]", None))
        self.label_PosXi.setText(_translate("MainWindow", "Xi[mm]", None))
        self.label_PosXf.setText(_translate("MainWindow", "Xf[mm]", None))
        self.edit_Mi.setText(_translate("MainWindow", "0", None))
        self.edit_PosXf.setText(_translate("MainWindow", "0", None))
        self.button_AddCarga.setText(_translate("MainWindow", "Añadir", None))
        self.button_SupCarga.setText(_translate("MainWindow", "Suprimir", None))
        self.group_R.setTitle(_translate("MainWindow", "Reacciones", None))
        self.label_RXY1.setText(_translate("MainWindow", "RY1:", None))
        self.label_RXZ1.setText(_translate("MainWindow", "RZ1:", None))
        self.label_RXY2.setText(_translate("MainWindow", "RY2:", None))
        self.label_RXZ2.setText(_translate("MainWindow", "RZ2:", None))
        self.group_Diag.setTitle(_translate("MainWindow", "Diagramas", None))
        self.button_CalcDiag.setText(_translate("MainWindow", "Calcular", None))
        self.radio_XY.setText(_translate("MainWindow", "Plano XY", None))
        self.radio_XZ.setText(_translate("MainWindow", "Plano XZ", None))
        self.radio_TT.setText(_translate("MainWindow", "Torsión/Total", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cargasTab), _translate("MainWindow", "Cargas", None))

        self.group_Diametros.setTitle(_translate("MainWindow", "Diámetros", None))
        self.label_FacDis.setText(_translate("MainWindow", "Factor de diseño:", None))
        self.label_SecCrit.setText(_translate("MainWindow", "Sec. Crítica:", None))
        self.button_ReCalc.setText(_translate("MainWindow", "->>", None))
        self.label_n.setText(_translate("MainWindow", "n:", None))
        self.label_Secciones.setText(_translate("MainWindow", "Secciones:", None))
        self.button_CalcDiam.setText(_translate("MainWindow", "Calcular ->", None))
        self.group_CMohr.setTitle(_translate("MainWindow", "Círculo de Mohr", None))
        self.label_Sigma1.setText(_translate("MainWindow", "σ1:", None))
        self.label_Sigma2.setText(_translate("MainWindow", "σ2:", None))
        self.label_Tau12.setText(_translate("MainWindow", "τ1,2:", None))
        self.label_SigmaTau.setText(_translate("MainWindow", "στ:", None))
        self.label_phi.setText(_translate("MainWindow", "φ:", None))
        self.group_TFalla.setTitle(_translate("MainWindow", "Teorías de Falla", None))
        self.label_MDuctil.setText(_translate("MainWindow", "Materiales Dúctiles:", None))
        self.label_MFragil.setText(_translate("MainWindow", "Materiales Frágiles:", None))
        self.radio_CMF.setText(_translate("MainWindow", "CMF", None))
        self.radio_CMF.setToolTip(_translate("MainWindow", "<html><head/><body><p>Coulomb-Mohr Frágil</p></body></html>", None))
        self.radio_MM.setText(_translate("MainWindow", "MM", None))
        self.radio_MM.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mohr Modificado</p></body></html>", None))
        self.radio_ENM.setText(_translate("MainWindow", "ENM", None))
        self.radio_ENM.setToolTip(_translate("MainWindow", "<html><head/><body><p>Esfuerzo Normal Máximo</p></body></html>", None))
        self.radio_ED.setText(_translate("MainWindow", "ED", None))
        self.radio_ED.setToolTip(_translate("MainWindow", "<html><head/><body><p>Energía de Distorsión</p></body></html>", None))
        self.radio_CMD.setText(_translate("MainWindow", "CMD", None))
        self.radio_CMD.setToolTip(_translate("MainWindow", "<html><head/><body><p>Coulomb-Mohr Dúctil</p></body></html>", None))
        self.radio_ECM.setText(_translate("MainWindow", "ECM", None))
        self.radio_ECM.setToolTip(_translate("MainWindow", "<html><head/><body><p>Esfuerzo Cortante Máximo</p></body></html>", None))
        self.group_SecCrit.setTitle(_translate("MainWindow", "Sección Crítica", None))
        self.label_Tauxz.setText(_translate("MainWindow", "τxz':", None))
        self.label_Sigmax.setText(_translate("MainWindow", "σx:", None))
        self.label_xcrit.setText(_translate("MainWindow", "x:", None))
        self.button_KtKts.setText(_translate("MainWindow", "Kt, Kts...", None))
        self.checkBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Calcular Coeficientes de Concentración de Esfuerzos</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dEstaticoTab), _translate("MainWindow", "D. Estático", None))

        self.group_Fluctuantes.setTitle(_translate("MainWindow", "Esfuerzos Fluctuantes", None))
        self.label_Sigma_a.setText(_translate("MainWindow", "σa:", None))
        self.label_Tau_a.setText(_translate("MainWindow", "τa: 0", None))
        self.label_Tau_m.setText(_translate("MainWindow", "τm:", None))
        self.label_Sigma_m.setText(_translate("MainWindow", "σm: 0", None))
        self.button_KfKfs.setText(_translate("MainWindow", "Kf, Kfs...", None))
        self.group_CFalla.setTitle(_translate("MainWindow", "Criterios de Falla a la Fatiga", None))
        self.radio_Goodman.setText(_translate("MainWindow", "ED-Goodman", None))
        self.radio_Gerber.setText(_translate("MainWindow", "ED-Gerber", None))
        self.radio_Soderberg.setText(_translate("MainWindow", "ED-Soderberg", None))
        self.radio_ASME.setText(_translate("MainWindow", "ED-ASME", None))
        self.label_Sigma_ap.setText(_translate("MainWindow", "σa\':", None))
        self.label_Sigma_mp.setText(_translate("MainWindow", "σm\':", None))
        self.group_RFatiga.setTitle(_translate("MainWindow", "Resistencia a la Fatiga", None))
        self.label_kc.setText(_translate("MainWindow", "--", None))
        self.label_ke.setText(_translate("MainWindow", "--", None))
        self.label_kd.setText(_translate("MainWindow", "--", None))
        self.button_ke.setText(_translate("MainWindow", "ke", None))
        self.button_kf.setText(_translate("MainWindow", "kf", None))
        self.label_Sut.setText(_translate("MainWindow", "Sut:", None))
        self.label_kf.setText(_translate("MainWindow", "--", None))
        self.label_ka.setText(_translate("MainWindow", "--", None))
        self.label_kb.setText(_translate("MainWindow", "--", None))
        self.button_kb.setText(_translate("MainWindow", "kb", None))
        self.button_ka.setText(_translate("MainWindow", "ka", None))
        self.button_kc.setText(_translate("MainWindow", "kc", None))
        self.label_Coef.setText(_translate("MainWindow", "Coeficientes de Marin:", None))
        self.button_kd.setText(_translate("MainWindow", "kd", None))
        self.label_Se.setText(_translate("MainWindow", "Se=ka·kb·kc·kd·ke·kf·Se\'", None))
        self.label_Se_2.setText(_translate("MainWindow", "Se=--", None))
        self.label_Sep.setText(_translate("MainWindow", "Se\':", None))
        self.group_DiametrosD.setTitle(_translate("MainWindow", "Diámetros", None))
        self.label_FacDisD.setText(_translate("MainWindow", "Factor de diseño:", None))
        self.label_SecCritD.setText(_translate("MainWindow", "Sec. Crítica:", None))
        self.button_ReCalcD.setText(_translate("MainWindow", "Iterar", None))
        self.label_nD.setText(_translate("MainWindow", "n:", None))
        self.button_CalcDiamD.setText(_translate("MainWindow", "Calcular ->", None))
        self.label_SeccionesD.setText(_translate("MainWindow", "Secciones:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dDinamicoTab), _translate("MainWindow", "D.Dinámico", None))

        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de EjesDim", None))

class Ui_Kt_Kts(object):
    def setupUi(self, Kt_Kts):
    	#Ventana Principal
        Kt_Kts.setObjectName(_fromUtf8("Kt_Kts"))
        Kt_Kts.resize(257, 147)
        self.gridLayout = QtGui.QGridLayout(Kt_Kts)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
   		#		-Entrada h
        self.edit_h = QtGui.QLineEdit(Kt_Kts)
        self.edit_h.setEnabled(False)
        self.edit_h.setMaximumSize(QtCore.QSize(45, 16777215))
        self.edit_h.setObjectName(_fromUtf8("edit_h"))
        self.gridLayout.addWidget(self.edit_h, 2, 4, 1, 1)
   		#		-Etiqueta r
        self.label_r = QtGui.QLabel(Kt_Kts)
        self.label_r.setObjectName(_fromUtf8("label_r"))
        self.gridLayout.addWidget(self.label_r, 3, 3, 1, 1)
        #		-Entrada D
        self.edit_D = QtGui.QLineEdit(Kt_Kts)
        self.edit_D.setEnabled(False)
        self.edit_D.setMaximumSize(QtCore.QSize(45, 16777215))
        self.edit_D.setObjectName(_fromUtf8("edit_D"))
        self.gridLayout.addWidget(self.edit_D, 1, 4, 1, 1)
        #		-Entrada d        
        self.edit_d = QtGui.QLineEdit(Kt_Kts)
        self.edit_d.setEnabled(False)
        self.edit_d.setMinimumSize(QtCore.QSize(0, 0))
        self.edit_d.setMaximumSize(QtCore.QSize(45, 16777215))
        self.edit_d.setObjectName(_fromUtf8("edit_d"))
        self.gridLayout.addWidget(self.edit_d, 0, 4, 1, 1)
        #		-Etiqueta D
        self.label_D = QtGui.QLabel(Kt_Kts)
        self.label_D.setObjectName(_fromUtf8("label_D"))
        self.gridLayout.addWidget(self.label_D, 1, 3, 1, 1)
        #		-Etiqueta h
        self.label_h = QtGui.QLabel(Kt_Kts)
        self.label_h.setObjectName(_fromUtf8("label_h"))
        self.gridLayout.addWidget(self.label_h, 2, 3, 1, 1)
        #		-Etiqueta d
        self.label_d = QtGui.QLabel(Kt_Kts)
        self.label_d.setObjectName(_fromUtf8("label_d"))
        self.gridLayout.addWidget(self.label_d, 0, 3, 1, 1)
        #		-Entrada r
        self.edit_r = QtGui.QLineEdit(Kt_Kts)
        self.edit_r.setEnabled(False)
        self.edit_r.setMaximumSize(QtCore.QSize(45, 16777215))
        self.edit_r.setObjectName(_fromUtf8("edit_r"))
        self.gridLayout.addWidget(self.edit_r, 3, 4, 1, 1)
        #		-Plot Kt
        self.graphics_Kt = Mpl(Kt_Kts)
        self.graphics_Kt.setMinimumSize(QtCore.QSize(112, 110))
        self.graphics_Kt.setObjectName(_fromUtf8("graphics_Kt"))
        self.gridLayout.addWidget(self.graphics_Kt, 0, 0, 3, 3)
        #		-Etiqueta Kts
        self.label_Kts = QtGui.QLabel(Kt_Kts)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Kts.setFont(font)
        self.label_Kts.setObjectName(_fromUtf8("label_Kts"))
        self.gridLayout.addWidget(self.label_Kts, 3, 1, 1, 1)
        #		-Etiqueta Kt
        self.label_Kt = QtGui.QLabel(Kt_Kts)
        self.label_Kt.setFont(font)
        self.label_Kt.setObjectName(_fromUtf8("label_Kt"))
        self.gridLayout.addWidget(self.label_Kt, 3, 0, 1, 1)

        self.retranslateUi(Kt_Kts)
        QtCore.QMetaObject.connectSlotsByName(Kt_Kts)

    def retranslateUi(self, Kt_Kts):
        Kt_Kts.setWindowTitle(_translate("Kt_Kts", "Hombro", None))
        self.label_r.setText(_translate("Kt_Kts", "r [mm]", None))
        self.label_D.setText(_translate("Kt_Kts", "D [mm]", None))
        self.label_h.setText(_translate("Kt_Kts", "h [mm]", None))
        self.label_d.setText(_translate("Kt_Kts", "d [mm]", None))
        self.label_Kts.setText(_translate("Kt_Kts", "Kts: ", None))
        self.label_Kt.setText(_translate("Kt_Kts", "Kt: ", None))

from mpl import Mpl

'''
kb_d=QtGui.QInputDialog.getDouble(None, "kb-Factor de Tamano",\
                                   "Establezca el diametro para iterar:",\
                                   value=str(round(self.dcrit,2),\
                                   minValue=0,decimals=2)
'''           
'''
class EjesDim_Gui(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.show()
p=EjesDim_Gui()
'''