
class Persona:

    def __init__(self, nombre, edad): #Constructor de la clase Persona
        self.nombre = nombre #Atributo de la clase Persona
        self.edad = edad #Atributo de la clase Persona

    def hola(self): #Método de la clase Persona
        print('Hola, mi nombre es {} y tengo {} años'.format(self.nombre, self.edad))


if __name__ == '__main__':
    persona = Persona('Alexander', 32) #Objeto persona de la clase Persona
    print ('Edad: {}'.format(persona.edad)) #Acceso al atributo edad de la instancia persona
    persona.hola()