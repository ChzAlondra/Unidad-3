class Nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def agregar_al_final_rec(nodo_actual, dato):
    if nodo_actual is None:
        return Nodo(dato)
    
    if nodo_actual.siguiente is not None:
        nodo_actual.siguiente = agregar_al_final_rec(nodo_actual.siguiente, dato)
    else:
        nodo_actual.siguiente = Nodo(dato)
        
    return nodo_actual

def imprimir_lista_rec(nodo):
    if nodo is not None:
        print(f"Tenemos {nodo.dato}")
        imprimir_lista_rec(nodo.siguiente)

def obtener_cola_rec(nodo):
    if nodo is None or nodo.siguiente is None:
        return nodo
    
    return obtener_cola_rec(nodo.siguiente)

def existe_rec(nodo, busqueda):
    if nodo is None:
        return False
    
    if nodo.dato == busqueda:
        return True
    
    return existe_rec(nodo.siguiente, busqueda)

def eliminar_rec(nodo, busqueda):
    if nodo is None:
        return None
        
    if nodo.dato == busqueda:
        return nodo.siguiente

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
        
    print("--- 1. Creando la lista (1 al 9 al final, 10 al inicio) ---")
    for i in range(1, 10):
        lista = agregar_al_final_rec(lista, i)
    
    lista = agregar_al_inicio(lista, 10)
    
    print("\nLista inicial (10 números):")
    imprimir_lista_rec(lista)
    
    NUM_A_ELIMINAR_MEDIO = 5
    lista = eliminar_rec(lista, NUM_A_ELIMINAR_MEDIO)
    print(f"\n--- 2.a. Después de eliminar el {NUM_A_ELIMINAR_MEDIO} (en medio) ---")
    imprimir_lista_rec(lista)
    
    NUM_A_ELIMINAR_CABEZA = 10
    lista = eliminar_rec(lista, NUM_A_ELIMINAR_CABEZA)
    print(f"\n--- 2.b. Después de eliminar el {NUM_A_ELIMINAR_CABEZA} (cabeza) ---")
    imprimir_lista_rec(lista)
    
    NUM_A_ELIMINAR_COLA = 9
    lista = eliminar_rec(lista, NUM_A_ELIMINAR_COLA)
    print(f"\n--- 2.c. Después de eliminar el {NUM_A_ELIMINAR_COLA} (cola) ---")
    imprimir_lista_rec(lista)

    print("\n--- 3. Verificaciones de la lista ---")
    
    print(f"¿Existe el número 5? {existe_rec(lista, 5)}")
    print(f"¿Existe el número 6? {existe_rec(lista, 6)}")
    
    if lista is not None:
        print(f"Cabeza (Recursivo): {obtener_cabeza(lista).dato}") 
        print(f"Cola (Recursivo): {obtener_cola_rec(lista).dato}") 
    
main()