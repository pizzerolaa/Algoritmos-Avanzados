"""
El programa analiza si el contenido de los archivos mcode1.txt, mcode2.txt y mcode3.txt están contenidos 
en los archivos transmission1.txt y transmission2.txt y despliega un true o false si es que las secuencias de 
chars están contenidas o no. En caso de ser true, muestra true, seguido de exactamente un espacio, seguido de 
la posición en el archivo de transmissiónX.txt donde inicia el código de mcodeY.txt
"""
import os
from readFile import readSingleFile
from kmp_algorithm import kmpSearch

def main():
    script = os.path.dirname(os.path.abspath(__file__))

    transmissions = ["files/transmission1.txt", "files/transmission2.txt"]
    mcodes = ["files/mcode1.txt", "files/mcode2.txt", "files/mcode3.txt"]

    for tfile in transmissions:
        transmission_path = os.path.join(script, tfile)
        transmission_data = readSingleFile(transmission_path).replace("\n", "").replace("\r", "").strip()

        print(f"Analizando {tfile}...")

        for mfile in mcodes:
            mcode_path = os.path.join(script, mfile)
            mcode_data = readSingleFile(mcode_path).replace("\n", "").replace("\r", "").strip()

            found, indices = kmpSearch(mcode_data, transmission_data)

            if found:
                print(f"true {indices[0]} -> Patrón {mfile} encontrado en {tfile}")
            else:
                print(f"false -> Patrón {mfile} no encontrado en {tfile}")

if __name__ == "__main__":
    main()