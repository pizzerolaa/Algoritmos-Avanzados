#include "mergeSort.h"
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int number;
    if (!(cin >> number)) {
        cerr << "Error al leer el número de elementos." << endl;
        return 1;
    }

    vector<double> arr(number);

    for (int i = 0; i < number; i++) {
        if (!(cin >> arr[i])) {
            cerr << "Error al leer el elemento en la posición " << i << "." << endl;
            return 1;
        }
    }

    mergeSort(arr, 0, number - 1);

    cout << "Arreglo ordenado: ";
    for (int i = 0; i < number; i++) {
        cout << arr[i] << (i < number - 1 ? ", " : "\n");
    }

    return 0;
}
