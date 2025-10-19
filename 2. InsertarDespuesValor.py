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

    # Recorrido hacia adelante (forward)
    # Complejidad: O(n)
    def forward(self):
        cur, out = self.head, []
        while cur: 
            out.append(cur.dato)
            cur = cur.next
        return out

    # Recorrido hacia atrás (backward)
    # Complejidad: O(n)
    def backward(self):
        cur, out = self.tail, []
        while cur: 
            out.append(cur.dato)
            cur = cur.prev
        return out
    
    # ----------------------------------------------------
    # NUEVO MÉTODO 1: Búsqueda (find) - Complejidad O(n)
    # ----------------------------------------------------
    def find(self, v):
        """Busca y retorna la PRIMERA ocurrencia de un valor (v) en la lista."""
        cur = self.head
        while cur:
            if cur.dato == v: 
                return cur # Se encontró el nodo
            cur = cur.next
        return None # El valor no se encontró

    # ------------------------------------------------------------------------
    # NUEVO MÉTODO 2: Insertar después (insert_after) - Complejidad O(n) total
    # ------------------------------------------------------------------------
    def insert_after(self, valor_objetivo, x):
        """
        Inserta un nuevo nodo (x) después de la primera ocurrencia de valor_objetivo.
        """
        # 1. Búsqueda (O(n)): encontrar el nodo objetivo
        nodo_objetivo = self.find(valor_objetivo)
        
        # Si no existe el nodo objetivo, terminamos
        if not nodo_objetivo: 
            print(f"  [AVISO]: El valor objetivo ({valor_objetivo}) no se encontró. No se insertó {x}.")
            return
        
        # 2. Inserción/Enlace (O(1)): crear y enlazar el nuevo nodo
        n = Nodo(x)
        
        # Configurar los punteros del nuevo nodo
        n.prev = nodo_objetivo      # 'prev' apunta al objetivo
        n.next = nodo_objetivo.next # 'next' apunta al sucesor del objetivo
        
        # Manejar el puntero 'prev' del sucesor
        if nodo_objetivo.next: 
            # Si el nodo objetivo NO es el final (tail)
            nodo_objetivo.next.prev = n
        else: 
            # Si el nodo objetivo ES el final (tail), el nuevo nodo se convierte en la nueva 'tail'
            self.tail = n
            
        # Actualizar el puntero 'next' del nodo objetivo para apuntar al nuevo nodo
        nodo_objetivo.next = n
        
        print(f"  [ÉXITO]: Insertado {x} después de {valor_objetivo}.")
        # Complejidad: O(n) por la búsqueda (find) + O(1) por el enlace.
        
    # Agregamos el forward del ejercicio anterior para las pruebas
    def forward(self):
        cur, out = self.head, []
        while cur: 
            out.append(cur.dato)
            cur = cur.next
        return out
    
# Inicializar y poblar la lista (como en el Ejercicio 1)
ld = ListaDoble()
ld.push_back(10)
ld.push_back(20)
ld.push_back(30)
ld.push_front(5)

print(f"Lista Inicial: {ld.forward()}")
print("-" * 30)

# --------------------------------------------------
# PRUEBA 1: Insertar en medio de la lista (10, 15)
# Esperado: [5, 10, 15, 20, 30]
# --------------------------------------------------
ld.insert_after(10, 15)
print(f"Lista después de insert_after(10, 15): {ld.forward()}")

# -----------------------------------------------------
# PRUEBA 2: Insertar después del último elemento (30, 40)
# Esperado: [5, 10, 15, 20, 30, 40] (40 debe ser la nueva tail)
# -----------------------------------------------------
ld.insert_after(30, 40)
print(f"Lista después de insert_after(30, 40): {ld.forward()}")

# --------------------------------------------------
# PRUEBA 3: Insertar un valor inexistente (99, 100)
# Esperado: No hay cambios
# --------------------------------------------------
ld.insert_after(99, 100)
print(f"Lista después de insert_after(99, 100): {ld.forward()}")

print("-" * 30)