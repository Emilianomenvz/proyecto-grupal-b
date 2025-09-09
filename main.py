from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())
    lista=[3,2,5,1,4]
    
    #Realiza aquí tu prueba
    test = Operaciones()
    print(test.numero_mayor())
    lista=[10,23,1,54,53]

    print(test.ordenarLista(lista))

if __name__ == '__main__':
    main()

