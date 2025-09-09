class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        self.numero = 0
        
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def verificarPar(self):
        self.numero = int(input("Ingrese un número: "))
        if self.numero % 2 == 0:
            return True
        else:
            return False 

