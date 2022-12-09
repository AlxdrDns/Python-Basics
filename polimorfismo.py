
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'{self.nombre} va caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre) #Referencia a la superclase Persona

    def avanza(self): #Este método debe de tener los mismos parámetros del método de la superclase
        print(f'{self.nombre} va en bicicleta')


def main():
    persona = Persona('Alexander')
    persona.avanza()
    ciclista = Ciclista('Pedro')
    ciclista.avanza()


if __name__ == '__main__':
    main()