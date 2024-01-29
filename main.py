import chess
from engine import Evaluate, RestartEval
import sys

print('Welcome to ChessBite!')

def main():
    # Get user FEN input
    fen_input = input('Enter the FEN string: ')

    # Create the evaluation engine
    try:
        e = Evaluate(fen_input)
    except RestartEval:
        print('Error: invalid FEN.', file = sys.stderr)
        main()

    # Get the best moves and their evaluations
    best_moves, advantages = e.get_best_moves(num_moves=3)

    if best_moves:
        # Print the best moves and their evaluations
        print("Top 3 Moves and Evaluations:")
        for move, advantage in zip(best_moves, advantages):
            print(f"Move: {move.uci()}, Advantage: {advantage}")
    else:
        print("No legal moves found.")

while True:
    try:
        main()
    except ValueError:
        print('Error: invalid FEN.', file = sys.stderr)
        main()
    except RestartEval:
        print('An error occurred.', file = sys.stderr)
        main()
