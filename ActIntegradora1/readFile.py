"""
Este módulo proporciona funciones para leer archivos de texto y una función principal que
demuestra su uso leyendo archivos de códigos maliciosos y archivos de transmisión.

Funciones:
- read_file(files: list[str], mode: str = 'r', encoding: str = 'utf-8') -> list[str]:
  Lee una lista de archivos y devuelve su contenido como una lista de strings.
- readSingleFile(file: str, mode: str = 'r', encoding: str = 'utf-8') -> str:
  Lee un único archivo y devuelve su contenido como un string.

Ejemplo de uso:
    mcodes = ["mcode1.txt", "mcode2.txt", "mcode3.txt"]
    transmissions = ["transmission1.txt", "transmission2.txt"]
    dataM = read_file(mcodes)
    dataT = read_file(transmissions)
- Imprimir contenido de los archivos
    for content in dataM:
        print(content)
    for content in dataT:
        print(content)
"""

def read_file(files: list[str], mode: str = 'r', encoding: str = 'utf-8') -> list[str]:
    data = []
    for file in files:
        try:
            with open(file, mode, encoding=encoding) as f:
                data.append(f.read().strip())
        except FileNotFoundError:
            print(f"Error: El archivo {file} no fue encontrado!")
            return[]
        except IOError:
            print(f"Error: No se puede leer el archivo {file}!")
            return[]
    return data

def readSingleFile(file: str, mode: str = 'r', encoding: str = 'utf-8') -> str:
    with open(file, mode, encoding=encoding) as f:
        return f.read().strip()

