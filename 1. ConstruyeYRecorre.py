# -------------------------
# CLASES DE LA LISTA DOBLE
# -------------------------

class Nodo:
    """Representa un nodo en la lista doblemente ligada."""
    def __init__(self, dato):
        self.dato = dato
        self.prev = None  # Puntero al nodo anterior
        self.next = None  # Puntero al nodo siguiente

class ListaDoble:
    """Implementa una lista doblemente ligada con inserción en extremos y recorridos."""
    def __init__(self):
        self.head = None  # Puntero a la cabeza (inicio de la lista)
        self.tail = None  # Puntero a la cola (final de la lista)

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

# -------------------------
# EJECUCIÓN DEL EJERCICIO 1
# -------------------------

# Crear una instancia de la lista doble
ld = ListaDoble()

# 1. Insertar 10, 20, 30 al final (push_back)
print("Paso 1: Insertando 10, 20, 30 al final.")
ld.push_back(10)
ld.push_back(20)
ld.push_back(30)
# Estado actual (adelante): [10, 20, 30]

# 2. Insertar 5 al inicio (push_front)
print("Paso 2: Insertando 5 al inicio.")
ld.push_front(5)
# Estado final (adelante): [5, 10, 20, 30]

# Mostrar los recorridos
print("\n--- Resultados de Recorrido ---")

# Recorrido hacia adelante (desde la cabeza)
print(f"Recorrido hacia adelante (forward): {ld.forward()}")

# Recorrido hacia atrás (desde la cola)
print(f"Recorrido hacia atrás (backward): {ld.backward()}")