"""

"""
import sys
import os
from clear_screen import clear
import time
import termtables as tt
from Operator import *
import textwrap

"""
Variables estáticas
"""

CEND = '\033[0m'     # código de escape, para indicar donde termina el cambiar color en la terminarl
CGREEN = '\033[92m'  # código de escape, cambiar color del texto en la terminarl
CBLUE = '\033[94m'   # código de escape, cambiar color del texto en la terminarl
CYELLOW = '\033[93m' # código de escape, cambiar color del texto en la terminarl

# menu principal
MENU_PRINCIPAL = CGREEN + '\t\tMenú\033[0m'+ CBLUE +\
"""
\t1. Opción 1
\t2. Opción 2
\t3. Autores
\t4. Salir""" + CEND

OPCION_SALIR = 4

INSTRUCCIONES_REL_OP1 = ('{3}Se ingresara una relación a la vez, donde cada uno de los valores debera estar separado por coma (,).{0}' +
     '\n\n{2}Ejemplo:{0} {3}ingresar: {0}{2}1,2{0} {3}luego debe de seleccionar la tecla {0}{1}"ENTER"{0} {3}para ingresar la siguiente relación. ' +
     '\n\nPara indicar que {1}terminó de ingresar{0} {3}las relaciones{0} {1}ingrese{0} {3}únicamente la letra {0}{1}f{0} {3}y luego seleccione \nla tecla {0}{1}"ENTER"{0}.').format(CEND,CYELLOW,CGREEN,CBLUE)

def convert(list):
    return tuple(i for i in list)

def toArray(valor):
    arreglo = []

    tmp = valor.split(',')

    if(len(tmp)>0):
        for value in tmp:
            if(es_entero(value)):
                arreglo.append(int(value))
            else:
                return []

    return arreglo

def printMatrix(Matrix):

    asciiMatrix = ""

    try:
        asciiMatrix = tt.to_string(Matrix,
            # header=["Name", "Age"],
            style=tt.styles.ascii_thin_double,
            # alignment="ll",
            # padding=(0, 1),
        )
    except:
        asciiMatrix = ""

    return asciiMatrix

def string_lleno(string_evaluar):
    """
    :arg string_evaluar: variable que se evaluara
    :return True si no esta vacío, False si está vacío
    """
    return bool(string_evaluar and string_evaluar.strip())

def es_entero(digito):
    """
    Método para identificar si todo un string es un digito o número
    :param digito: String que deseamos verificar si es un entero
    :return: True or False
    """

    # Verificamos si tiene signo al inicio
    if(digito[0] in ('-', '+')):
        return digito[1:].isdigit()
    return digito.isdigit()

def opcion1():

    conjunto = []

    control = True

    # Ingreso de la definicion del conjunto
    while control:
        # Limpiamos la terminal
        clear()

        # Titulo de la operacion
        print(CGREEN + "\t\tDefinir el Conjunto.\n" + CEND)

        #Solicitamo ingreso del conjunto
        in_conjunto = input(CBLUE+"Ingrese los numeros del conjunto separado por comas (ejemplo: 1,2,3,4) : "+CEND)

        if(string_lleno(in_conjunto)):
            # Separando conjunto y validando que sean numeros
            conjunto = toArray(in_conjunto)

            if((conjunto is not None) and (len(conjunto) > 0)):
                control = False
            else:
                print(CYELLOW + "\n\n\t\tUn dato del conjunto no es numerico, ingreselo de nuevo. \n\t\tSi desea regresar al menu principal seleccione ctrl + C"+CEND)
                time.sleep(2)
        else:
            print(CYELLOW + "\n\n\t\tNo ha definido un conjunto, si desea regresar al menu seleccione ctrl + C")
            time.sleep(2)


    conjunto = convert(conjunto)
    relacion = []
    control = True

    # Ingreso de la relacion
    while control:
        # Limpiamos la terminal
        clear()

        # Titulo de Operacion a realizar
        print(CGREEN + "\t\tIngreso de Relación" + CEND)

        print(CBLUE+"\nINSTRUCCIONES:\n"+CEND)

        # mostrando instrucciones de como ingresar una relaci[on
        print(INSTRUCCIONES_REL_OP1)

        # Mostrando el conjunto ingresado
        print(("\n\n\t{0}Conjunto Ingresado:{1} {2}\n").format(CBLUE,CEND,conjunto))

        # Si ya hay una relacion ingresada la mostraremos
        if(len(relacion) > 0):
            print("\n\t{1}Relación Ingresada:{0} {2}".format(CEND,CBLUE,relacion))
            print()

        # Solicitamo ingreso de la relacion
        in_relacion = input(CBLUE + "Ingrese la relación  (ejemplo: 1,2,3,4) : " + CEND)

        if (string_lleno(in_relacion)):
            # Separando conjunto y validando que sean numeros
            if('f' in in_relacion):
                control = False
            else:
                #separamos componentes
                temp_relacion = toArray(in_relacion)
                if ((temp_relacion is not None) and (len(temp_relacion) > 0)):
                    temp_relacion = convert(temp_relacion)
                    relacion.append(temp_relacion)
                    print("Se agrego la relacion: {0}".format(temp_relacion))
                    time.sleep(2)

                else:
                    print(CYELLOW + "\n\n\t\tUn dato del conjunto no es numerico, ingreselo de nuevo. \n\t\tSi desea regresar al menu principal seleccione ctrl + C" + CEND)
                    time.sleep(2)


    if((len(conjunto) > 0) and (len(relacion) > 0)):

        # DEFINIR JOINT (CONJUNTO)
        #joint = (1, 2, 3, 4)
        # DEFINIR RELATION (RELACION)
        #relation = [(1, 3), (1, 4), (2, 1), (3, 2)]

        # Limpiamos la terminal
        clear()

        # Titulo de Operacion a realizar
        print(CGREEN + "\n\n\t\tCalculando Relacion Transitiva" + CEND)

        ops = Operator(conjunto, relacion)

        return printMatrix(ops.closedTransitiveRel())



    return ""


try:
    while True:

        # Limpiamos la terminal
        clear()

        # Mostramos menú principal
        print(MENU_PRINCIPAL)

        # Leemos opcion seleccionada por el usuario
        opmenu_principal = input("Ingrese el número de la opción del menú: ")

        # Verificamos si se ingreso una opción
        if (string_lleno(opmenu_principal)):

            # Verificamos si se ingreso un digito entero
            if (es_entero(opmenu_principal)):

                opmenu_principal = int(opmenu_principal)

                # Verificamos si el usuario desea salir
                if (opmenu_principal == OPCION_SALIR):
                    print(CYELLOW + '\n\t\tSaliendo del Programa' + CEND)
                    # Saliendo del programa
                    exit()
                elif(opmenu_principal == 1):
                    matriz = opcion1()

                    if(string_lleno(matriz)):
                        clear()
                        print("\n\t\tMatriz Transitiva\n\n")
                        print(matriz)
                        print()
                        input("Seleccione cualquier tecla para continuar: ")
                        
            else:
                print(CYELLOW + "\nDebe ingresar el numero de la opcion deseada" + CEND)
                time.sleep(2)
        else:
            print(CYELLOW + "\nDebe ingresar la opcion deseada" + CEND)
            time.sleep(2)

except KeyboardInterrupt:
        print(CYELLOW +'\n\n\t\tSaliendo del Programa'+CEND)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)