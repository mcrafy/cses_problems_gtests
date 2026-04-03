#include <gtest/gtest.h>
#include <vector>

long long solve_apple_division(int n, const std::vector<long long> &P);

TEST(Introductory, AppleDivision_BaseCase)
{
    int expected = 1;
    EXPECT_EQ(solve_apple_division(5, std::vector<long long>{3, 2, 7, 4, 1}), expected);
}

TEST(Introductory, AppleDivision_EdgeCaseBig)
{
    int expected = 88;
    EXPECT_EQ(solve_apple_division(5, std::vector<long long>{3, 2, 7, 100}), expected);
}

TEST(Introductory, AppleDivision_EdgeCaseOne)
{
    int expected = 5;
    EXPECT_EQ(solve_apple_division(1, std::vector<long long>{5}), expected);
}