
class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property   #Getter para acceder al atributo privado region
    def region(self):
        return self.__region

    @region.setter #Setter para modificar el atributo privado region
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es válida en {self.__pais}')
    

if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['Quito', 'Guayaquil'])
    print(casilla.region)
    casilla.region = 'Ambato'
    print(casilla.region)