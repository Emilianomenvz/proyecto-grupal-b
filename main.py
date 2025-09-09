from clases.operaciones import Operaciones


def main():
    test = Operaciones()
    #Prueba base
    print(test.saludoAlejandroMontes())
    lista=[3,2,5,1,4]
    
    #Realiza aquí tu prueba

    print(test.ordenarLista(lista))

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