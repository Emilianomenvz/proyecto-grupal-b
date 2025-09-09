class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def ordenarLista(self, lista):
        return sorted(lista)
    
    def minimo(self, lista):
        menor = lista[0]
        for num in lista:
            if num < menor:
                menor = num
        return menor
