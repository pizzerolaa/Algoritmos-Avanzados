
"""
    Lee un archivo de texto y devuelve su contenido como una lista de strings.
    Args:
    file (str): Ruta al archivo de texto a leer.
    Returns:
    list[str]: Lista donde cada elemento es una línea del archivo.
"""
def read_file(file: str) -> list[str]:
    data_list = []
    with open(file) as file:
        for line in file:
            data_list.append(line.strip())
    return data_list

def main():
    file = "mcode1.txt"
    print(read_file(file))

if __name__ == "__main__":
    main()

