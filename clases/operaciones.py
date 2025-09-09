class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

        self.numero = 0
        
        

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    

    def numero_mayor(self):
        return max(self.lista)


    def promedio(self, lista):
        if not lista:
            return 0
        return sum(lista) / len(lista)

    def reemplazarEspacios(self, texto: str, caracter: str) -> str:
        
        if not caracter or len(caracter) != 1:
            raise ValueError("El caracter debe ser un único símbolo.")



    def verificarPar(self):
        self.numero = int(input("Ingrese un número: "))
        if self.numero % 2 == 0:
            return True
        else:
            return False 


    def contarVocales(texto):
        contador = 0
        for letra in texto.lower():
            if letra in "aeiou":
                contador += 1
        return contador


    def serieFibonacci(self, n):
        a, b = 0, 1
        while a <= n:
            print(a, end=" ")
            a, b = b, a + b
        print()


    def num_mayor(self, lista):
        mayor=lista[0]
        for num in lista:
            if num > mayor: 
                mayor=num
        return mayor
    
    
    def ordenarLista(self, lista):
        return sorted(lista)
    

    def minimo(self, lista):
        menor = lista[0]
        for num in lista:
            if num < menor:
                menor = num
        return menor

    def contarPalabraEnTexto(texto, palabra):
        texto = texto.lower()
        palabra = palabra.lower()
        palabras = texto.split()
        return palabras.count(palabra)

        return texto.replace(" ", caracter)

