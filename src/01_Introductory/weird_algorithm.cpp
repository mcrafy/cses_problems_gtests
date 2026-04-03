//
// Created by mcrafy on 03.04.26.
//
#include <iostream>
#include <vector>
#include <string>

std::vector<long long> solve_weird_algorithm(long long n) {
    std::vector<long long> sequence;

    return sequence;
}
// --------------------------------

#ifndef RUNNING_TESTS
int main() {
    long long n;
    if (!(std::cin >> n)) return 0;

    auto result = solve_weird_algorithm(n);
    for (size_t i = 0; i < result.size(); ++i) {
        std::cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    std::cout << std::endl;
    return 0;
}
#endif