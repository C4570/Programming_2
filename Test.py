class Producto:
    def __init__(self, codigo, cantidad):
        self.codigo = codigo
        self.cantidad = cantidad

class TablaHash:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)]

    def _hash(self, codigo):
        # Función de hash simple utilizando la suma de los valores ASCII
        hash_value = sum(ord(c) for c in codigo)
        return hash_value % self.capacidad

    def insertar_producto(self, producto):
        indice = self._hash(producto.codigo)
        self.tabla[indice].append(producto)

    def eliminar_producto(self, codigo):
        indice = self._hash(codigo)
        lista_productos = self.tabla[indice]
        for i, producto in enumerate(lista_productos):
            if producto.codigo == codigo:
                del lista_productos[i]
                return

    def buscar_producto(self, codigo):
        indice = self._hash(codigo)
        lista_productos = self.tabla[indice]
        for producto in lista_productos:
            if producto.codigo == codigo:
                return producto
        return None

    def factor_carga(self):
        elementos = sum(len(lista) for lista in self.tabla)
        return elementos / self.capacidad

    def longitud_lista_mas_larga(self):
        max_longitud = max(len(lista) for lista in self.tabla)
        return max_longitud

    def cantidad_elementos(self):
        elementos = sum(len(lista) for lista in self.tabla)
        return elementos


def imprimir_estadisticas(tabla):
    print("Estadísticas del programa:")
    print("Factor de carga:", tabla.factor_carga())
    print("Longitud de la lista más larga:", tabla.longitud_lista_mas_larga())
    print("Cantidad de elementos:", tabla.cantidad_elementos())


def main():
    capacidad_tabla = 10000  # Capacidad inicial de la tabla hash
    tabla = TablaHash(capacidad_tabla)

    # Ejemplo de uso
    producto1 = Producto("AAN1235465", 10)
    producto2 = Producto("123ABCDE12", 5)

    tabla.insertar_producto(producto1)
    tabla.insertar_producto(producto2)

    print("Producto encontrado:", tabla.buscar_producto("AAN1235465").codigo)
    print("Producto no encontrado:", tabla.buscar_producto("XYZ9876543"))

    tabla.eliminar_producto("AAN1235465")

    imprimir_estadisticas(tabla)


if __name__ == "__main__":
    main()
