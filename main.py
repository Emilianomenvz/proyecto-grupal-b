from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())
   
    
    #Realiza aquí tu prueba

    # Prueba del nuevo método reemplazarEspacios
    texto = "Hola mundo con espacios"
    caracter = "_"
    print(f"Texto original: '{texto}'")
    print(f"Reemplazando espacios con '{caracter}':", test.reemplazarEspacios(texto, caracter))


# Prueba de contarPalabraEnTexto
    texto2 = "hola mundo hola hola universo"
    palabra = "hola"
    print(f"\nTexto: '{texto2}'")
    print(f"La palabra '{palabra}' aparece", op.contarPalabraEnTexto(texto2, palabra), "veces.")

if __name__ == '__main__':
    main()
    
