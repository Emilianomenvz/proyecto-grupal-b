class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    
    def reemplazarEspacios(self, texto: str, caracter: str) -> str:
        
        if not caracter or len(caracter) != 1:
            raise ValueError("El caracter debe ser un único símbolo.")

        return texto.replace(" ", caracter)
