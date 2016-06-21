import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/pet
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.

# This function takes a single parameters containing a list
# with exactly five entries (one per contestant). Each entry 
# is a list with exactly four integers (the scores for that
# contestant)

class Contestant(object):
    Contestant_ID = 0

    def __init__(self, scores):
        Contestant.Contestant_ID += 1
        self.ID = Contestant.Contestant_ID
        self._scores = scores
        self._total = self.total_scores()

    @property
    def scores(self):
        return self._scores

    @property
    def total(self):
        return self._total

    def total_scores(self):
        total = sum(self._scores)
        return total


def solve2(contestant_scores):

    contestant = []
    for score in contestant_scores:
        c = Contestant(score)
        contestant.append(c)

    totals = {}
    for c in contestant:
        totals[c.ID] = c.total()

    ids = list(totals.keys())
    tot_score = list(totals.values())

    max_score = max(tot_score)

    winner = ids[tot_score.index(max_score)]

    return winner, max_score



def solve(contestant_scores):
    
    totals = []
    for score in contestant_scores:
        total_score = sum(score)
        totals.append(total_score)

    win_score = max(totals)

    for i, total in enumerate(totals):
        if total == win_score:
            winner = i + 1

    # Replace 1 with the winning contestant (remember that
    # contestants are 1-indexed, not 0-indexed) and replace 0
    # with the score of the winning contestant.
    return winner, win_score


#if __name__ == "__main__":
    #tokens = sys.stdin.read().strip().split()

   # scores = [ [int(tokens.pop(0)) for i in range(4)] for j in range(5) ]

   # pet, score = solve(scores)

   # print(pet, score)
