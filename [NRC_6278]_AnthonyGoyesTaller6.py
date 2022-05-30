# Se importa la librería de Lifo y Fifo
# Queue: módulo que implementa colas multi-productor y multi-consumidor.
from queue import Queue
 
# Se genera la clase que contendrá al algoritmo de búsqueda no informada.
class Grafo:
    """
    Una clase que representa a un grafo.

    ...
    
    Argumentos
    ----------
    num_nodos: entero
        Es usado para determinar el número de nodos.
    dirigido: booleano
        Determina si el nodo es dirigido. Valor por defecto "Verdadero".

    Atributos
    ---------
    matriz_num_nodos : entero
        Número de nodos en el grafo.
    matriz_nodos : entero
        Clave del nodo generado.
    matriz_dirigido : booleano
        Determina si el nodo es dirigido.
    matriz_lista_adyacencia: diccionario
        Almacena los nodos como  un conjunto no ordenado de pares clave-valor.

    Métodos
    -------
    agregar_arista(self, nodo1, nodo2, peso=1):
        Agrega una arista o arco entre dos nodos a la representación del grafo.

    imprimir_lista_adyacencia(self):
        Imprime la lista de adyacencia como representación del grafo.

    bpa(self, nodo_inicial):
        Función que imprime el recorrido por búsqueda en anchura.
    """
    # Se establece el constructor de la clase
    def __init__(self, num_nodos, dirigido=True):
        """
        Contructor con todos los atributos necesarios para la clase grafo.

        Parámetros
        ----------
        matriz_num_nodos : entero
            Número de nodos en el grafo.
        matriz_nodos : entero
            Clave del nodo generado.
        matriz_dirigido : booleano
            Determina si el nodo es dirigido.
        matriz_lista_adyacencia: diccionario
            Almacena los nodos como  un conjunto no ordenado de pares clave-valor.
        """
        # Se inicializan los atributos de la clase
        # Atributo: número de nodos
        self.matriz_num_nodos = num_nodos
        # Se establece que el nodo debe estar en el rango permitido
        self.matriz_nodos = range(self.matriz_num_nodos)
        # Atributo: dirigido. Por defecto "Verdadero"
        self.matriz_dirigido = dirigido
        #Representación gráfica con una lista de adyacencia
        #Se genera un diccionario y se settea todos los nodos con un ciclo repetitivo "para"
        self.matriz_lista_adyacencia = {nodo: set() for nodo in self.matriz_nodos}     
         
    #  Función que agrega una arista o arco entre dos nodos a la representación del grafo
    def agregar_arista(self, nodo1, nodo2, peso=1):
        """
        Agrega una arista o arco entre dos nodos a la representación del grafo.

        El último argumento, peso, tiene como valor asignado 1.

        Parámetros
        ----------
        nodo1 : entero
            Almacena el valor para el primer nodo.
        nodo2 : entero
            Almacena el valor para el segundo nodo.
        nodo1 : entero
            Almacena el peso de los arcos, línea que une los nodos. Valor por defecto 1. 

        Retorna
        -------
        A un index del diccionario establecido, matriz_lista_adyacencio[clave], se le 
        añadirá su nodo adyacente, nodo# y el peso. 
        """
        # Añade una arista del nodo 1 al 2 con peso por defecto 1
        self.matriz_lista_adyacencia[nodo1].add((nodo2, peso))
        # Si la matriz no es dirigida, añade una arista del nodo 2 al 1 con peso por defecto 1
        if not self.matriz_dirigido:
            self.matriz_lista_adyacencia[nodo2].add((nodo1, peso))
   
    # Función que imprime la lista de adyacencia
    def imprimir_lista_adyacencia(self):
        """
        Imprime la lista de adyacencia como representación del grafo.

        Parámetros
        ----------
        Ninguno

        Retorna
        -------
        Una cadena de texto con la matriz de adyacencia generada.
        """
        for key in self.matriz_lista_adyacencia.keys():
            print("node", key, ": ", self.matriz_lista_adyacencia[key])

    # Función que imprime el recorrido de la busqueda por anchura de un vértice fuente dado.
    # bpa hace referencia al algoritmo de búsqueda por anchura
    def bpa(self, nodo_inicial):
        """
        Imprime el recorrido de la busqueda por anchura de un vértice fuente dado.

        Parámetros
        ----------
        nodo_inicial : entero
            Representa al nodo raíz del grafo generado.

        Retorna
        -------
        Una cadena de texto con la matriz de adyacencia generada.
        """
        # Se genera una variable tipo "colecciones" para prevenir ciclos infinitos
        visitado = set()
        # Se instancia la clase para trabajar con colas, una estructura de datos
        queue = Queue()

        # Se añade el nodo inicial a la cola y a la colección
        queue.put(nodo_inicial)
        visitado.add(nodo_inicial)

        # Ciclo repetitivo "mietras" la cola no esté vacía realice el bloque de código interno.
        while not queue.empty():
            # Recorre la cola y almacena el nodo en una variable
            nodo_actual = queue.get()
            # Imprime el nodo almacenado y termina con un salto de línea
            print(nodo_actual, end = " ")

            # Ciclo repetitivo "para". Obtiene los vértices adyacentes del
            # vértice desencolado, nodo actual.
            for (nodo_siguiente, peso) in self.matriz_lista_adyacencia[nodo_actual]:
                # Si vértice  adyacente no ha sido visitado, entonces lo marca
                # como visitado y lo agrega a la cola
                if nodo_siguiente not in visitado:
                    queue.put(nodo_siguiente)
                    visitado.add(nodo_siguiente)
 
if __name__ == "__main__":
    #Ejecución del algoritmo búsqueda por anchura
    #Se instancia la clase
    #Parámetro:
    #   número de nodos : 9 | Tipo : entero
    #   dirigido: falso | Tipo: booleano
    grafo = Grafo(5, dirigido=True)
 
    # Añade las aristas con peso por defecto 1
    grafo.agregar_arista(0, 1)
    grafo.agregar_arista(0, 2)
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(1, 4)
    grafo.agregar_arista(2, 3)
 
    # Imprime la lista de adyacencia como tipo de dato "diccionario": {(nodo, peso)}
    grafo.imprimir_lista_adyacencia()

    print ("Imprimiendo el resultado del primer recorrido del algoritmo debúsqueda por peso " 
                "(comenzando por el vértice 0): ")
    grafo.bpa(0)
    print()

