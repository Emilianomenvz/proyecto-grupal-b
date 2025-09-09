class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    
    def promedio(self, lista):
        if not lista:
            return 0
        return sum(lista) / len(lista)