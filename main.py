from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())    
    #Realiza aquí tu prueba
    print(test.promedio([1,2,3,4,5,6,7,8,9,10]))    

if __name__ == '__main__':
    main()