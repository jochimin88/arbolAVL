# ArbolAVL
Implemetacion del arbol AVL

¿Que es un árbol AVL?
Los árboles AVL son un tipo especial de árbol binario. Inventado por los matemáticos rusos Adelson-Velskii y Landis, de allí el nombre AVL. 
El árbol AVL tiene la peculiaridad de ser el primer árbol binario auto-balanceable. 
Los árboles AVL están siempre equilibrados de tal modo que para todos los nodos la altura de la rama izquierda no difiere en más de una unidad de la altura de la rama derecha o viceversa.

La siguiente imagen es una representación de su equilibrio:


![](https://pythondiario.com/wp-content/uploads/2018/08/rotacionDoble2.gif.webp)

Para conseguir esta propiedad de equilibrio, la inserción y borrado de los nodos se ha de realizar de una forma especial. Si al realizar una operación de inserción o borrado de rompe la condición de equilibrio, hay que realizar una serie de rotaciones de nodos.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/AVL_Tree_Example.gif/220px-AVL_Tree_Example.gif)


Operaciones:
Otro punto a tener en cuenta son las operaciones que se pueden realizar en un árbol AVL. Esto nos servira para saber que métodos agregar al momento de la implementación.
Rotaciones:
El reequilibrado se produce de abajo hacia arriba sobre los nodos en los que se produce el desequilibrio. Pueden darse dos casos: rotación simple o rotación doble; a su vez ambos casos pueden ser hacia la derecha o hacia la izquierda.
Podemos realizar 4 tipos de rotaciones:
Rotación simple a la derecha:
De un árbol de raíz (r) y de hijos izquierdo (i) y derecho (d), lo que haremos será formar un nuevo árbol cuya raíz sea la raíz del hijo izquierdo, como hijo izquierdo colocamos el hijo izquierdo de i (nuestro i’) y como hijo derecho construimos un nuevo árbol que tendrá como raíz, la raíz del árbol (r), el hijo derecho de i (d’) será el hijo izquierdo y el hijo derecho será el hijo derecho del árbol (d).

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Rotacionsimplederecha1.JPG/300px-Rotacionsimplederecha1.JPG)

Rotación simple a la izquierda:
De un árbol de raíz (r) y de hijos izquierdo (i) y derecho (d), consiste en formar un nuevo árbol cuya raíz sea la raíz del hijo derecho, como hijo derecho colocamos el hijo derecho de d (nuestro d’) y como hijo izquierdo construimos un nuevo árbol que tendrá como raíz la raíz del árbol (r), el hijo izquierdo de d será el hijo derecho (i’) de r y el hijo izquierdo será el hijo izquierdo del árbol (i).

Precondición : Tiene que tener hijo derecho no vacío.


Rotación doble a la derecha:
La Rotación doble a la Derecha son dos rotaciones simples, primero rotación simple izquierda y luego rotación simple derecha.


![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/ROTACIONDCHA1.jpg/300px-ROTACIONDCHA1.jpg) ![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/ROTACIONDCHA2.jpg/300px-ROTACIONDCHA2.jpg)

Rotación doble a la izquierda
La Rotación doble a la Izquierda son dos rotaciones simples, primero rotación simple derecha y luego rotación simple izquierda.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/ROTACIONIZDA2.jpg/300px-ROTACIONIZDA2.jpg) ![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/ROTACIONIZQ2.jpg/300px-ROTACIONIZQ2.jpg)


Inserción:
La inserción en un árbol de AVL puede ser realizada insertando el valor dado en el árbol como si fuera un árbol de búsqueda binario desequilibrado y después retrocediendo hacia la raíz, rotando sobre cualquier nodo que pueda haberse desequilibrado durante la inserción.
Proceso de inserción:
Buscar hasta encontrar la posición de inserción o modificación (proceso idéntico a inserción en árbol binario de búsqueda).
Insertar el nuevo nodo con factor de equilibrio “equilibrado”.
Desandar el camino de búsqueda, verificando el equilibrio de los nodos, y re-equilibrando si es necesario.

![](https://commons.wikimedia.org/wiki/File:Insercion1.jpg)


