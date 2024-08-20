#include <iostream>
#include <vector>
#include <algorithm>
#include "dynamic_prog.h"
#include "greedy_algh.h"
#include "print_result.h"

int main() {
    int N;
    std::cin >> N;

    std::vector<int> coins(N);
    for (int i = 0; i < N; i++) {
        std::cin >> coins[i];
    }

    std::sort(coins.rbegin(), coins.rend()); //aqui ordenamos las monedas de + a -

    int Q;
    std::cin >> Q;

    std::cout << "Monedas disponibles:" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cout << coins[i] << " ";
    }
    std::cout << std::endl << std::endl;

    std::cout << "Programación Dinámica(DP):" << std::endl;
    std::vector<int> dpResult = dynamic_prog(coins, Q);
    print_result(dpResult, coins);

    std::cout << "Algoritmo Avaro(Greedy):" << std::endl;
    std::vector<int> greedyResult = greedy_algh(coins, Q);
    print_result(greedyResult, coins);

    return 0;
}