class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        self.numero = 0
        self.__x=int(0)
        self.__y=int(0)
        
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    
    def reemplazarEspacios(self, texto: str, caracter: str) -> str:
        
        if not caracter or len(caracter) != 1:
            raise ValueError("El caracter debe ser un único símbolo.")



    def verificarPar(self):
        self.numero = int(input("Ingrese un número: "))
        if self.numero % 2 == 0:
            return True
        else:
            return False 

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

    def generarTablaMultiplicar(self,x,y):
        self.__x=x
        self.__y=y
        for i in range(0,self.__y+1):
            print(self.__x*i)
            return
        
        
        

