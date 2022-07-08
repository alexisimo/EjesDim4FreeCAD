import os
import FreeCAD

def im_mat():
    '''Funcion que importa las propiedades de los materiales del archivo
    lista_materiales.txt.'''
    #Guarda en una variable la direccion donde se encuentra el archivo.
    dir=os.path.dirname(__file__)
    #Extrae el texto y lo almacena en data
    data=open(os.path.join(dir, 'lista_materiales.txt'),'r')
    #Enlista el texto por fila
    mat= list(data)
    #Crea variables vacias para iterar
    Lista=[]
    Sut={}
    Sy={}
    Suc={}

    a=0
    #ACEROS
    #Extrae las propiedades de los aceros
    for i in range(len(mat)):
        if mat[i][0]!= '-' and mat[i][0]!= 'A':
            if mat[i][0:1]=='\n':
                a=i+1
                break
            Sut[mat[i][0:7]]=float(mat[i][25:33])
            Sy[mat[i][0:7]]=float(mat[i][34:-1])
            Suc[mat[i][0:7]]='--'
            Lista.append('AISI '+mat[i][0:7])
            
    #ACEROS CON TRATAMIENTO TERMICO
    #Extrae las propiedades de los aceros con tratamiento termico
    for i in range(len(mat)):
        if mat[i+a][0]!= '-' and mat[i+a][0]!= 'A':
            if mat[i+a][0:1]=='\n':
                a+=i+1
                break
            Sut[mat[i+a][0:22]]=float(mat[i+a][25:33])
            Sy[mat[i+a][0:22]]=float(mat[i+a][34:-1])
            Suc[mat[i+a][0:22]]=Sut[mat[i+a][0:22]]
            Lista.append('AISI '+mat[i+a][0:22])
            
    #HIERROS FUNDIDOS
    #Extrae las propiedades de los hierros fundidos
    for i in range(len(mat)):
        if mat[i+a][0]!= '-' and mat[i+a][0]!= 'A':
            if mat[i+a][0:1]=='\n':
                a+=i
                break
            Sut[mat[i+a][0:2]]=float(mat[i+a][25:33])
            Sy[mat[i+a][0:2]]='--'
            Suc[mat[i+a][0:2]]=float(mat[i+a][34:-1])
            Lista.append('ASTM '+mat[i+a][0:2])
    #Cierra el archivo
    data.close()
    #Regresa una lista con los nombres, y los diccionarios de las propiedades
    return Lista, Sut, Sy, Suc

#FreeCAD.Console.PrintMessage(im_mat()[1]['60']) 
