from clases.operaciones import Operaciones
from clases.operaciones import NumeroMayor


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())
    lista=[3,2,5,1,4]
    
    #Realiza aquí tu prueba

    print(test.ordenarLista(lista))

if __name__ == '__main__':
    main()

# Extraer el número mayor de una lista
def prueba_numero_mayor():
    lista = [3, 2, 5, 1, 4]
    numero_mayor_instancia = NumeroMayor(lista)
    print("El número mayor es:", numero_mayor_instancia.numero_mayor())
    prueba_numero_mayor()
    