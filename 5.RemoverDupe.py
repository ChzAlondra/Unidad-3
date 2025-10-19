# Reutilizamos las clases Nodo y ListaDoble, incluyendo el método remove_node.

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

    # Métodos push_front, push_back y forward (asumidos de los ejercicios anteriores)
    def push_back(self, x):
        n = Nodo(x)
        n.prev = self.tail
        if self.tail: self.tail.next = n
        else: self.head = n
        self.tail = n
    
    def remove_node(self, nodo):
        """
        Desenlace un nodo dado de la lista (O(1)).
        Asumido del Ejercicio 3.
        """
        if not nodo: return
        if nodo.prev: nodo.prev.next = nodo.next
        else: self.head = nodo.next
        if nodo.next: nodo.next.prev = nodo.prev
        else: self.tail = nodo.prev
        nodo.prev = nodo.next = None
        
    def forward(self):
        cur, out = self.head, []
        while cur: out.append(cur.dato); cur = cur.next
        return out

    # ----------------------------------------------------------------------
    # NUEVO MÉTODO: Remover duplicados (remove_dups) - Complejidad O(n)
    # ----------------------------------------------------------------------
    def remove_dups(self):
        """
        Elimina nodos duplicados en sitio, dejando la primera aparición.
        Usa un set para rastrear elementos vistos.
        """
        vistos = set() # O(n) espacio
        cur = self.head
        
        # Recorrido de la lista (O(n) tiempo)
        while cur:
            dato_actual = cur.dato
            
            if dato_actual in vistos:
                # Caso: Duplicado encontrado. Borramos el nodo actual.
                
                # Guardamos el nodo a borrar
                borrar = cur
                
                # Avanzamos 'cur' ANTES de borrar, para no perder el rastro
                cur = cur.next 
                
                # Borramos el nodo duplicado (O(1))
                self.remove_node(borrar)
                
            else:
                # Caso: Primera aparición. Agregamos el dato al set.
                vistos.add(dato_actual)
                
                # Avanzamos 'cur'
                cur = cur.next
        
        print(f"  [ÉXITO]: Duplicados eliminados. Vistos: {vistos}")

# Inicializar y poblar la lista con duplicados
ld = ListaDoble()
ld.push_back(10)
ld.push_back(20)
ld.push_back(10) # Duplicado de 10
ld.push_back(30)
ld.push_back(20) # Duplicado de 20
ld.push_back(40)
ld.push_back(50)
ld.push_back(30) # Duplicado de 30

print(f"Lista Inicial: {ld.forward()}")
print("-" * 40)

# Aplicar la eliminación de duplicados
ld.remove_dups()

# Mostrar el resultado
print(f"Lista Final (sin duplicados): {ld.forward()}")

# Prueba con una lista que no tiene duplicados
print("\n--- Prueba con lista sin duplicados ---")
ld2 = ListaDoble()
ld2.push_back(1)
ld2.push_back(2)
ld2.push_back(3)

print(f"Lista Inicial: {ld2.forward()}")
ld2.remove_dups()
print(f"Lista Final: {ld2.forward()}")

print("-" * 40)