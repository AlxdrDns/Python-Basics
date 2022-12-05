class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hola(self):
        print('Hola, mi nombre es {} y tengo {} años'.format(self.nombre, self.edad))

if __name__ == '__main__':
    persona = Persona('Alexander', 32)

print ('Edad: {}'.format(persona.edad))
persona.hola()