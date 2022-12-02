#(C)reate
#(R)ead or retreive
#(U)pdate
#(D)elete


import sys


clientes = [
    {
        'nombre': 'Pablo',
        'empresa': 'Google',
        'email': 'pablo@google.com',
        'posicion': 'Software Engineer'
    },
    {
        'nombre': 'Ricardo',
        'empresa': 'Facebook',
        'email': 'ricardo@facebook.com',
        'posicion': 'Data Engineer'
    }
]


def crear_cliente(cliente):
    global clientes
    if cliente not in clientes:
        clientes.append(cliente)
    else:
        print('El cliente ya está en la lista')


def actualizar_cliente(nombre_cliente, nombre_cliente_actualizado):
    global clientes
    if nombre_cliente in clientes:
        index = clientes.index(nombre_cliente)
        clientes[index] = nombre_cliente_actualizado
    else:
        print('El cliente no se encuentra en la lista de clientes')


def borrar_cliente(nombre_cliente):
    global clientes
    if nombre_cliente in clientes:
        clientes.remove(nombre_cliente)
    else:
        print('El cliente no se encuentra en la lista de clientes')


def buscar_cliente(nombre_cliente):
    global clientes
    for cliente in clientes:
        if cliente != nombre_cliente:
            continue
        else:
            return True


def listar_clientes():
    for idx, cliente in enumerate(clientes):
        print('{uid} | {nombre} | {empresa} | {email} | {posicion}'.format(
            uid=idx, 
            nombre=cliente['nombre'],
            empresa=cliente['empresa'],
            email=cliente['email'],
            posicion=cliente['posicion']))


def _imprimir_bienvenida():
    print('BIENVENIDOS AL SISTEMA DE VENTAS')
    print('*' * 50)
    print('Qué deseas hacer hoy?')
    print('[C]rear un cliente')
    print('[A]ctualizar un cliente')
    print('[E]liminar un cliente')
    print('[B]uscar un cliente')


def _get_campo_cliente(nombre_campo):
    campo = None
    while not campo:
        campo = input('Cuál es el cliente {}?'.format(nombre_campo))
    return campo


""" def _get_nombre_cliente():
    nombre_cliente = None
    while not nombre_cliente:
        nombre_cliente = input('Cuál es el nombre del cliente?')
        if nombre_cliente == 'Salir':
            nombre_cliente = None
            break
    if not nombre_cliente:
            sys.exit()
    return nombre_cliente """


if __name__ == '__main__':
    _imprimir_bienvenida()
    comando = input()
    comando = comando.upper()
    if comando == 'C':
        cliente = {
            'nombre': _get_campo_cliente('nombre'),
            'empresa': _get_campo_cliente('empresa'),
            'email': _get_campo_cliente('email'),
            'posicion': _get_campo_cliente('posicion')
        }
        crear_cliente(cliente)
        listar_clientes()
    elif comando == 'E':
        nombre_cliente = _get_nombre_cliente()
        borrar_cliente(nombre_cliente)
        listar_clientes()
    elif comando == 'A':
        nombre_cliente = _get_nombre_cliente()
        nombre_cliente_actualizado = input('Cuál es el nombre del cliente actualizado?')
        actualizar_cliente(nombre_cliente, nombre_cliente_actualizado)
        listar_clientes()
    elif comando == 'B':
        nombre_cliente = _get_nombre_cliente()
        busqueda = buscar_cliente(nombre_cliente)
        if busqueda:
            print('El cliente está en la lista de clientes')
        else:
            print('El cliente: {} no está en la lista de clientes'.format(nombre_cliente))
        listar_clientes()
    else:
        print('Comando inválido')