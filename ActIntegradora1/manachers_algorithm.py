"""

"""
def findLPS(txt: str) -> str:
    n = len(txt)
    if n == 0:
        return ""
    
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
    return txt[start: start + max_len]

text1 = "sdivinayateopinayanimilesoriginayanicetromedominayanimonarcasarepasonimulatocarretaacasonicotinayanicitavecinoanimacocinapedazogallinacedazotersonosretozadecanillagozadepanicocaminaonicevaticinayanitocinosacaaterracotaluminosaperasacranominayanimodemortecinayanigiroseliminayanipoetayanivida"
print(findLPS(text1))

