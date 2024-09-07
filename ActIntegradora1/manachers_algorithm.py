"""
Este archivo contiene la implementación del algoritmo de Manacher para encontrar 
el palíndromo más largo en una cadena de texto.

Funciones:
----------
- findLPS(txt: str) -> tuple[int, int]:
    Encuentra el palíndromo más largo en una cadena dada utilizando el algoritmo 
    de Manacher. La función transforma la cadena original para manejar palíndromos 
    de longitud par e impar, expande en torno a los centros y devuelve las posiciones 
    (iniciando en 1) del inicio y fin del palíndromo más largo.

Parámetros:
----------
- txt: str 
    La cadena de texto donde se buscará el palíndromo más largo.

Devuelve:
--------
- tuple[int, int]: 
    Una tupla con las posiciones 1-indexadas del inicio y fin del palíndromo más largo.

Descripción del Algoritmo:
--------------------------
El algoritmo de Manacher es eficiente para encontrar el palíndromo más largo en 
una cadena con complejidad O(n). Esto se logra transformando la cadena para unificar 
el manejo de palíndromos pares e impares, y expandiendo alrededor de cada carácter 
o separador agregado. Luego se registra la longitud del palíndromo más largo y 
sus posiciones.

La cadena de entrada se transforma agregando un carácter separador entre cada letra 
para manejar palíndromos pares e impares de la misma forma.
"""


def findLPS(txt: str) -> tuple[int, int]:
    n = len(txt)
    if n == 0:
        return (0, 0)
    
    t = '|'.join(f'^{txt}$') # cambiamos el formato agregando separador entre caracteres
    n = len(t)
    l = [0] * n
    center = 0
    right = 0
    max_len = 0
    max_center = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i  # indice espejo de i
        if i < right:
            l[i] = min(right - i, l[mirror])
        
        while t[i + l[i] + 1] == t[i - l[i] - 1]: # intentamos expandir alrededor del centro actual
            l[i] += 1
        
        if i + l[i] > right: # actualizamos el centro si expandimos más allá de la derecha actual
            center = i
            right = i + l[i]
        
        if l[i] > max_len: # actualizamos el palíndromo más largo
            max_len = l[i]
            max_center = i

    start = (max_center - max_len) // 2 # # encontramos los índices de inicio y fin del palíndromo original
    end = start + max_len - 1

    return start + 1, end + 1
