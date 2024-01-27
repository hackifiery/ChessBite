import chess

values = {'n': 3, 'p': 1, 'b': 3, 'q': 9, 'r': 5, 'k': 0}
numbering = ['', 'p', 'n', 'b', 'r', 'q', 'k']

class Evaluate:
    def __init__(self, fen):
        self.values = values
        self.numbering = numbering
        self.b = chess.Board(fen)

    def get_material(self):
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

    def get_best_move(self):
        best_move = None
        if self.b.turn == chess.WHITE:
            max_advantage = float('-inf')
        else:
            min_advantage = float('inf')

        for move in self.b.legal_moves:
            self.b.push(move)
            advantage = self.get_material()
            self.b.pop()

            if self.b.turn == chess.WHITE and advantage > max_advantage:
                max_advantage = advantage
                best_move = move
            elif self.b.turn == chess.BLACK and advantage < min_advantage:
                min_advantage = advantage
                best_move = move

        return best_move
