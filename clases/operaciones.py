class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"

    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def serieFibonacci(self, n):
        a, b = 0, 1
        while a <= n:
            print(a, end=" ")
            a, b = b, a + b
        print()
