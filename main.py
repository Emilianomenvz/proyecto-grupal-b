from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())

    
    #Realiza aquí tu prueba
    print(test.verificarPar())

   
    
    #Realiza aquí tu prueba

    # Prueba del nuevo método reemplazarEspacios
    texto = "Hola mundo con espacios"
    caracter = "_"
    print(f"Texto original: '{texto}'")
    print(f"Reemplazando espacios con '{caracter}':", test.reemplazarEspacios(texto, caracter))



if __name__ == '__main__':
    main()
    
def contarPalabraEnTexto(texto, palabra):
    # Convertimos a minúsculas
    texto = texto.lower()
    palabra = palabra.lower()
    
    # Separamos en palabras
    palabras = texto.split()
    
    # Contamos las coincidencias exactas
    return palabras.count(palabra)

texto = "Hola mundo, hola a todos en este mundo."
resultado1 = contarPalabraEnTexto(texto, "hola")
resultado2 = contarPalabraEnTexto(texto, "mundo")
resultado3 = contarPalabraEnTexto(texto, "python")

print("Veces que aparece 'hola':", resultado1)
print("Veces que aparece 'mundo':", resultado2)
print("Veces que aparece 'python':", resultado3)