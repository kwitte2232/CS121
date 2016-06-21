import sys

# Skeleton code for problem https://uchicago.kattis.com/problems/uchicago%3Ampcs%3Atricky
#
# Make sure you read the problem before editing this code.
#
# You should focus only on implementing the solve() function.
# Do not modify any other code.


# This functions takes two parameters. Each is a list
# of strings representing the cards that each player
# will play in the game (each string has a single
# character: "A", "2", ..., "9", "J", "Q", or "K")
#
# If player one wins, you must return the string "PLAYER 1 WINS"
#
# If player two wins, you must return the string "PLAYER 2 WINS"
#
# If the game ends in a tie, you must return the string "TIE"
def solve(p1_cards, p2_cards):
    face_cards = {"J": 11, "Q": 12, "K": 13, "A": 14}
    faces = list(face_cards.keys())

    for i, card in enumerate(p1_cards):
        if type(card) == str:
            for face in faces:
                if card == face:
                    p1_cards[i] = face_cards[face]

    #print(p1_cards)

    for i, card in enumerate(p2_cards):
        if type(card) == str:
            for face in faces:
                if card == face:
                    p2_cards[i] = face_cards[face]

    #print(p2_cards)

    N = len(p1_cards)
    p1_count = 0
    p2_count = 0

    for i in range(N):
        if p1_cards[i] > p2_cards[i]:
            p1_count += 1
        elif p2_cards[i] > p1_cards[i]:
            p2_count += 1

    print(p1_count)
    print(p2_count)

    if p1_count > p2_count:
        return "PLAYER 1 WINS"
    elif p2_count > p1_count:
        return "PLAYER 2 WINS"
    else:
        return "TIE"

    # Write your solution here, and don't forget to update
    # the return statement to return the correct value.
    


#if __name__ == "__main__":
   # tokens = sys.stdin.read().strip().split()

    #n = int(tokens.pop(0))

   # p1_cards = [tokens.pop(0) for i in range(n)]
    #p2_cards = [tokens.pop(0) for i in range(n)]

   # print(solve(p1_cards, p2_cards))

