# -------------------------
# CLASE DE NODO (Key-Value)
# -------------------------

class NodoKV:
    """Nodo especializado para la LRU, guarda llave (k) y valor (v)."""
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.prev = None
        self.next = None

# -------------------------
# CLASE LRU CACHE
# -------------------------

class LRU:
    """
    Implementación de LRU Cache usando un diccionario y una lista doble.
    """
    def __init__(self, cap: int):
        self.cap = cap
        self.map = {}  # Diccionario: key -> NodoKV
        
        # Nodos centinela (dummy nodes) para head y tail
        # Simplifican las operaciones _add_front y _remove
        self.head = NodoKV(0, 0) # Nodo centinela MRU
        self.tail = NodoKV(0, 0) # Nodo centinela LRU
        
        # Inicialización de la lista doble vacía entre los centinelas
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- HELPERS (Operaciones de la lista doble en O(1)) ---
    
    def _add_front(self, n: NodoKV):
        """Añade un nodo inmediatamente después del head (MRU)."""
        n.prev = self.head
        n.next = self.head.next
        self.head.next.prev = n
        self.head.next = n

    def _remove(self, n: NodoKV):
        """Desenlace un nodo de la lista."""
        n.prev.next = n.next
        n.next.prev = n.prev
        # Opcional: limpiar punteros del nodo
        n.prev = n.next = None

    def _move_to_front(self, n: NodoKV):
        """Mueve un nodo existente a la posición MRU."""
        self._remove(n)
        self._add_front(n)

    def _evict_lru(self):
        """Expulsa el nodo LRU (el que está justo antes del tail) si la capacidad se excede."""
        # El nodo LRU es el penúltimo nodo (self.tail.prev)
        lru_node = self.tail.prev
        
        # Verificar que no estemos intentando borrar el head centinela (solo pasa si la lista está vacía)
        if lru_node is self.head: 
            return # Lista vacía, nada que borrar

        self._remove(lru_node)
        # Eliminar también del mapa para liberar memoria
        del self.map[lru_node.k]
        
        print(f"  [EVICT]: Expulsado el LRU (key: {lru_node.k}, value: {lru_node.v}).")

    # --- API (Operaciones de la Cache en O(1)) ---

    def get(self, k: int) -> int:
        """Obtiene el valor de la clave. Si existe, lo mueve a MRU."""
        if k not in self.map:
            print(f"  [GET]: Key {k} no encontrada.")
            return -1
        
        n = self.map[k]
        # Actualizar uso: mover a la cabeza (MRU)
        self._move_to_front(n)
        print(f"  [GET]: Key {k} -> {n.v}. Movido a MRU.")
        return n.v

    def put(self, k: int, v: int):
        """Inserta o actualiza un valor. Si se inserta, verifica capacidad."""
        if k in self.map:
            # Caso 1: Actualizar (Hit)
            n = self.map[k]
            n.v = v
            self._move_to_front(n) # Mover a MRU
            print(f"  [PUT]: Key {k} actualizada a {v}. Movido a MRU.")
        else:
            # Caso 2: Insertar nuevo (Miss)
            n = NodoKV(k, v)
            self.map[k] = n
            self._add_front(n) # Añadir a MRU
            print(f"  [PUT]: Key {k} insertada con valor {v}.")
            
            # Verificar capacidad y expulsar si es necesario
            if len(self.map) > self.cap:
                self._evict_lru()
                
# -------------------------
# DEMOSTRACIÓN DE LA CACHE
# -------------------------

# Crear una caché con capacidad 2
cache = LRU(2)
print("--- Inicializando LRU Cache con capacidad 2 ---")

# 1. put(1, 10) -> {1:10} (MRU: 1)
cache.put(1, 10)    

# 2. put(2, 20) -> {1:10, 2:20} (MRU: 2)
cache.put(2, 20)    

print("\n--- Estado Actual: {1:10, 2:20} --- (LRU: 1)")

# 3. get(1) -> 10. Actualiza el uso. (MRU: 1)
print(f"Resultado get(1): {cache.get(1)}") 
# Nueva secuencia de uso: 1 (MRU), 2 (LRU)

# 4. put(3, 30). Capacidad excedida. Expulsa LRU (2).
cache.put(3, 30)    
# Nuevo estado: {1:10, 3:30} (LRU: 2 fue expulsado, LRU actual: 1)

# 5. get(2) -> -1. (Fue expulsado)
print(f"Resultado get(2): {cache.get(2)}") 

# 6. put(4, 40). Capacidad excedida. Expulsa LRU (1).
cache.put(4, 40)    
# Nuevo estado: {3:30, 4:40} (1 fue expulsado, LRU actual: 3)

print("\n--- Pruebas Finales ---")
print(f"Resultado get(1): {cache.get(1)}") # -1 (Expulsado)
print(f"Resultado get(3): {cache.get(3)}") # 30. Mueve 3 a MRU.
print(f"Resultado get(4): {cache.get(4)}") # 40. Mueve 4 a MRU.