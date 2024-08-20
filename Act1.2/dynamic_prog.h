#ifndef DYNAMIC_PROG_H
#define DYNAMIC_PROG_H

#include <vector>
#include <climits>

std::vector<int> dynamic_prog(std::vector<int>& coins, int amount){
    std::vector<int> dp(amount + 1, INT_MAX);
    std::vector<int> choice(amount + 1, -1);
    dp[0] = 0;

    for(int i = 1; i <= amount; i++){
        for(size_t j = 0; j < coins.size(); j++){
            if(coins[j] <= i && dp[i - coins[j]] != INT_MAX && dp[i - coins[j]] + 1 < dp[i]){
                dp[i] = dp[i - coins[j]] + 1;
                choice[i] = static_cast<int>(j);
            }
        }
    }

    std::vector<int> result(coins.size(), 0);
    if(dp[amount] == INT_MAX){
        return result;
    }

    int current = amount;
    while(current > 0){
        result[choice[current]]++;
        current -= coins[choice[current]];
    }

    return result;
}

#endif