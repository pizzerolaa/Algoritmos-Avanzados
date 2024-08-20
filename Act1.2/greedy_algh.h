#ifndef GREEDY_ALGH_H
#define GREEDY_ALGH_H

#include <vector>

std::vector<int> greedy_algh(std::vector<int>& coins, int amount){
    std::vector<int> result(coins.size(), 0);
    for (size_t i = 0; i < coins.size(); i++){
        while(amount >= coins[i]) {
            result[i]++;
            amount -= coins[i];
        }
    }
    return result;
}

#endif