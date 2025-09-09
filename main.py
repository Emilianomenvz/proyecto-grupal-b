from clases.operaciones import Operaciones as Nombres
from clases.operaciones import ordenarLista

def main():
    test = Nombres()
    
    #Prueba base
    print(test.saludoAlejandroMontes())
    
    #Realiza aquí tu prueba
    lista=[3,2,5,1,4]
    print(ordenarLista(lista))

if __name__ == '__main__':
    main()    