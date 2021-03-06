# Problema-metro

Hola !! 馃檶

### Sobre el proyecto
Este programa corresponde a una implementaci贸n de una posible soluci贸n al problema "Metro" de Buda, donde se busca encontrar la ruta m铆nima entre
dos estaciones de metro distintas dentro de una red de ellas. Adem谩s el tren y las estaciones pueden tener un color asociado, indicando que un tren
se detiene en estaciones de su propio color, o bien, sin color.

El programa esta construido en Python 馃悕

## Uso

### Input del programa

La informaci贸n necesaria para el problema debe estar estrucutrada en un archivo JSON, donde se indicar谩 el color del tren, la estaci贸n de inicio 
y termino, y la informaci贸n de cada estaci贸n (nombre, color y estaciones vecinas).

El formato es el siguiente: 
  ```sh
  {
  "train color": <color>,
  "start": <nombre_estacion_inicio>,
  "target": <nombre_estacion_final>,
  "stations": {
    <nombre_estacion_x>: {
      "color": <color>,
      "neighbors": [
        <nombre_estacion_vecina>,
        <nombre_estacion_vecina>
      ]
    },
    <nombre_estacion_y>: {
      "color": <color>,
      "neighbors": [
        <nombre_estacion_vecina>,
        <nombre_estacion_vecina>
      ]
    },
    <nombre_estacion_z>: {
      "color": <color>,
      "neighbors": [
        <nombre_estacion_vecina>,
        <nombre_estacion_vecina>
      ]
    }
  }
}
  ```
Donde:
| Variable | Descripci贸n 
| --- | ---| 
| < color > | Debe ser un string equivalente a uno de los colores disponibles ("red" y "green"), o bien "None" que representa sin color. | 
| < nombre_estacion_inicio > | Debe ser un string correspondiente al nombre de alguna estaci贸n de la red (cuyos nombres est谩n definidos dentro del atributo "stations" del JSON). Representa el punto de partida de la b煤squeda de la ruta m铆nima|
| < nombre_estacion_final > | Igual al caso anterior, pero representa la estaci贸n final de la ruta m铆nima a calcular|
| < nombre_estacion_x > |  Debe ser un string correspondiente al nombre de alguna estaci贸n de la red (cuyos nombres est谩n definidos dentro del atributo "stations" del JSON). |
| < nombre_estacion_vecina > |   Debe ser un string correspondiente al nombre de una estaci贸n vecina. Osea, que tiene una conexi贸n directa. |

Cabe se帽alar que, si la estacion "A" y "B" son vecinas, basta con incluir a la estacion "B" dentro de los "neighbors" de "A" y el programa autom谩ticamente a帽adir谩 la relaci贸n rec铆proca sobre que "A" tambien es vecina de "B". Sin embargo, si se a帽aden ambas relaciones tambi茅n esta correcto.

M谩s facil con un ejemplo! A continuaci贸n se muestra una red y su formato en JSON:

![image](https://user-images.githubusercontent.com/48299079/169196314-df40c6fc-1f3c-480c-84f3-8f0808d28f4f.png)
```sh
{
  "train color": "red",
  "start": "A",
  "target": "C",
  "stations": {
    "A": {
      "color": "None",
      "neighbors": [
        "B",
        "C"
      ]
    },
    "B": {
      "color": "green",
      "neighbors": [
        "A",
        "C"
      ]
    },
    "C": {
      "color": "red",
      "neighbors": [
        "B",
        "A"
      ]
    }
  }
}
```
Tambi茅n en la carpeta input_examples/ puedes encontrar un dibujo de las redes descritas en metro/inputs, las que puedes modifcar su "start" y "target" para realizar pruebas y comprobarlas en el dibujo.

### Ejecuci贸n :zap:

El programa se ejecuta desde el terminal (situado a la misma altura que la carpeta "metro") con el comando:

  ```sh
  python3 -m metro <ruta_input>
   # e.g python3 -m metro metro/inputs/input_3.json
  ```
 Se espera el retorno de la ruta m铆nima que recorre el tren desde la estacion de inicio a la final indicada en el archivo input. Tambi茅n,puede ocurrir que se arroje un error, con un respectivo mensaje alertando el problema existente en el archivo de input.

## Tests

Se implementaron diferentes tests :test_tube: sobre las funciones y clases principales del programa mediante la librer铆a UnitTest. Estos pueden ser ejecutados
mediante:

  ```sh
  python3 -m unittest discover 
  ```
 ## Referencias
 
 EL dise帽o de la soluci贸n esta inspirada en el algoritmo Dijkstra, utilizado en grafos para encontrar la ruta m铆nima considerando arcos con costo. Esta idea fue adaptada al problema presentado, para lo cual recurr铆 a los siguientes ejemplos y fuentes de informaci贸n para guiar el desarrollo:
 
 - https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
 - https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
 - https://stackabuse.com/dijkstras-algorithm-in-python/
