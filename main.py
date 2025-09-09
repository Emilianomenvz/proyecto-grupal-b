from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base

    print(test.saludoAlejandroMontes())    
    #Realiza aquí tu prueba
    print(test.promedio([1,2,3,4,5,6,7,8,9,10]))    

    print(test.saludoAlejandroMontes())

    
    #Realiza aquí tu prueba
    print(test.serieFibonacci(8))




    op = Operaciones()

    print(op.esPar(2))   
    print(op.esPar(3))   
    print(op.esPar(0)) 


    
    #Realiza aquí tu prueba
    test = Operaciones()
    print(test.numero_mayor())
    lista=[10,23,1,54,53]

    print(test.num_mayor(lista))


    lista = [5, 3, 8, 1, 4]

    vocales = Operaciones()
    print(vocales.contarVocales("Hola mundo"))
    
    print(test.ordenarLista(lista))


    print(test.verificarPar())

    
    #Realiza aquí tu prueba


    print(test.minimo(lista))

    # Prueba del nuevo método reemplazarEspacios
    texto = "Hola mundo con espacios"
    caracter = "_"
    print(f"Texto original: '{texto}'")
    print(f"Reemplazando espacios con '{caracter}':", test.reemplazarEspacios(texto, caracter))

    lista_elian = [1, 2, 2, 3, 1, 4, 2, 5]
    print("Lista original:", lista_elian)
    print("Lista sin duplicados:", test.eliminarDuplicados(lista_elian))



# Prueba de contarPalabraEnTexto
    texto2 = "hola mundo hola hola universo"
    palabra = "hola"
    print(f"\nTexto: '{texto2}'")
    print(f"La palabra '{palabra}' aparece", op.contarPalabraEnTexto(texto2, palabra), "veces.")

if __name__ == '__main__':


    main()


