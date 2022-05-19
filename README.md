# Problema-metro

Hola!!

### Sobre el proyecto
Este programa corresponde a una implementación de una posible solución al problema "Metro" de Buda, donde se busca encontrar la ruta mínima entre
dos estaciones de metro distintas dentro de una red de ellas. Además el tren y las estaciones pueden tener un color asociado, indicando que un tren
se detiene en estaciones de su propio color, o bien, sin color.

El programa esta construido en Python 🐍

## Uso

### Input del programa

La información necesaria para el problema debe estar estrucutrada en un archivo JSON, donde se indicará el color del tren, la estación de inicio 
y termino, y la información de cada estación (nombre, color y estaciones vecinas).

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
| Variable | Descripción 
| --- | ---| 
| < color > | Debe ser un string equivalente a uno de los colores disponibles ("red" y "green"), o bien "None" que representa sin color. | 
| < nombre_estacion_inicio > | Debe ser un string correspondiente al nombre de alguna estación de la red (cuyos nombres están definidos dentro del atributo "stations" del JSON). Representa el punto de partida de la búsqueda de la ruta mínima|
| < nombre_estacion_final > | Igual al caso anterior, pero representa la estación final de la ruta mínima a calcular|
| < nombre_estacion_x > |  Debe ser un string correspondiente al nombre de alguna estación de la red (cuyos nombres están definidos dentro del atributo "stations" del JSON). |
| < nombre_estacion_vecina > |   Debe ser un string correspondiente al nombre de una estación vecina. Osea, que tiene una conexión directa. |

Cabe señalar que, si la estacion "A" y "B" son vecinas, basta con incluir a la estacion "B" dentro de los "neighbors" de "A" y el programa automáticamente añadirá la relación recíproca sobre que "A" tambien es vecina de "B". Sin embargo, si se añaden ambas relaciones también esta correcto.

Más facil con un ejemplo! A continuación se muestra una red y su formato en JSON:

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

### Ejecución :zap:

El programa se ejecuta desde el terminal (situado a la misma altura que la carpeta "metro") con el comando:

  ```sh
  python3 -m metro <ruta_input>
   # e.g python3 -m metro metro/inputs/input_3.json
  ```
 Se espera el retorno de la ruta mínima que recorre el tren desde la estacion de inicio a la final indicada en el archivo input. También,puede ocurrir que se arroje un error, con un respectivo mensaje alertando el problema existente en el archivo de input.

## Tests

Se implementaron diferentes tests :test_tube: sobre las funciones y clases principales del programa mediante la librería UnitTest. Estos pueden ser ejecutados
mediante:

  ```sh
  python3 -m unittest discover 
  ```
