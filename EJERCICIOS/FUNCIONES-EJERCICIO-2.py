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
    PI = 3.14159
    def area_circulo(radio):
        area = PI * radio ** 2
        return area

    circulo = area_circulo(20)
    print(circulo)
if __name__ == '__main__':
    main()
