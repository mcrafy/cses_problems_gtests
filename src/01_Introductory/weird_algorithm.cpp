//
// Created by mcrafy on 03.04.26.
//
#include <iostream>
#include <vector>
#include <string>

std::vector<long long> solve_weird_algorithm(long long n)
{
    std::vector<long long> sequence;
    sequence.reserve(n);
    sequence.push_back(n);

    while (n != 1)
    {
        if ((n & 1) == 0)
            n >>= 1;
        else
            n = n * 3 + 1;
        sequence.push_back(n);
    }

    return sequence;
}
// --------------------------------

#ifndef RUNNING_TESTS
int main()
{
    long long n;
    if (!(std::cin >> n)) return 0;

    auto result = solve_weird_algorithm(n);
    for (size_t i = 0; i < result.size(); ++i)
    {
        std::cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    std::cout << std::endl;
    return 0;
}
#endif