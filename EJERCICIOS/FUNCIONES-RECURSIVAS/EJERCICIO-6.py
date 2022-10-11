#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Tomas
#
# Created:     11/10/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    def bomba(nro):
        nro -= 1
        if nro>0:
            print(nro)
            bomba(nro)
        else:
            print("¡Booom!")

    bomba(11)









if __name__ == '__main__':
    main()
