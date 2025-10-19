class Nodo: 
    def __init__(self, dato): 
        self.dato = dato 
        self.prev = None 
        self.next = None 
 
class ListaDoble: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
 
    def push_front(self, dato): 
        nuevo = Nodo(dato) 
        nuevo.next = self.head 
        if self.head: 
            self.head.prev = nuevo 
        else: 
            self.tail = nuevo  # estaba vacía 
        self.head = nuevo 
 
    def push_back(self, dato): 
        nuevo = Nodo(dato) 
        nuevo.prev = self.tail 
        if self.tail: 
            self.tail.next = nuevo 
        else: 
            self.head = nuevo  # estaba vacía 
        self.tail = nuevo 
 
    def remove_node(self, nodo): 
        if nodo is None: 
            return 
        if nodo.prev: 
            nodo.prev.next = nodo.next 
        else: 
            self.head = nodo.next  # borraste head 
        if nodo.next: 
            nodo.next.prev = nodo.prev 
        else: 
            self.tail = nodo.prev  # borraste tail 
        nodo.prev = nodo.next = None  # desconectar (opcional) 
 
    def find(self, dato): 
        cur = self.head 
        while cur: 
            if cur.dato == dato: 
                return cur 
            cur = cur.next 
        return None 
 
    def to_list_forward(self): 
        cur, out = self.head, [] 
        while cur: 
            out.append(cur.dato) 
            cur = cur.next 
        return out 
 
    def to_list_backward(self): 
        cur, out = self.tail, [] 
        while cur: 
            out.append(cur.dato) 
            cur = cur.prev 
        return out