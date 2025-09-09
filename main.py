from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())

    
    #Realiza aquí tu prueba
    print(test.verificarPar())

   
    
    #Realiza aquí tu prueba


    print(test.minimo(lista))

    # Prueba del nuevo método reemplazarEspacios
    texto = "Hola mundo con espacios"
    caracter = "_"
    print(f"Texto original: '{texto}'")
    print(f"Reemplazando espacios con '{caracter}':", test.reemplazarEspacios(texto, caracter))




if __name__ == '__main__':
    main()
    
