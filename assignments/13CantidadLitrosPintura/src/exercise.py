import math
def main():
    #escribe tu código abajo de esta línea
    a = float(input("Area a pintar en metros: "))
    r = float(input("Rendimiento (m2/l): "))
    l = (a / r)
    print("Litros a comprar:",math.ceil(l))

if __name__ == '__main__':
    main()
