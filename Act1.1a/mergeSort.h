#ifndef MERGESORT_H
#define MERGESORT_H

#include <vector>
#include "merge.h"

inline void mergeSort(std::vector<double>& arr, int left, int right){
    if(left < right){
        int middle = left + (right - left) / 2;

        mergeSort(arr, left, middle);
        mergeSort(arr, middle + 1, right);

        merge(arr, left, middle, right);        
    }
}

#endif