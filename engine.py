import chess

values = {'n': 3, 'p': 1, 'b': 3, 'q': 9, 'r': 5, 'k': 0}
numbering = ['', 'p', 'n', 'b', 'r', 'q', 'k']

class Evaluate:
    def __init__(self, fen):
        self.values = values
        self.numbering = numbering
        self.b = chess.Board(fen)

    def evaluate_position(self):
        whitematerial = 0
        blackmaterial = 0
        for square in chess.SQUARES:
            piece = self.b.piece_at(square)
            if piece:
                if piece.color == chess.WHITE:
                    whitematerial += self.values[self.numbering[piece.piece_type]]
                else:
                    blackmaterial += self.values[self.numbering[piece.piece_type].lower()]
        return whitematerial - blackmaterial

    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.b.is_game_over():
            return self.evaluate_position()

        legal_moves = list(self.b.legal_moves)

        if maximizing_player:
            max_eval = float('-inf')
            for move in legal_moves:
                self.b.push(move)
                eval_val = self.minimax(depth - 1, False)
                self.b.pop()
                max_eval = max(max_eval, eval_val)
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                self.b.push(move)
                eval_val = self.minimax(depth - 1, True)
                self.b.pop()
                min_eval = min(min_eval, eval_val)
            return min_eval

    def get_best_moves(self, num_moves=3, depth=3):
        best_moves = []
        if self.b.turn == chess.WHITE:
            max_advantages = [float('-inf')] * num_moves
        else:
            min_advantages = [float('inf')] * num_moves

        legal_moves = list(self.b.legal_moves)

        for move in legal_moves:
            self.b.push(move)
            advantage = self.minimax(depth - 1, False)
            self.b.pop()

            if self.b.turn == chess.WHITE:
                for i in range(num_moves):
                    if advantage > max_advantages[i]:
                        max_advantages.insert(i, advantage)
                        best_moves.insert(i, move)
                        break
            else:
                for i in range(num_moves):
                    if advantage < min_advantages[i]:
                        min_advantages.insert(i, advantage)
                        best_moves.insert(i, move)
                        break

        return best_moves, max_advantages if self.b.turn == chess.WHITE else min_advantages
