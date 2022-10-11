#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tomas
#
# Created:     11/10/2022
# Copyright:   (c) Tomas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    def suma(numero):
        if numero == 1:
            return 1
        else:
            return numero + suma(numero-1)

    print(suma(9))



if __name__ == '__main__':
    main()
