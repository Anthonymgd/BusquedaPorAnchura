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

            