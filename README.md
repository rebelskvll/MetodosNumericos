# MetodosNumericos
Repositorio para los scripts suministrados en el módulo virtual de métodos numéricos del Politécnico Grancolombiano. 
Estos scripts han sido tomados de la lectura fundamental 1 y se han modificado para hacer más fácil su lectura e interpretación, documentando las funciones, modificando algunos nombres de variables y cambiando la forma en la que se presentan los resultados.

# Requerimientos

Se pueden instalar a través del comando `pip install -r requirements.txt`

- El módulo `prettytable` es usado para mostrar los datos en una tabla ascii organizada.

Ejemplo de la salida en pantalla de los resultados.

![Ejemplo de salida](/imagenes/ejemplo_salida.png)

- El módulo `sympy` es usado para encontrar la derivada de la función a evaluar en el método de Newton, aún no está confirmado que sea exacto, por lo cual se recomienda hallar la derivada de forma manual para evitar errores. 