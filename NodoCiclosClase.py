class Nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def agregar_al_final(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    if nodo_inicial == None:
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial

def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo

def imprimir_lista(nodo):
    while nodo != None:
        print(f"Tenemos {nodo.dato}")
        nodo = nodo.siguiente

def obtener_cabeza(nodo_inicial):
    return nodo_inicial

def obtener_cola(nodo_inicial):
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    return temporal

def existe(nodo, busqueda):
    while nodo != None:
        if nodo.dato == busqueda:
            return True
        nodo = nodo.siguiente
    return False

def eliminar(nodo, busqueda):
    if nodo == None:
        return
    if nodo.dato == busqueda:
        return nodo.siguiente
    temporal = nodo
    while temporal.siguiente != None:
        if temporal.siguiente.dato == busqueda:
            if temporal.siguiente.siguiente != None:
                temporal.siguiente = temporal.siguiente.siguiente
            else:
                temporal.siguiente = None
                return nodo
        temporal = temporal.siguiente
    return nodo
    
class Mascota():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def __str__(self):
        return f"Mascota llamada {self.nombre}"
    
    def __eq__(self, __o: object) -> bool:
        return self.nombre == __o.nombre

def main():
    lista = None
    lista = agregar_al_final(lista, Mascota("Maggie"))
    lista = agregar_al_final(lista, Mascota("Grimm"))
    lista = agregar_al_inicio(lista, Mascota("Panqué"))
    lista = agregar_al_inicio(lista, Mascota("Ejemplo"))
    print("Antes de eliminar: ")
    imprimir_lista(lista)
    lista = eliminar(lista, Mascota("Ejemplo"))
    print("Después de eliminar: ")
    imprimir_lista(lista)
    print(existe(lista, Mascota("Grimm")))
    print(existe(lista, Mascota("Ejemplo")))
    print(obtener_cabeza(lista).dato)
    print(obtener_cola(lista).dato)
    
main()
