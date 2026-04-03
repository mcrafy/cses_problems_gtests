#include <gtest/gtest.h>
#include <vector>

long long solve_apple_division(int n,  std::vector<long long> &P);

TEST(Introductory, AppleDivision_BaseCase)
{
    std::vector<long long> test = {3, 2, 7, 4, 1};
    int expected = 1;
    EXPECT_EQ(solve_apple_division(5,  test), expected);
}

TEST(Introductory, AppleDivision_EdgeCaseBig)
{
    std::vector<long long> test = {3, 2, 7, 100};
    int expected = 88;
    EXPECT_EQ(solve_apple_division(4, test), expected);
}

TEST(Introductory, AppleDivision_EdgeCaseOne)
{
    std::vector<long long> test = {5};
    int expected = 5;
    EXPECT_EQ(solve_apple_division(1, test), expected);
}