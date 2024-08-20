#ifndef MERGE_H
#define MERGE_H

#include <vector>

inline void merge(std::vector<double>& arr, int left, int middle, int right) {
    int lenL = middle - left + 1;
    int lenR = right - middle;

    std::vector<double> tempL(lenL), tempR(lenR);

    for(int i = 0; i < lenL; i++){
        tempL[i] = arr[left + i];
    }
    for(int j = 0; j < lenR; j++){
        tempR[j] = arr[middle + 1 + j];
    }

    int i = 0, j = 0, k = left;

    while(i < lenL && j < lenR){
        if(tempL[i] >= tempR[j]){
            arr[k] = tempL[i];
            i++;
        } else {
            arr[k] = tempR[j];
            j++;
        }
        k++;
    }

    while (i < lenL){
        arr[k] = tempL[i];
        i++;
        k++;
    }

    while(j < lenR){
        arr[k] = tempR[j];
        j++;
        k++;
    }
}

#endif