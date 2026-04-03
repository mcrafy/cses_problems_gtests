//
// Created by mcrafy on 03.04.26.
//
#include <gtest/gtest.h>
#include <vector>

std::vector<long long> solve_weird_algorithm(long long n);

TEST(Introductory, WeirdAlgorithm_BaseCase) {
    std::vector<long long> expected = {3, 10, 5, 16, 8, 4, 2, 1};
    EXPECT_EQ(solve_weird_algorithm(3), expected);
}

TEST(Introductory, WeirdAlgorithm_EdgeCaseOne) {
    std::vector<long long> expected = {1};
    EXPECT_EQ(solve_weird_algorithm(1), expected);
}
