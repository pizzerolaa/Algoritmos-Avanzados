"""
Este módulo contiene la implementación del algoritmo de búsqueda KMP (Knuth-Morris-Pratt).

El algoritmo KMP se utiliza para buscar la ocurrencia de un patrón en un texto. Es eficiente y funciona en 
tiempo lineal respecto al tamaño del texto y del patrón, gracias al uso del arreglo LPS (Longest Prefix Suffix).

Funciones:
----------
- compLTSArr(pat: str) -> list[int]: 
    Calcula el arreglo LPS para el patrón dado.
- kmpSearch(pat: str, txt: str) -> tuple[bool, list[int]]: 
    Busca todas las ocurrencias del patrón en el texto y
    devuelve si se encontró alguna ocurrencia junto con las posiciones.

Ejemplo de uso:
---------------
    pattern = "ABC"
    text = "AABAACABACABABCAB"
    found, positions = kmpSearch(pattern, text)
    print(f"Encontrado: {found}")  # True si se encontró el patrón
    print(f"Posiciones: {positions}")  # Lista de posiciones donde empieza el patrón
"""
def compLTSArr(pat: str) -> list[int]:
    m = len(pat)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps 

def kmpSearch(pat: str, txt: str) -> tuple[bool, list[int]]:
    m = len(pat)
    n = len(txt)

    lps = compLTSArr(pat)
    result = []

    i = 0
    j = 0

    while (n - i) >= (m - j):
        if pat[j] == txt[i]:
            j += 1
            i += 1
        if j == m:
            result.append(i - j + 1)
            j = lps[j - 1]
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return (len(result) > 0, result)
