'''
TAD - Matriz

__init__: Recibe dos dimensiones y crea una matriz de elementos nulos de dichas 
dimensiones (filas x columnas).

get: Recibe dos posiciones y devuelve el elemento guardado en la matriz en dicha posicion.
Retorna None si las posiciones son invalidas. put: Recibe dos posiciones y un valor float y
actualiza dicha posicion en la matriz con el valor de float. Devuelve el valor nuevo si las 
posiciones son validas, o None si son invalidas

__add__: Recibe como parametro otra matriz. Si las dimensiones de ambas matrices no 
son compatibles, devuelve None. Si las dimensiones son compatibles, devuelve una nueva 
matriz con el resultado de la suma matricial entre ambas, o sea sumar componente a 
componente.

'''
class Matriz:
    def __init__(self, rows, columns):
        if rows <= 0 or columns <= 0:
            return 'Entrada no valida'
        
        else:
            self.matriz = []
            self.rows = rows
            self.columns = columns
            
            for row in range(self.rows):
                self.matriz.append([[]] * self.columns)

    def get(self, row, column):    
        if row > self.rows or column > self.columns or isinstance(row, float) or isinstance(column, float):
            return None
        else:
            return self.matriz[row-1][column-1]     
    
    def put(self, row, column, value):
        if row > self.rows or column > self.columns or isinstance(value, int):
            return None
        else:
            self.matriz[row-1][column-1] = value
            return self.matriz[row-1][column-1]    
       
    def __add__(self, matriz):
        if self.rows == matriz.rows and self.columns == matriz.columns:
            new_matriz = Matriz(self.rows,self.columns)
            for row in range(self.rows):
                for column in range(self.columns):
                    new_matriz.put(row, column, self.get(row, column) + matriz.get(row, column))
            return new_matriz.matriz
        else:
            return None


matriz1 = Matriz(2,2)
matriz2 = Matriz(2,2)

matriz1.put(1, 1, 1.5)
matriz1.put(1, 2, 2.5)
matriz1.put(2, 1, 3.5)
matriz1.put(2, 2, 4.5)

matriz2.put(1, 1, 1.5)
matriz2.put(1, 2, 2.5)
matriz2.put(2, 1, 3.5)
matriz2.put(2, 2, 4.5)

print(matriz1.__add__(matriz2))