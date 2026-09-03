# Cuadrícula interactiva con selección de círculos mediante coordenadas

Programa en Python que representa una cuadrícula de 8x8 en la consola. 
El usuario escribe una coordenada (X, Y) y el círculo correspondiente 
cambia de vacío a seleccionado. 
## Cómo ejecutarlo

```bash
python grid_app_consola.py
```

o, según cómo esté configurado tu sistema:

```bash
python3 grid_app_consola.py
```
## Explicación del código

Arriba de todo dejé guardados los colores que uso en la consola. Esos códigos raros como \033[93m son para que la terminal pinte de amarillo o de azul, y el COLOR_NORMAL es para volver a como estaba antes de pintar. También dejé fijo que la cuadrícula es de 8x8 para no estar poniendo el número por todos lados.

Después armo la cuadrícula en sí. Como no usé nada de tkinter ni gráficos, se me ocurrió representarla como una tabla, o sea una lista de listas: cada fila es una lista y adentro tiene 8 casillas. Al principio todas quedan con un punto porque ese es el que uso para decir que ahí no hay nada seleccionado todavía. Ahí uso dos for metidos uno dentro del otro, uno para las filas y otro para ir llenando cada columna de esa fila.

También dejé una lista vacía aparte, la de "seleccionadas". Ahí es donde voy guardando las coordenadas que el usuario va escogiendo, para poder mostrarle después cuáles ha usado.

La función mostrar_cuadricula() es la que se encarga de dibujar todo en pantalla cada vez que hace falta. Pone los números de columna arriba en amarillo, y después va fila por fila poniendo el número de esa fila también en amarillo, y mirando casilla por casilla si hay una O o un punto: si es O la pinta de azul, si no la deja normal.

La función coordenada_valida() la hice para no dejar que el usuario meta cualquier número. Solo revisa que esté entre 1 y 8 tanto en X como en Y, y si no, devuelve que es falso.

En seleccionar_coordenada() es donde pasa lo importante. Primero pregunta si la coordenada es válida usando la función anterior; si no lo es, avisa y no hace nada más. Si sí es válida, busca esa posición en la tabla y le cambia el puntico por una O. Y de una vez revisa si esa coordenada ya la había guardado antes: si no estaba, la mete a la lista y avisa que quedó seleccionada, y si ya estaba, le dice al usuario que esa ya la había escogido.

reiniciar_cuadricula() es más simple: solo vuelve a poner puntos en toda la tabla y vacía la lista de seleccionadas, como si arrancara de cero otra vez.

mostrar_seleccionadas() nada más mira si la lista está vacía o no y muestra lo que hay guardado.

Y al final está el menú, que es un while que se queda dando vueltas mostrando la cuadrícula y las opciones hasta que uno escriba 4 para salir. Según lo que uno escriba (1, 2, 3 o 4), hace una cosa distinta llamando a las funciones de arriba, y si uno escribe cualquier otra cosa le dice que esa opción no existe.

##Uso

1. Al iniciar, se muestra un menú con 4 opciones.
2. Elige la opción **1** y escribe una coordenada X y Y (ambas entre 1 y 8) para seleccionar un círculo.
3. Elige la opción **2** para ver el historial de coordenadas seleccionadas.
4. Elige la opción **3** para reiniciar la cuadrícula.
5. Elige la opción **4** para salir del programa.
