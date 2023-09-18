class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Неверный ввод. Введите еще!')

    def check_winner(self):
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return row[0]

        for col in range(len(self.board[0])):
            if all(self.board[row][col] == self.board[0][col] and self.board[0][col] != ' ' for row in range(3)):
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
        print('Добро пожаловать в Крестики-нолики.')
        self.print_board()

        while True:
            row = int(input('Введите строку (0-2): '))
            col = int(input('Введите столбец (0-2): '))

            self.make_move(row, col)
            self.print_board()

            winner = self.check_winner()
            if winner:
                print('Игрок', winner, 'победил!')
                break
            elif self.is_board_full():
                print("Ничья!")
                break


game = TicTacToe()
game.play()

# зачтено
