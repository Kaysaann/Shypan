from math import *
import math

# Variables
verif = True

# Fonctions EncodageUser
def EncodageUser(msg, dataType):
    while verif:
        dataTemp = input("\n" + msg + "\n>>> ")
        try:
            dataTemp = dataType(dataTemp)
            return dataTemp
        except:
            print("\nVeuillez entrer une valeur valide.")

# Fonctions Calcul
def CalcAdd(nb1, nb2):
    try:
        return nb1 + nb2
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcDiv(nb1, nb2):
    try:
        return nb1 / nb2
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcDeff(nb1, nb2):
    try:
        return nb1 - nb2
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcSin(nb):
    try:
        return math.sin(nb)
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcCos(nb):
    try:
        return math.cos(nb)
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")   

def CalcSqrt(nb):
    try:
        return math.sqrt(nb)
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcPow(nb1, power):
    try:
        return nb1 ** power
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcLog(nb):
    try:
        return math.log(nb)
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcExp(nb):
    try:
        return math.exp(nb)
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcTan(nb):
    try:
        return math.tan(nb)
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

def CalcCotan(nb):
    try:
        return 1 / math.tan(nb)
    except ValueError:
        print("\nLa valeur rentrer n'est pas un nombre (", ValueError, ")")

