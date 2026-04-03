#include <iostream>
#include <vector>
#include <climits>
#include <cstdlib>

long long solve_apple_division(int n, std::vector<long long> &P)
{
    long long total = 0;
    for (int i = 0; i < n; i++)
    {
        total += P[i];
    }

    long long min_diff = LLONG_MAX;
    for (int mask = 0; mask < 1 << n; ++mask)
    {
        long long subset = 0;
        for (int j = 0; j < n; ++j)
        {
            if (mask & 1 << j)
            {
                subset += P[j];
            }
            long long diff = abs(total - 2 * subset);

            if (diff < min_diff)
            {
                min_diff = diff;
            }
        }

    }
    return min_diff;
}

#ifndef RUNNING_TESTS
int main() {
    
    return 0;
}
#endif
