class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None
        self.anterior = None

class doubleList:
    def __init__(self):
        self.root = None

def insertar_lista_vacia(self,dato):
    if self.root is None:
        nuevoNodo = Nodo(dato)
        self.root = nuevoNodo
    else:
        print("La lista no esta vacia")

def insertar_inicio(self,dato):
    if self.root is None:
        self.insertar_lista_vacia(dato)
        return
    else:
        nuevoNodo = Nodo(dato)
        nuevoNodo.siguiente = self.root
        self.root.anterior = nuevoNodo
        self.root = nuevoNodo

def insertar_final(self,dato):
    if self.root is None:
        nuevoNodo = Nodo(dato)
        self.root = nuevoNodo
        return
    apuntador = self.root
    while apuntador.siguiente is not None:
        apuntador = apuntador.siguiente
    nuevoNodo = Nodo(dato)
    apuntador.siguiente = nuevoNodo
    nuevoNodo.anterior = apuntador

def insertar_despues_elemento(self,x,dato):
    if self.root is None:
        print("La lista esta vacia")
    else:
        apuntador = self.root
        while apuntador is not None:
            if apuntador.elemento == x:
                break
            apuntador = apuntador.siguiente
        if apuntador is None:
            print("El elemento no se encuentra en la lista")
        else:
            nuevoNodo = Nodo(dato)
            nuevoNodo.anterior = apuntador
            nuevoNodo.siguiente = apuntador.siguiente
            if apuntador.siguiente is not None:
                apuntador.siguiente.anterior = nuevoNodo
            apuntador.siguiente = nuevoNodo

def insertar_antes_elemento(self,x,dato):
    if self.root is None:
        print("La lista esta vacia")
    else:
        apuntador = self.root
        while apuntador is not None:
            if apuntador.elemento == x:
                break
            apuntador = apuntador.siguiente
        if apuntador is None:
            print("El elemento no se encuentra en la lista")
        else:
            nuevoNodo = Nodo(dato)
            nuevoNodo.siguiente = apuntador
            nuevoNodo.anterior = apuntador.anterior
            if apuntador.anterior is not None:
                apuntador.anterior.siguiente = nuevoNodo
            apuntador.anterior = nuevoNodo

def navegar_lista(self):
    if self.root is None:
        print("La lista esta vacia")
        return
    else:
        apuntador = self.root
        while apuntador is not None:
            print(apuntador.elemento, "")
            apuntador = apuntador.siguiente

def lista_vacia(self):
    if self.root is None:
        return True
    else:
        return False
    
def contar_elementos(self):
    apuntador = self.root
    cuenta = 0
    while apuntador is not None:
        cuenta = cuenta + 1
        apuntador = apuntador.siguiente
    return cuenta

def eliminar_inicio(self):
    if self.root is None:
        print("La lista no contiene Nodos para eliminar")
        return
    if self.root.siguiente is None:
        self.root = None
    self.root = self.root.siguiente
    self.root.anterior = None

def eliminar_final(self):
    if self.root is None:
        print("La lista no contiene Nodos para eliminar")
        return
    if self.root.siguiente is None:
        self.root = None
        return
    apuntador = self.root
    while apuntador.siguiente is not None:
        apuntador = apuntador.siguiente
    apuntador.anterior.siguiente = None

def eliminar_elemento(self,x):
    if self.root is None:
        print("La lista esta vacia")
        return
    if self.root.siguiente is None:
        if self.root.elemento == x:
            self.root = None
        else:
            print("Elemento no encontrado")
    if self.root.elemento == x:
        self.eliminar_inicio()
        return
    apuntador = self.root
    while apuntador.siguiente is not None:
        if apuntador.elemento == x:
            break
        apuntador = apuntador.siguiente
    if apuntador.siguiente is not None:
        apuntador.anterior.siguiente = apuntador.siguiente
        apuntador.siguiente.anterior = apuntador.anterior
    else:
        if apuntador.elemento == x:
            self.eliminar_final()
        else:
            return print("Elemento no encontrado")