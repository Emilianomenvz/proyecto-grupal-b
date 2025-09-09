class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def num_mayor(self, lista):
        mayor=lista[0]
        for num in lista:
            if num > mayor: 
                mayor=num
        return mayor
    
    
