"""
Aquí se ejucuta todo el programa.
"""
import os
from readFile import readSingleFile
from kmp_algorithm import kmpSearch
from manachers_algorithm import findLPS
from lcs_algorithm import lcsAlgorithm

def main():
    script = os.path.dirname(os.path.abspath(__file__))

    transmissions = ["files/transmission1.txt", "files/transmission2.txt"]
    mcodes = ["files/mcode1.txt", "files/mcode2.txt", "files/mcode3.txt"]
    
    transmission_data = [readSingleFile(os.path.join(script, tfile)).replace("\n", "").replace("\r", "").strip() for tfile in transmissions]

    for i, tfile in enumerate(transmissions):
        print(f"\nAnalizando {tfile}...")

        for mfile in mcodes:
            mcode_path = os.path.join(script, mfile)
            mcode_data = readSingleFile(mcode_path).replace("\n", "").replace("\r", "").strip()

            found, indices = kmpSearch(mcode_data, transmission_data[i])

            if found:
                print(f"true {indices[0]} -> Patrón {mfile} encontrado en {tfile}")
            else:
                print(f"false -> Patrón {mfile} no encontrado en {tfile}")
        
        print(f"\nAnalizando LPS en {tfile}...")

        start, end = findLPS(transmission_data[i])

        print(f"{start}, {end}")

    print("\nAnalizando LCS entre transmission1.txt y transmission2.txt...")
    lcs = lcsAlgorithm(transmission_data[0], transmission_data[1])
    print(f"LCS: {lcs}")

if __name__ == "__main__":
    main()