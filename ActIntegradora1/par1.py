import os
from readFile import readSingleFile
from kmp_algorithm import kmpSearch

def main():
    script = os.path.dirname(os.path.abspath(__file__))

    transmissions = ["transmission1.txt", "transmission2.txt"]
    mcodes = ["mcode1.txt", "mcode2.txt", "mcode3.txt"]

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