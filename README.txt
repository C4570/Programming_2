1. Como ejecutarlo

    Para hacerlo funcionar solo deberá de ejecutarse el archivo "menu.py".

2. Proceso de creación 

    Si bien el código está comentado, a continuación explicaré brevemente su funcionamiento.

    Al principio al solo tener la estructura del menú y la clase HashTable era fácil guiarse y mantener un orden sin perderse, pero más temprano que tarde
    la lectura del código se empezó a hacer engorrosa llegando al punto donde me ralentizaba la búsqueda de errores o para hacer alguna modificación por esto
    decidí dividir el código en 3 partes:  

    main.py: Este archivo es como su nombre indica el principal y más importante de los 3, ya que es donde se declaran tanto los objetos como funciones necesarias.
             A continuación explicaré un poco mejor cada objeto y función.
            
            class:
                -Producto: objeto según su código, nombre y una cantidad. Además de inicializar, también se encuentra un método para ver los atributos antes mencionados.
                -HashTable: tabla hash donde se guardan en listas dentro de listas los objetos Product según un index calculado a través de una función hash denotada 
                            como h(k) donde k es el código alfanumérico del producto. En caso de que la posición que del index esté ya ocupado y se produzca una 
                            Colisión, Product se guardará en la siguiente posición dentro de la lista en el index que se le asignó. Un ejemplo gráfico podría ser 
                            la siguiente:

                            Digamos que tenemos un Product el cual queremos insertar en nuestra tabla hash donde podemos ver que cada fila es una lista que contiene otra 
                            lista con otros Product o no adentro y queremos insertar nuestro Product en el index 1: 

                                                El Product se guarda después del 
                                                último elemento, es decir, acá
                                                                ↓
                            index   +-----------------------------------+               index   +-----------------------------------+
   Al estar ocupada  ->       1     | [Product1,Product2]               |                 1     | [Product1,Product2, Product]      |
        la fila                     +-----------------------------------+                       +-----------------------------------+
                              2     | [Product1,Product2,...,Productn ] |           \     2     | [Product1,Product2,...,Productn ] |
                                    +-----------------------------------+    --------\          +-----------------------------------+
                             ...    | [                ...            ] |    --------/   ...    | [                ...            ] |
                                    +-----------------------------------+           /           +-----------------------------------+
                              n     | [Product1,Product2,...,Productn ] |                 n     | [Product1,Product2,...,Productn ] |
                                    +-----------------------------------+                       +-----------------------------------+

                            También tiene sus métodos para buscar o eliminar un elemento y también para imprimir en pantalla estadísticas clave de la tabla como puede ser 
                            su factor de carga o la misma tabla.
                            Al intentar implementar el método de rehash, me encontré con muchas dificultades. El programa se quedaba atrapado en un bucle infinito y no pude 
                            encontrar el error. Debido a esto y a la falta de tiempo, no pude hacerlo funcionar.
           
            def:
                -text y choice: esta función junto a la función choice ayudan a simplificar código evitando la redundancia del mismo, ya que usaba varias veces el mismo 
                                código en distintos lugares
                -animation: animación de carga 
                -clear_screen: limpia la pantalla
                -validation: se valida la entrada de datos para evitar errores y/o el mal uso del programa o esta era la idea, pero por falta de tiempo no llego a programarla

    rand_gen.py: En pocas palabras, genera aleatoriamente objetos Product y los inserta dentro de la tabla hash para usarlos a modo de test. Si se quiere se puede modificar 
                 los nombres de los productos agregando o quitándolos de la lista "food_names" y en cuanto a la cantidad que genera también se puede aumentar o disminuir 
                 modificando la variable "x".
    
    menu.py: Basado en el esqueleto proporcionado, modifique, agregando y quitando opciones para crear un menú que se adapte a las necesidades del programa (Es solo un menú)

2. Preguntas

    2.1.¿Por qué elegí el método de multiplicación sobre otros?
    
    -Principalmente elegí este método debido a su eficiencia y eficacia frente a su simplicidad. El método de multiplicación es una excelente opción para una función hash 
     debido a su capacidad para distribuir uniformemente los valores hash en la tabla y reducir las colisiones. Esto se logra multiplicando la clave k por una constante A 
     entre 0 y 1 y extrayendo la parte fraccional del producto. Luego, este valor se multiplica por el tamaño de la tabla hash para obtener el valor hash. Además, el valor 
     de m (el tamaño de la tabla hash) no es tan crítico en este método como en otros, como el método de división. Esto permite tomar m como una potencia de 2 y aún así 
     obtener una buena distribución de valores hash. Además de estas ventajas, el método de multiplicación es fácil de implementar y rápido de calcular.
    

    2.2.¿Por qué y que elegí como clave y valor?
    
    -Tomé la decisión de elegir como key la clave alfanumérica de 10 dígitos del producto y como valor el nombre del mismo, ya que es menos probable que se repita 
     la clave alfanumérica y es más probable que se repita el nombre, además, es más sencillo e intuitivo usar la clave como clave y el nombre como valor.


    2.2.¿Qué valor elegí como tamaño?

    -Como tamaño elegi el valor de 60.000 ya que el supermercado vende normalmente 40.000 productos y de esta manera aunque se alcanzen los 40 mil productos 
     vendidos el factor de carga estara aproximadamente en 0.66 


    2.2.Porque SI es un problema utilizar un tamaño de tabla fijo 

    -Fijar el tamaño es un problema devido a que si el tamaño de la tabla es demasiado pequeño, puede haber una gran cantidad de colisiones, lo que ralentiza el 
    rendimiento. Por otro lado, si el tamaño de la tabla es demasiado grande, se desperdicia memoria y recursos del sistema. Además, si el número de elementos almacenados 
    en la tabla cambia con el tiempo, puede ser necesario redimensionar la tabla para evitar problemas de rendimiento o uso excesivo de memoria.