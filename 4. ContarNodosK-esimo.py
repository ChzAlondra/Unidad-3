# Reutilizar las implementaciones de Nodo y ListaDoble con los métodos de inserción.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Métodos de inserción
    def push_front(self, x):
        n = Nodo(x)
        n.next = self.head
        if self.head: self.head.prev = n
        else: self.tail = n
        self.head = n
    def push_back(self, x):
        n = Nodo(x)
        n.prev = self.tail
        if self.tail: self.tail.next = n
        else: self.head = n
        self.tail = n
    def forward(self):
        cur, out = self.head, []
        while cur: out.append(cur.dato); cur = cur.next
        return out
    
    # Métodos a probar
    def __len__(self):
        cur, count = self.head, 0
        while cur: count += 1; cur = cur.next
        return count
    
    def k_from_end(self, k):
        if k <= 0:
            print(f"  [ERROR]: k debe ser un valor positivo.")
            return None
            
        cur = self.tail
        i = 1 
        while cur and i < k:
            cur = cur.prev
            i += 1
            
        if cur and i == k:
            print(f"  [ÉXITO]: El {k}-ésimo desde el final es {cur.dato}.")
            return cur.dato
        else:
            print(f"  [AVISO]: La posición k={k} excede el tamaño de la lista ({len(self)}).")
            return None


# Inicializar y poblar la lista
ld = ListaDoble()
ld.push_front(5)
ld.push_back(10)
ld.push_back(15)
ld.push_back(20)
ld.push_back(30) # tail

print(f"Lista: {ld.forward()}")
print("-" * 50)

# --------------------------------------------------
# PRUEBA (a): Contar nodos con len()
# Esperado: 5
# --------------------------------------------------
largo = len(ld)
print(f"(a) El tamaño de la lista (len()): {largo}")

# --------------------------------------------------
# PRUEBA (b) - Caso 1: k=1 (el último)
# Esperado: 30
# --------------------------------------------------
ld.k_from_end(1) 

# --------------------------------------------------
# PRUEBA (b) - Caso 2: k=3 (el del medio)
# Esperado: 15
# --------------------------------------------------
ld.k_from_end(3)

# --------------------------------------------------
# PRUEBA (b) - Caso 3: k=5 (el primero)
# Esperado: 5
# --------------------------------------------------
ld.k_from_end(5) 

# --------------------------------------------------
# PRUEBA (b) - Caso 4: k > n
# Esperado: Aviso/None
# --------------------------------------------------
ld.k_from_end(6) 

print("-" * 50)