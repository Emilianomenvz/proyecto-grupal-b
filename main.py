from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())
    lista=[3,2,5,1,4]
    
    #Realiza aquí tu prueba

    print(test.minimo(lista))


if __name__ == '__main__':
    main()