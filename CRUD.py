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
        'puesto': 'Software Engineer'
    },
    {
        'nombre': 'Ricardo',
        'empresa': 'Facebook',
        'email': 'ricardo@facebook.com',
        'puesto': 'Data Engineer'
    }
]


def crear_cliente(cliente):
    global clientes
    if cliente not in clientes:
        clientes.append(cliente)
    else:
        print('El cliente ya está en la lista')


def actualizar_cliente(id_cliente, cliente_actualizado):
    global clientes
    if len(clientes) - 1 >= id_cliente:
        clientes[id_cliente] = cliente_actualizado
    else:
        print('El cliente no se encuentra en la lista de clientes')


def borrar_cliente(id_cliente):
    global clientes
    for idx, cliente in enumerate(clientes):
        if idx == id_cliente:
            del clientes[idx]
            break


def buscar_cliente(nombre_cliente):
    global clientes
    for cliente in clientes:
        if cliente['nombre'] != nombre_cliente:
            continue
        else:
            return True


def listar_clientes():
    print('uid | nombre | empresa | email | puesto')
    print('*' * 50)
    for idx, cliente in enumerate(clientes):
        print('{uid} | {nombre} | {empresa} | {email} | {puesto}'.format(
            uid=idx, 
            nombre=cliente['nombre'],
            empresa=cliente['empresa'],
            email=cliente['email'],
            puesto=cliente['puesto']))


def _imprimir_bienvenida():
    print('BIENVENIDOS AL SISTEMA DE VENTAS')
    print('*' * 50)
    print('Qué deseas hacer hoy?')
    print('[C]rear un cliente')
    print('[L]istar clientes')
    print('[A]ctualizar un cliente')
    print('[E]liminar un cliente')
    print('[B]uscar un cliente')


def _get_campo_cliente(nombre_campo, mensaje='Cuál es el/la {} del cliente?'):
    campo = None
    while not campo:
        campo = input(mensaje.format(nombre_campo))
    return campo


def _get_cliente_desde_usuario():
    cliente = {
        'nombre': _get_campo_cliente('nombre'),
        'empresa': _get_campo_cliente('empresa'),
        'email': _get_campo_cliente('email'),
        'puesto': _get_campo_cliente('puesto'),
    }
    return cliente


if __name__ == '__main__':
    _imprimir_bienvenida()
    comando = input()
    comando = comando.upper()
    if comando == 'C':
        cliente = _get_cliente_desde_usuario()
        crear_cliente(cliente)
        listar_clientes()
    elif comando == 'L':
        listar_clientes()
    elif comando == 'A':
        id_cliente = int(_get_campo_cliente('id'))
        cliente_actualizado = _get_cliente_desde_usuario()
        actualizar_cliente(id_cliente, cliente_actualizado)
        listar_clientes()
    elif comando == 'E':
        id_cliente = int(_get_campo_cliente('id'))
        borrar_cliente(id_cliente)
        listar_clientes()
    elif comando == 'B':
        nombre_cliente = _get_campo_cliente('nombre')
        busqueda = buscar_cliente(nombre_cliente)
        if busqueda:
            print('El cliente si está en la lista de clientes')
        else:
            print('El cliente: {} no está en la lista de clientes'.format(nombre_cliente))
        listar_clientes()
    else:
        print('Comando inválido')