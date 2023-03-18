annio = int(input("Coloque un annio"))

def bisiesto(annio):
    if (annio % 4 == 0 and annio % 100 != 0) or annio % 400 == 0:
        print(f"el annio {annio} es bisiesto")
    else:
        print(f"el annio {annio} no es bisiesto")

bisiesto(annio)
