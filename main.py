from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())
    lista=[3,2,5,1,4]
    
    #Realiza aquí tu prueba

if __name__ == '__main__':
    main()
    
op = Operaciones()

print(op.esPar(2))   
print(op.esPar(3))   
print(op.esPar(0))   
