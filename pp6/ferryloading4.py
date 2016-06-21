import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/ferryloading4
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


def solve(l, m, cars):
    # Your code here
    return 0

if __name__ == "__main__":
    tokens = sys.stdin.read().split()

    ntests = int(tokens.pop(0))

    for i in range(ntests):
        l = int(tokens.pop(0))
        m = int(tokens.pop(0))
        cars = []
        for j in range(m):
            cars.append( (int(tokens.pop(0)), tokens.pop(0)) )

        print(solve(l, m, cars))


