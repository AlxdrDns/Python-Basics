
class Rectangulo:

    def __init__(self, base, altura): #Constructor de la clase Rectangulo
        self.base = base
        self.altura = altura

    def area(self): #Método de la clase Rectangulo
        return self.base * self.altura

class Cuadrado(Rectangulo): #La clase Cuadrado extiende la clase Rectángulo

    def __init__(self, lado): #Constructor de la clase Cuadrado
        super().__init__(lado, lado) #super() nos permite obtener una referencia de la superclase


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
