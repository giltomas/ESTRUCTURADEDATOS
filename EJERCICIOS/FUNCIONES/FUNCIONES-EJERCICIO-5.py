#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     10/10/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    def recortar(numero, inferior, superior):
        if numero<inferior:
            return inferior
        if numero>superior:
            return superior
        if numero>inferior and numero<superior:
            return numero

    recorte = recortar(5,4,6)
    print(recorte)



if __name__ == '__main__':
    main()
