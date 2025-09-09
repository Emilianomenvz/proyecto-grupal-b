class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def ordenarLista(self, lista):
        return sorted(lista)
    
    # Extraer el número mayor de una lista
class NumeroMayor:
    
    def __init__(self, lista):
        self.lista = lista

    def numero_mayor(self):
        return max(self.lista)
