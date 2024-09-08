"""
Este archivo contiene la implementación del algoritmo para encontrar la 
subsecuencia común más larga (LCS) entre dos cadenas de texto.

Funciones:
----------
- lcsAlgorithm(s1: str, s2: str) -> str:
    Implementa el algoritmo de programación dinámica para encontrar la 
    subsecuencia común más larga entre dos cadenas de entrada. Devuelve 
    la subsecuencia más larga encontrada.

Parámetros:
-----------
- s1: str 
    Primera cadena de texto.
- s2: str 
    Segunda cadena de texto.

Devuelve:
--------
- str: 
    La subsecuencia común más larga entre las dos cadenas dadas. Si no se 
    encuentra ninguna, se devuelve una cadena vacía.

Descripción del Algoritmo:
--------------------------
El algoritmo de la subsecuencia común más larga (LCS) utiliza una tabla de 
programación dinámica para almacenar las longitudes de las subsecuencias comunes 
en diferentes puntos de ambas cadenas. La complejidad de este algoritmo es O(m * n), 
donde 'm' y 'n' son las longitudes de las cadenas s1 y s2, respectivamente.

Se compara cada carácter de s1 con cada carácter de s2 y se construye una tabla de 
tamaño (m+1) x (n+1) donde cada celda (i, j) contiene la longitud de la subsecuencia 
común más larga que termina en los caracteres i-ésimo de s1 y j-ésimo de s2.

Si los caracteres coinciden, el valor de la celda es 1 más el valor de la celda 
diagonalmente anterior. Si no coinciden, la celda se inicializa en 0.

La subsecuencia más larga se identifica mediante el valor máximo en la tabla, 
que también indica el índice de finalización en la primera cadena, desde donde 
se puede reconstruir la subsecuencia.
"""


def lcsAlgorithm(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0
    end = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    end = i
            else:
                dp[i][j] = 0
    
    return s1[end - length:end]