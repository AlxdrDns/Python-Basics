clientes = 'Pablo,Ricardo,'


def crear_cliente(nombre_cliente):
    global clientes
    if nombre_cliente not in clientes:
        clientes += nombre_cliente
        _agregar_coma()
    else:
        print('El cliente ya está en la lista')

def listar_clientes():
    global clientes
    print(clientes)


def _agregar_coma():
    global clientes
    clientes += ','


def _imprimir_bienvenida():
    print('BIENVENIDOS AL SISTEMA DE VENTAS')
    print('*' * 50)
    print('Qué deseas hacer hoy?')
    print('[C]rear un cliente')
    print('[B]orrar un cliente')


if __name__ == '__main__':
    _imprimir_bienvenida()
    comando = input()
    if comando == 'C':
        nombre_cliente = input('Cuál es el nombre del cliente?')
    elif comando == 'D':
        pass
    else:
        print('Comando inválido')
    crear_cliente(nombre_cliente)
    listar_clientes()