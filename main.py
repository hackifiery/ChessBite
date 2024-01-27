import engine
import chess

print('Welcome. Enter your FEN here to get the best move: ')
a = input('FEN: ')

b = chess.Board(a)
e = engine.Evaluate(a)

# Get the best move
best_move = e.get_best_move()
b.push(best_move)
ne = engine.Evaluate(b.fen())

# Print the updated board after the best move
print("Board after the best move:")
print(b)

# Print material advantage after making the best move
advantage_after_best_move = ne.get_material()
if advantage_after_best_move > 0:
    print('White is winning (+%d advantage)' % advantage_after_best_move)
elif advantage_after_best_move < 0:
    print('Black is winning (%d advantage)' % advantage_after_best_move)
else:
    print('Tied (+0 advantage)')

print("Best Move:", best_move.uci())
