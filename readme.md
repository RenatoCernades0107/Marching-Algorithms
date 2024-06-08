# Ejercicios semana 10

Renato Aurelio Cernades Ames

## Marching squares

En el archivo `marching_squares.py` podrá encontrar el algoritmo completo del marching squares para crear figuras 2D en base a funciones implicitas.

### Input
```py
def draw_curve(func, output_file: str, min_x:float, min_y:float, min_z:float, max_x: float, max_y: float, max_z: float, precision: float)
```

`func`: Función implicita (float, float) -> float

`output_file`: Nombre del archivo output (string).

`min_x`, `min_y`, `max_x`, `max_y`: Son los límites en donde se creará la figura (float).

`precision`: La distancia más pequeña en que los cuadrados se pueden dividir en el algoritmo (float).

### Output
Crea un archivo tipo .eps.

### Tests

En el archivo `test_marching_cubes.py` podrá encontrar 3 ejemplos. Puede correclo con el comando `pytest -q test_marching_squares.py`. Cuando se probó, demoró 57.65 segundos en correr. Y obtuve los siguientes resultados:

<image src="images/circle.png">

<image src="images/sin.png">

<image src="images/tan.png">


## Marching cubes

En el archivo `marching_cubes.py` podrá encontrar el algoritmo completo del marching squares para crear figuras 3D en base a funciones implicitas.


### Input
```py
def draw_curve(func, output_file: str, min_x:float, min_y:float, min_z:float, max_x: float, max_y: float, max_z: float, precision: float)
```

`func`: Función implicita (float, float) -> float

`output_file`: Nombre del archivo output (string).

`min_x`, `min_y`, `min_z`, `max_x`, `max_y`, `max_z`: Son los límites en donde se creará la figura (float).

`precision`: La distancia más pequeña en que los cubos se pueden dividir en el algoritmo (float).

### Output
Crea un archivo tipo .off.

### Tests

En el archivo `test_marching_cubes.py` podrá encontrar 3 ejemplos. Puede correclo con el comando `pytest -q test_marching_cubes.py`. Cuando se probó, demoró 12.47 minutos en correr. Y obtuve los siguientes resultados:

<image src="images/sphere.png">

<image src="images/torus.png">

<image src="images/heart.png">
