"""
Módulo para gestionar una lista enlazada de alumnos.

Este programa implementa una lista enlazada simple donde cada nodo contiene
un objeto de tipo Alumno (con nombre y calificación). Permite realizar
operaciones como agregar, buscar, eliminar, y obtener extremos de la lista.
"""

class Nodo:
    """
    Representa un nodo en una lista enlazada simple.

    Atributos:
        dato (Alumno): El objeto Alumno almacenado en este nodo.
        siguiente (Nodo): Referencia al siguiente nodo en la lista, o None si es el último.
    """
    dato = None
    siguiente = None

    def __init__(self, dato):
        """
        Inicializa un nuevo nodo con el dato proporcionado.

        Args:
            dato (Alumno): El objeto que se almacenará en el nodo.
        """
        self.dato = dato
        self.siguiente = None

def agregar_al_inicio(nodo_inicial, dato):
    """
    Agrega un nuevo nodo al inicio de la lista enlazada.

    Args:
        nodo_inicial (Nodo or None): La cabeza actual de la lista (puede ser None si la lista está vacía).
        dato (Alumno): El objeto Alumno que se desea insertar al inicio.

    Returns:
        Nodo: El nuevo nodo, que ahora es la cabeza de la lista.
    """
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo


def agregar_al_final(nodo_inicial, dato):
    """
    Agrega un nuevo nodo al final de la lista enlazada.

    Args:
        nodo_inicial (Nodo or None): La cabeza actual de la lista (puede ser None si está vacía).
        dato (Alumno): El objeto Alumno a agregar al final.

    Returns:
        Nodo: La nueva cabeza de la lista (puede ser el mismo nodo_inicial o el nuevo nodo si la lista estaba vacía).
    """
    nuevo_nodo = Nodo(dato)
    # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
    if nodo_inicial is None:
        return nuevo_nodo
    # Recorremos hasta el último nodo
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    # Enlazamos el último nodo con el nuevo
    temporal.siguiente = nuevo_nodo
    return nodo_inicial


def imprimir_lista(nodo):
    """
    Imprime todos los alumnos en la lista enlazada.

    Args:
        nodo (Nodo or None): La cabeza de la lista a imprimir.
    """
    if nodo is None:
        print("La lista está vacía.")
        return
    while nodo is not None:
        print(f"Alumno: {nodo.dato}")
        nodo = nodo.siguiente


def obtener_cabeza(nodo_inicial):
    """
    Devuelve el primer nodo de la lista (la cabeza).

    Args:
        nodo_inicial (Nodo or None): La cabeza actual de la lista.

    Returns:
        Nodo or None: El primer nodo, o None si la lista está vacía.
    """
    return nodo_inicial


def obtener_cola(nodo_inicial):
    """
    Devuelve el último nodo de la lista (la cola).

    Args:
        nodo_inicial (Nodo or None): La cabeza de la lista.

    Returns:
        Nodo or None: El último nodo, o None si la lista está vacía.
    """
    if nodo_inicial is None:
        return None
    temporal = nodo_inicial
    # Avanzamos hasta que no haya siguiente nodo
    while temporal.siguiente:
        temporal = temporal.siguiente
    return temporal


def buscar_por_nombre(nodo_inicial, nombre):
    """
    Busca un alumno por su nombre y devuelve el primero que coincida.

    Args:
        nodo_inicial (Nodo or None): La cabeza de la lista.
        nombre (str): El nombre del alumno a buscar.

    Returns:
        Alumno or None: El objeto Alumno encontrado, o None si no existe.
    """
    temporal = nodo_inicial
    while temporal is not None:
        if temporal.dato.nombre == nombre:
            return temporal.dato
        temporal = temporal.siguiente
    return None


def buscar_por_calificacion(nodo_inicial, calificacion):
    """
    Busca todos los alumnos que tengan una calificación específica.

    Args:
        nodo_inicial (Nodo or None): La cabeza de la lista.
        calificacion (float or int): La calificación a buscar.

    Returns:
        list[Alumno]: Lista de objetos Alumno que coinciden con la calificación.
                      Puede estar vacía si no se encuentra ninguno.
    """
    resultados = []
    temporal = nodo_inicial
    while temporal is not None:
        if temporal.dato.calificacion == calificacion:
            resultados.append(temporal.dato)
        temporal = temporal.siguiente
    return resultados


def eliminar_por_nombre(nodo_inicial, nombre):
    """
    Elimina el primer alumno cuyo nombre coincida con el dado.

    Args:
        nodo_inicial (Nodo or None): La cabeza actual de la lista.
        nombre (str): El nombre del alumno a eliminar.

    Returns:
        Nodo or None: La nueva cabeza de la lista después de la eliminación.
    """
    # Caso: lista vacía
    if nodo_inicial is None:
        return None
    # Caso: el primer nodo es el que queremos eliminar
    if nodo_inicial.dato.nombre == nombre:
        return nodo_inicial.siguiente
    # Caso: el nodo a eliminar está en medio o al final
    temporal = nodo_inicial
    while temporal.siguiente is not None:
        if temporal.siguiente.dato.nombre == nombre:
            # Saltamos el nodo a eliminar
            temporal.siguiente = temporal.siguiente.siguiente
            return nodo_inicial
        temporal = temporal.siguiente
    # Si no se encontró, devolvemos la lista sin cambios
    return nodo_inicial


def eliminar_por_calificacion(nodo_inicial, calificacion):
    """
    Elimina todos los alumnos que tengan la calificación especificada.

    Args:
        nodo_inicial (Nodo or None): La cabeza actual de la lista.
        calificacion (float or int): La calificación de los alumnos a eliminar.

    Returns:
        Nodo or None: La nueva cabeza de la lista tras las eliminaciones.
    """
    # Eliminar nodos del inicio que coincidan
    while nodo_inicial is not None and nodo_inicial.dato.calificacion == calificacion:
        nodo_inicial = nodo_inicial.siguiente

    # Si la lista quedó vacía, retornamos None
    if nodo_inicial is None:
        return None

    # Recorremos el resto de la lista
    temporal = nodo_inicial
    while temporal.siguiente is not None:
        if temporal.siguiente.dato.calificacion == calificacion:
            # Eliminamos el nodo siguiente
            temporal.siguiente = temporal.siguiente.siguiente
            # No avanzamos temporal aquí porque el nuevo siguiente también podría coincidir
        else:
            # Solo avanzamos si no eliminamos
            temporal = temporal.siguiente

    return nodo_inicial


class Alumno:
    """
    Representa a un alumno con nombre y calificación.

    Atributos:
        nombre (str): Nombre del alumno.
        calificacion (float or int): Calificación numérica del alumno.
    """
    def __init__(self, nombre, calificacion):
        """
        Inicializa un nuevo alumno.

        Args:
            nombre (str): Nombre del alumno.
            calificacion (float or int): Calificación del alumno.
        """
        self.nombre = nombre
        self.calificacion = calificacion

    def __str__(self):
        """
        Representación en cadena del alumno.

        Returns:
            str: Cadena legible con nombre y calificación.
        """
        return f"{self.nombre} (Calificación: {self.calificacion})"


def mostrar_menu():
    """
    Muestra el menú de opciones disponibles al usuario.
    """
    print("\n" + "="*50)
    print("           MENÚ DE GESTIÓN DE ALUMNOS")
    print("="*50)
    print("1. Agregar alumno al INICIO")
    print("2. Agregar alumno al FINAL")
    print("3. Buscar alumno por NOMBRE")
    print("4. Buscar alumnos por CALIFICACIÓN")
    print("5. Eliminar alumno por NOMBRE")
    print("6. Eliminar alumnos por CALIFICACIÓN")
    print("7. Mostrar PRIMER alumno")
    print("8. Mostrar ÚLTIMO alumno")
    print("9. Mostrar TODOS los alumnos")
    print("0. SALIR")
    print("="*50)

def main():
    """
    Función principal con menú interactivo para gestionar una lista enlazada de alumnos.

    Permite al usuario interactuar con la lista mediante un menú en consola,
    realizando operaciones como agregar, buscar, eliminar y mostrar alumnos.
    """
    lista = None  # Cabeza de la lista enlazada

    # AGREGAMOS LOS ALUMNOS PREDEFINIDOS AQUÍ
    lista = agregar_al_inicio(lista, Alumno("Alondra", 98))
    lista = agregar_al_final(lista, Alumno("Ana", 90))
    lista = agregar_al_final(lista, Alumno("Luis", 85))
    lista = agregar_al_inicio(lista, Alumno("Rocio", 92))
    lista = agregar_al_final(lista, Alumno("Carlos", 90))
    lista = agregar_al_final(lista, Alumno("María", 78))
    lista = agregar_al_inicio(lista, Alumno("Paola", 95))
    lista = agregar_al_final(lista, Alumno("Hugo", 84))
    lista = agregar_al_final(lista, Alumno("Alonso", 82))
    lista = agregar_al_final(lista, Alumno("Efren", 79))
    lista = agregar_al_inicio(lista, Alumno("Lilian", 98))

    while True:
        mostrar_menu()
        try:
            opcion = input("Seleccione una opción (0-9): ").strip()

            if opcion == "1":
                # Agregar al inicio
                nombre = input("Ingrese el nombre del alumno: ").strip()
                if not nombre:
                    print("❌ El nombre no puede estar vacío.")
                    continue
                try:
                    calificacion = float(input("Ingrese la calificación: "))
                    if calificacion < 0 or calificacion > 100:
                        print("⚠️  La calificación debe estar entre 0 y 100.")
                        continue
                except ValueError:
                    print("❌ Calificación inválida. Debe ser un número.")
                    continue
                lista = agregar_al_inicio(lista, Alumno(nombre, calificacion))
                print(f"✅ Alumno '{nombre}' agregado al INICIO.")

            elif opcion == "2":
                # Agregar al final
                nombre = input("Ingrese el nombre del alumno: ").strip()
                if not nombre:
                    print("❌ El nombre no puede estar vacío.")
                    continue
                try:
                    calificacion = float(input("Ingrese la calificación: "))
                    if calificacion < 0 or calificacion > 100:
                        print("⚠️  La calificación debe estar entre 0 y 100.")
                        continue
                except ValueError:
                    print("❌ Calificación inválida. Debe ser un número.")
                    continue
                lista = agregar_al_final(lista, Alumno(nombre, calificacion))
                print(f"✅ Alumno '{nombre}' agregado al FINAL.")

            elif opcion == "3":
                # Buscar por nombre
                nombre = input("Ingrese el nombre a buscar: ").strip()
                if not nombre:
                    print("❌ El nombre no puede estar vacío.")
                    continue
                alumno = buscar_por_nombre(lista, nombre)
                if alumno:
                    print(f"🔍 Alumno encontrado: {alumno}")
                else:
                    print(f"❌ No se encontró ningún alumno con el nombre '{nombre}'.")

            elif opcion == "4":
                # Buscar por calificación
                try:
                    calificacion = float(input("Ingrese la calificación a buscar: "))
                except ValueError:
                    print("❌ Calificación inválida.")
                    continue
                alumnos = buscar_por_calificacion(lista, calificacion)
                if alumnos:
                    print(f"🔍 Se encontraron {len(alumnos)} alumno(s) con calificación {calificacion}:")
                    for a in alumnos:
                        print(f"   - {a}")
                else:
                    print(f"❌ No se encontraron alumnos con calificación {calificacion}.")

            elif opcion == "5":
                # Eliminar por nombre
                nombre = input("Ingrese el nombre del alumno a eliminar: ").strip()
                if not nombre:
                    print("❌ El nombre no puede estar vacío.")
                    continue
                alumno_previo = buscar_por_nombre(lista, nombre)
                if not alumno_previo:
                    print(f"❌ No se puede eliminar: no existe un alumno llamado '{nombre}'.")
                else:
                    lista = eliminar_por_nombre(lista, nombre)
                    print(f"🗑️  Alumno '{nombre}' eliminado correctamente.")

            elif opcion == "6":
                # Eliminar por calificación
                try:
                    calificacion = float(input("Ingrese la calificación a eliminar: "))
                except ValueError:
                    print("❌ Calificación inválida.")
                    continue
                # Verificamos si hay alguien con esa calificación antes de eliminar
                alumnos_previos = buscar_por_calificacion(lista, calificacion)
                if not alumnos_previos:
                    print(f"❌ No hay alumnos con calificación {calificacion} para eliminar.")
                else:
                    lista = eliminar_por_calificacion(lista, calificacion)
                    print(f"🗑️  Se eliminaron {len(alumnos_previos)} alumno(s) con calificación {calificacion}.")

            elif opcion == "7":
                # Primer alumno
                cabeza = obtener_cabeza(lista)
                if cabeza:
                    print(f"🔝 Primer alumno: {cabeza.dato}")
                else:
                    print("❌ La lista está vacía.")

            elif opcion == "8":
                # Último alumno
                cola = obtener_cola(lista)
                if cola:
                    print(f"🔚 Último alumno: {cola.dato}")
                else:
                    print("❌ La lista está vacía.")

            elif opcion == "9":
                # Mostrar todos
                print("\n📋 Lista de alumnos:")
                imprimir_lista(lista)

            elif opcion == "0":
                print("\n👋 ¡Gracias por usar el sistema de gestión de alumnos!")
                break

            else:
                print("❌ Opción no válida. Por favor, seleccione una opción del 0 al 9.")

        except KeyboardInterrupt:
            print("\n\n⚠️  Operación cancelada por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    print("Programa finalizado.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()