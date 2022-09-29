# MetodosNumericos

Repositorio para los scripts suministrados en el módulo virtual de métodos numéricos del Politécnico Grancolombiano. 
Estos scripts han sido tomados de las lecturas fundamentales y el libro `Métodos numéricos con Python` de los profesores `Diego Arévalo Ovalle`, `Miguel Ángel Bernal Yermanos` y `Jaime Andrés Posada Restrepo`se han modificado para hacer más fácil su lectura e interpretación, documentando las funciones, modificando algunos nombres de variables y cambiando la forma en la que se presentan los resultados.

# Uso

Se creó un módulo llamado `cargarDatos.py`, el cual se usan en varios scripts, para darle un manejo un poco más simple al momento de cargar coordenadas del tipo (x,y). Dentro del archivo `datos.csv` se debe ingresar las coordenadas separadas por comas y cada coordenada debe ocupar una línea. Por ejemplo, para las coordenadas (5.4, 2) y (1, 3) el archivo debe lucir así:

5.4,2
1,3

# Requerimientos

Se pueden instalar a través del comando `pip install -r requirements.txt`

- El módulo `prettytable` es usado para mostrar los datos en una tabla ascii organizada.

Ejemplo de la salida en pantalla de los resultados.

![Ejemplo de salida](/imagenes/ejemplo_salida.png)

- El módulo `sympy` es usado para encontrar la derivada de la función a evaluar en el método de Newton, aún no está confirmado que sea exacto, por lo cual se recomienda hallar la derivada de forma manual para evitar errores.