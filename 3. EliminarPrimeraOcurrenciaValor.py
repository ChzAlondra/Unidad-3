# Reutilizamos las clases Nodo y ListaDoble, incluyendo el método find.

class Nodo:
    """Representa un nodo en la lista doblemente ligada."""
    def __init__(self, dato):
        self.dato = dato
        self.prev = None  
        self.next = None  

class ListaDoble:
    """Implementa una lista doblemente ligada."""
    def __init__(self):
        self.head = None  
        self.tail = None  

    # Inserción al inicio (push_front)
    # Complejidad: O(1)
    def push_front(self, x):
        n = Nodo(x)
        n.next = self.head  
        
        if self.head: 
            self.head.prev = n
        else: 
            # Si la lista estaba vacía, el nuevo nodo es también la cola
            self.tail = n
            
        self.head = n 

    # Inserción al final (push_back)
    # Complejidad: O(1)
    def push_back(self, x):
        n = Nodo(x)
        n.prev = self.tail  
        
        if self.tail: 
            self.tail.next = n
        else: 
            # Si la lista estaba vacía, el nuevo nodo es también la cabeza
            self.head = n
            
        self.tail = n 

    # Método find (asumido del Ejercicio 2)
    def find(self, v):
        cur = self.head
        while cur:
            if cur.dato == v: return cur
            cur = cur.next
        return None
    
    # Métodos push_front, push_back y forward (asumidos de los ejercicios anteriores)
    # ...

    # ----------------------------------------------------
    # NUEVO MÉTODO 1: Desenlazar un nodo (remove_node) - Complejidad O(1)
    # ----------------------------------------------------
    def remove_node(self, nodo):
        """
        Desenlace un nodo dado de la lista. Maneja los casos borde de head y tail.
        """
        # Si el nodo es None (no existe), simplemente retorna
        if not nodo: 
            return

        # 1. Ajustar el puntero 'next' del nodo PREVIO
        if nodo.prev: 
            # Si NO es la cabeza, el nodo previo apunta al sucesor del nodo a eliminar
            nodo.prev.next = nodo.next
        else: 
            # Si ES la cabeza, la 'head' se mueve al sucesor (puede ser None si solo había 1 nodo)
            self.head = nodo.next

        # 2. Ajustar el puntero 'prev' del nodo SUCESOR
        if nodo.next: 
            # Si NO es la cola, el nodo sucesor apunta al predecesor del nodo a eliminar
            nodo.next.prev = nodo.prev
        else: 
            # Si ES la cola, la 'tail' se mueve al predecesor (puede ser None si solo había 1 nodo)
            self.tail = nodo.prev
            
        # Opcional: Limpiar los punteros del nodo eliminado para liberarlo de la lista
        nodo.prev = nodo.next = None
        
        # Este método opera en O(1) ya que solo ajusta punteros.

    # -------------------------------------------------------------------------
    # NUEVO MÉTODO 2: Eliminar por valor (remove_value) - Complejidad O(n) total
    # -------------------------------------------------------------------------
    def remove_value(self, v):
        """
        Busca y elimina la primera ocurrencia del valor 'v' de la lista.
        """
        # 1. Búsqueda (O(n)): encontrar el nodo objetivo
        nodo_a_eliminar = self.find(v)
        
        # 2. Eliminación (O(1)): desenlazar el nodo (si existe)
        self.remove_node(nodo_a_eliminar)
        
        if nodo_a_eliminar:
            print(f"  [ÉXITO]: Eliminada la primera ocurrencia de {v}.")
        else:
            print(f"  [AVISO]: El valor {v} no se encontró en la lista.")
            
    # Agregamos el forward del ejercicio anterior para las pruebas
    def forward(self):
        cur, out = self.head, []
        while cur: 
            out.append(cur.dato)
            cur = cur.next
        return out
    
    # Agregamos un helper para las pruebas
    def is_empty(self):
        return self.head is None and self.tail is None
    
# Inicializar y poblar la lista
ld = ListaDoble()
ld.push_front(5)   # [5]
ld.push_back(10)   # [5, 10]
ld.push_back(15)   # [5, 10, 15]
ld.push_back(20)   # [5, 10, 15, 20]
ld.push_back(30)   # [5, 10, 15, 20, 30]

print(f"Lista Inicial: {ld.forward()}")
print("-" * 40)

# --------------------------------------------------
# PRUEBA 1: Eliminar un nodo en el medio (15)
# Esperado: [5, 10, 20, 30]
# --------------------------------------------------
ld.remove_value(15)
print(f"Lista después de eliminar (15): {ld.forward()}")

# --------------------------------------------------
# PRUEBA 2: Eliminar la HEAD (5)
# Esperado: [10, 20, 30] (10 debe ser la nueva head)
# --------------------------------------------------
ld.remove_value(5)
print(f"Lista después de eliminar la HEAD (5): {ld.forward()}")

# --------------------------------------------------
# PRUEBA 3: Eliminar la TAIL (30)
# Esperado: [10, 20] (20 debe ser la nueva tail)
# --------------------------------------------------
ld.remove_value(30)
print(f"Lista después de eliminar la TAIL (30): {ld.forward()}")

# --------------------------------------------------
# PRUEBA 4: Eliminar un valor inexistente (100)
# Esperado: No hay cambios
# --------------------------------------------------
ld.remove_value(100)
print(f"Lista después de eliminar (100): {ld.forward()}")

# --------------------------------------------------
# PRUEBA 5: Eliminar hasta vaciar la lista (20, luego 10)
# Esperado: []
# --------------------------------------------------
print("-" * 40)
ld.remove_value(20) # Queda [10]
ld.remove_value(10) # Queda []

print(f"Lista después de vaciarla: {ld.forward()} (¿Vacía? {'Sí' if ld.is_empty() else 'No'})")
print("-" * 40)