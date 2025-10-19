class Nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def agregar_al_final_rec(nodo_actual, dato):
    # Caso base 1: La lista está vacía (nodo_actual es None).
    if nodo_actual is None:
        return Nodo(dato)
    
    # Caso recursivo: Si hay un nodo siguiente, llama a la función en el siguiente nodo.
    if nodo_actual.siguiente is not None:
        # El 'siguiente' del nodo actual se convierte en el resultado de la llamada recursiva.
        nodo_actual.siguiente = agregar_al_final_rec(nodo_actual.siguiente, dato)
    # Caso base 2: Hemos llegado al final (nodo_actual.siguiente es None).
    else:
        nodo_actual.siguiente = Nodo(dato)
        
    return nodo_actual

def imprimir_lista_rec(nodo):
    if nodo is not None:
        print(f"Tenemos {nodo.dato}")
        imprimir_lista_rec(nodo.siguiente) # Llamada recursiva

def obtener_cola_rec(nodo):
    # Caso base: El nodo actual es el último (su 'siguiente' es None).
    if nodo is None or nodo.siguiente is None:
        return nodo
    
    # Caso recursivo: Mover al siguiente nodo.
    return obtener_cola_rec(nodo.siguiente)

def existe_rec(nodo, busqueda):
    # Caso base 1: Hemos llegado al final sin encontrar el dato.
    if nodo is None:
        return False
    
    # Caso base 2: Encontramos el dato.
    if nodo.dato == busqueda:
        return True
    
    # Caso recursivo: Comprobar en el resto de la lista.
    return existe_rec(nodo.siguiente, busqueda)

def eliminar_rec(nodo, busqueda):
    # Caso base 1: La lista está vacía.
    if nodo is None:
        return None
        
    # Caso base 2: El nodo actual es el que hay que eliminar.
    if nodo.dato == busqueda:
        # Devuelve el siguiente nodo, saltándose el nodo actual.
        return nodo.siguiente
        
    # Caso recursivo: Llama a eliminar en el resto de la lista.
    # El 'siguiente' del nodo actual se convierte en el resultado de la llamada recursiva.
    nodo.siguiente = eliminar_rec(nodo.siguiente, busqueda)
    return nodo

def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo

def obtener_cabeza(nodo_inicial):
    return nodo_inicial

def main():
    lista = None
    lista = agregar_al_final_rec(lista, "Luis")
    lista = agregar_al_final_rec(lista, "Leon")
    lista = agregar_al_inicio(lista, "Link")
    print("Antes de eliminar: ")
    imprimir_lista_rec(lista)
    
    lista = eliminar_rec(lista, "Link")
    print("\nDespués de eliminar 'Link': ")
    imprimir_lista_rec(lista)

    print("\nVerificaciones:")
    print(f"¿Existe 'Link'? {existe_rec(lista, 'Link')}")
    print(f"¿Existe 'Luis'? {existe_rec(lista, 'Luis')}")
    
    if lista is not None:
        print(f"Cabeza: {obtener_cabeza(lista).dato}")
        print(f"Cola: {obtener_cola_rec(lista).dato}")
    
main()