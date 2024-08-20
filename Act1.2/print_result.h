#ifndef PRINT_RESULT_H
#define PRINT_RESULT_H

#include <iostream>
#include <vector>

void print_result(const std::vector<int>& result, const std::vector<int>& coins){
    for(size_t i = 0; i < result.size(); i++){
        if (result[i] > 0) {
            std::cout << result[i] << " moneda(s) de " << coins[i] << std::endl;
        }
    }
    std::cout << std::endl;
}

#endif