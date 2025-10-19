import sys

# ==========================================================
# ESTRUCTURAS DE DATOS BASE (Ejercicios 1-5)
# ==========================================================

class Nodo:
    """Representa un nodo en la lista doblemente ligada."""
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDoble:
    """
    Implementa una lista doblemente ligada con métodos de los Ejercicios 1 al 5.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    # --- EJERCICIO 1: CONSTRUYE Y RECORRE ---
    def push_front(self, x):
        n = Nodo(x)
        n.next = self.head
        if self.head: self.head.prev = n
        else: self.tail = n
        self.head = n
        print(f"  [INFO]: Insertado {x} al inicio.")

    def push_back(self, x):
        n = Nodo(x)
        n.prev = self.tail
        if self.tail: self.tail.next = n
        else: self.head = n
        self.tail = n
        print(f"  [INFO]: Insertado {x} al final.")

    def forward(self):
        cur, out = self.head, []
        while cur: out.append(cur.dato); cur = cur.next
        return out

    def backward(self):
        cur, out = self.tail, []
        while cur: out.append(cur.dato); cur = cur.prev
        return out

    # --- EJERCICIO 2 Y 3: HELPER ---
    def find(self, v):
        """Busca y retorna el primer nodo con valor v."""
        cur = self.head
        while cur:
            if cur.dato == v: return cur
            cur = cur.next
        return None

    def remove_node(self, nodo):
        """Desenlace un nodo dado de la lista."""
        if not nodo: return
        if nodo.prev: nodo.prev.next = nodo.next
        else: self.head = nodo.next
        if nodo.next: nodo.next.prev = nodo.prev
        else: self.tail = nodo.prev
        nodo.prev = nodo.next = None

    # --- EJERCICIO 2: INSERTAR DESPUÉS ---
    def insert_after(self, objetivo, x):
        nodo_objetivo = self.find(objetivo)
        if not nodo_objetivo: 
            print(f"  [AVISO]: Objetivo {objetivo} no encontrado. No se insertó {x}.")
            return
        
        n = Nodo(x)
        n.prev = nodo_objetivo
        n.next = nodo_objetivo.next
        
        if nodo_objetivo.next: nodo_objetivo.next.prev = n
        else: self.tail = n
            
        nodo_objetivo.next = n
        print(f"  [INFO]: Insertado {x} después de {objetivo}.")

    # --- EJERCICIO 3: ELIMINAR PRIMERA OCURRENCIA ---
    def remove_value(self, v):
        nodo_a_eliminar = self.find(v)
        if nodo_a_eliminar:
            self.remove_node(nodo_a_eliminar)
            print(f"  [INFO]: Eliminada la primera ocurrencia de {v}.")
        else:
            print(f"  [AVISO]: El valor {v} no se encontró en la lista.")

    # --- EJERCICIO 4: CONTAR Y K-ÉSIMO ---
    def __len__(self):
        cur, count = self.head, 0
        while cur: count += 1; cur = cur.next
        return count
    
    def k_from_end(self, k):
        if k <= 0:
            print(f"  [ERROR]: k debe ser positivo.")
            return None
            
        cur = self.tail
        i = 1 
        while cur and i < k:
            cur = cur.prev
            i += 1
            
        if cur and i == k:
            return cur.dato
        else:
            return None

    # --- EJERCICIO 5: REMOVER DUPLICADOS ---
    def remove_dups(self):
        vistos = set()
        cur = self.head
        while cur:
            if cur.dato in vistos:
                borrar = cur
                cur = cur.next 
                self.remove_node(borrar)
            else:
                vistos.add(cur.dato)
                cur = cur.next
        print(f"  [INFO]: Proceso de eliminación de duplicados finalizado.")

# ==========================================================
# ESTRUCTURA DE DATOS EXTRA (Ejercicio 6)
# ==========================================================

class NodoKV:
    """Nodo especializado para la LRU Cache."""
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.prev = None
        self.next = None

class LRU:
    """Implementación de LRU Cache (O(1) amortizado)."""
    def __init__(self, cap: int):
        self.cap = cap
        self.map = {}
        self.head = NodoKV(0, 0)
        self.tail = NodoKV(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front(self, n: NodoKV):
        n.prev = self.head
        n.next = self.head.next
        self.head.next.prev = n
        self.head.next = n

    def _remove(self, n: NodoKV):
        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = n.next = None

    def _move_to_front(self, n: NodoKV):
        self._remove(n)
        self._add_front(n)

    def _evict_lru(self):
        lru_node = self.tail.prev
        if lru_node is self.head: return
        self._remove(lru_node)
        del self.map[lru_node.k]
        print(f"  [EVICT]: Expulsado el LRU (key: {lru_node.k}).")

    def get(self, k: int) -> int:
        if k not in self.map: return -1
        n = self.map[k]
        self._move_to_front(n)
        return n.v

    def put(self, k: int, v: int):
        if k in self.map:
            n = self.map[k]
            n.v = v
            self._move_to_front(n)
        else:
            n = NodoKV(k, v)
            self.map[k] = n
            self._add_front(n)
            if len(self.map) > self.cap:
                self._evict_lru()

# ==========================================================
# FUNCIONES DE MENÚ
# ==========================================================

def get_int_input(prompt):
    """Obtiene una entrada entera válida del usuario."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  [ERROR]: Entrada inválida. Por favor, ingrese un número entero.")

def display_list_status(ld):
    """Muestra el estado actual de la lista."""
    print("\n--- ESTADO DE LA LISTA ---")
    print(f"  Recorrido adelante: {ld.forward()}")
    print(f"  Recorrido atrás:   {ld.backward()}")
    print(f"  Tamaño (len()):    {len(ld)}")
    print("--------------------------\n")

# --------------------------------------------------------------------------------------------------
# MENÚ PARA LA LISTA DOBLE (Ejercicios 1 al 5)
# --------------------------------------------------------------------------------------------------

def menu_lista_doble(ld):
    """Menú interactivo para la Lista Doble."""
    while True:
        print("\n\n--- MENÚ DE LISTA DOBLE (EJERCICIOS 1-5) ---")
        print("1. Insertar al inicio (push_front)")
        print("2. Insertar al final (push_back)")
        print("3. Recorrer (Mostrar status)")
        print("4. Insertar después de un valor (insert_after) [E2]")
        print("5. Eliminar por valor (remove_value) [E3]")
        print("6. Obtener k-ésimo desde el final (k_from_end) [E4]")
        print("7. Remover duplicados (remove_dups) [E5]")
        print("0. Volver al Menú Principal")
        
        choice = input("Seleccione una opción: ")

        if choice == '1':
            dato = get_int_input("  Ingrese el dato a insertar al inicio: ")
            ld.push_front(dato)
        elif choice == '2':
            dato = get_int_input("  Ingrese el dato a insertar al final: ")
            ld.push_back(dato)
        elif choice == '3':
            display_list_status(ld)
        elif choice == '4':
            objetivo = get_int_input("  Ingrese el valor objetivo (después de cuál insertar): ")
            nuevo = get_int_input("  Ingrese el valor a insertar: ")
            ld.insert_after(objetivo, nuevo)
        elif choice == '5':
            valor = get_int_input("  Ingrese el valor a eliminar (primera ocurrencia): ")
            ld.remove_value(valor)
        elif choice == '6':
            k = get_int_input("  Ingrese el valor de k (1 es el último): ")
            resultado = ld.k_from_end(k)
            if resultado is not None:
                print(f"  [RESULTADO]: El {k}-ésimo desde el final es: {resultado}")
            else:
                 print(f"  [RESULTADO]: No se encontró el {k}-ésimo (k={k} es demasiado grande o inválido).")
        elif choice == '7':
            ld.remove_dups()
        elif choice == '0':
            break
        else:
            print("  [ERROR]: Opción no válida. Intente de nuevo.")

# --------------------------------------------------------------------------------------------------
# MENÚ PARA LRU CACHE (Ejercicio 6)
# --------------------------------------------------------------------------------------------------

def menu_lru_cache():
    """Menú interactivo para la LRU Cache."""
    
    capacidad = get_int_input("  Ingrese la capacidad máxima de la LRU Cache: ")
    if capacidad <= 0:
        print("  [ERROR]: La capacidad debe ser un número positivo.")
        return
        
    cache = LRU(capacidad)
    print(f"\n--- LRU Cache inicializada con capacidad: {capacidad} ---")

    while True:
        print("\n\n--- MENÚ LRU CACHE (EJERCICIO 6) ---")
        print(f"Capacidad: {cache.cap} | Elementos: {len(cache.map)}")
        print("1. get(key)")
        print("2. put(key, value)")
        print("3. Mostrar contenido (mapa interno)")
        print("0. Volver al Menú Principal")
        
        choice = input("Seleccione una opción: ")

        if choice == '1':
            key = get_int_input("  Ingrese la clave (key) a buscar: ")
            value = cache.get(key)
            if value != -1:
                print(f"  [RESULTADO]: Clave {key} encontrada, valor: {value}. (Movido a MRU).")
            else:
                print(f"  [RESULTADO]: Clave {key} no encontrada (-1).")
        elif choice == '2':
            key = get_int_input("  Ingrese la clave (key): ")
            value = get_int_input("  Ingrese el valor (value): ")
            cache.put(key, value)
            print(f"  [INFO]: put({key}, {value}) ejecutado. Verifique expulsiones.")
        elif choice == '3':
            # Muestra el mapa interno (desordenado, el orden LRU/MRU está en la lista doble)
            print(f"  Mapa interno: {cache.map}") 
            # Recorrido de la lista (MRU a LRU)
            current = cache.head.next
            order = []
            while current is not cache.tail:
                order.append(f"({current.k}: {current.v})")
                current = current.next
            print(f"  Orden de uso (MRU -> LRU): {' -> '.join(order) if order else '[Vacío]'} ")

        elif choice == '0':
            break
        else:
            print("  [ERROR]: Opción no válida. Intente de nuevo.")

# --------------------------------------------------------------------------------------------------
# MENÚ PRINCIPAL
# --------------------------------------------------------------------------------------------------

def main_menu():
    """Menú principal para seleccionar el ejercicio."""
    lista_doble_instancia = ListaDoble()
    
    while True:
        print("\n===========================================")
        print("      MENÚ PRINCIPAL DE EJERCICIOS (LISTAS DOBLES)")
        print("===========================================")
        print("1. [EJERCICIOS 1-5]: Lista Doblemente Ligada")
        print("2. [EJERCICIO 6]: LRU Cache")
        print("0. Salir")
        
        main_choice = input("Seleccione una opción (0-2): ")

        if main_choice == '1':
            menu_lista_doble(lista_doble_instancia)
        elif main_choice == '2':
            menu_lru_cache()
        elif main_choice == '0':
            print("Saliendo del programa. ¡Adiós! 👋")
            sys.exit()
        else:
            print("  [ERROR]: Opción no válida. Intente de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    main_menu()