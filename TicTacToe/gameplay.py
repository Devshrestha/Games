
from math import inf as infinity
import time


class game:
    def __init__(self, mode, p1):
        # self.grid=[['1','2','3'],['4','5','6'],['7','8','9']]
        self.grid = [['  ', '  ', '  '], [
            '  ', '  ', '  '], ['  ', '  ', '  ']]
        self.playing = True
        self.turn = 1
        self.mode = mode
        self.stat = "Player1 turn "
        self.winner = None
        self.win = None
        self.available = [(0, 0), (0, 1), (0, 2), (1, 0),
                          (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        if p1 == 1:
            self.marker = ['', 'X', 'O']
        else:
            self.marker = ['', 'O', 'X']
        self.scores = {self.marker[2]: 10, self.marker[1]: -10, 'tie': 0}

    def minimax(self, a, depth, ismaximizing):
        print(self.grid)
        board=a.copy()
        stop=self.ai_check_winner(board)
        if stop  == self.marker[1]:
            return -10
        elif stop==self.marker[2]:
            return 10
        elif stop=='tie':
            return 0

        if ismaximizing:
            best_score = -infinity
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '  ':

                        board[i][j] = self.marker[2]
                        score_a = self.minimax(board, depth+1, False)

                        best_score = max(score_a, best_score)

            return best_score
        else:

            worst_score = infinity
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "  ":
                        board[i][j] = self.marker[1]
                        score_p = self.minimax(board, depth+1, True)

                        worst_score = min(score_p, worst_score)

            return worst_score

    def chosse_bests_move(self,copy_board):
        bestscore = -infinity
        for i in range(3):
            for j in range(3):
                if copy_board[i][j] == '  ':

                    copy_board[i][j] = self.marker[2]
                    score = self.minimax(copy_board, 0, False)
                    copy_board[i][j] = '  '
                    if score > bestscore:
                        bestscore = score
                        best_move = (i, j)
        return best_move

    def ai_update(self, i, j):
        self.check_winner()
        if self.winner != None:
            return
        if self.turn == 2:
            a=self.grid.copy()
            move=self.chosse_bests_move(a[:])    
            self.grid[move[0]][move[1]] = self.marker[2]
            self.available.remove(move)
            self.turn = 1

        else:
            if (i, j) in self.available:
                self.grid[i][j] = self.marker[1]
                self.available.remove((i, j))
                self.turn = 2

    def update(self, j, i):
        if (j, i) in self.available:
            if self.turn == 1:
                self.grid[j][i] = self.marker[1]
                self.status("Player2 turn")
                self.turn = 2
            else:
                self.grid[j][i] = self.marker[2]
                self.status("Player1 turn")
                self.turn = 1
            self.available.remove((j, i))
            self.check_winner()

    def status(self, msg):
        # try to keep message len between 8 to 12
        self.stat = msg

    def the_winner(self, win):
        if win == 't':
            self.status('Its a Tie!')
        # for pvp
        if self.mode == 1:
            if self.marker[1] == win:
                self.status('Player1 Won')
            elif self.marker[2] == win:
                self.status('Player2 Won')
        elif self.mode == 2:
            if self.marker[1] == win:
                self.status('Player1 Won')
            elif self.marker[2] == win:
                self.status("Computer Won")

    def check_winner(self):
        # across
        for i in range(3):
            if (self.grid[i][0] == self.grid[i][1] == self.grid[i][2]) and self.grid[i][0] != '  ':
                self.winner = self.grid[i][0]
                self.the_winner(self.grid[i][0])
                self.playing = False
        # down
        for i in range(3):
            if (self.grid[0][i] == self.grid[1][i] == self.grid[2][i]) and self.grid[i][i] != '  ':
                self.winner = self.grid[0][i]
                self.the_winner(self.grid[0][i])
                self.playing = False
        # diagnal
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2])and self.grid[0][0] != '  ':
            self.winner = self.grid[1][1]
            self.the_winner(self.grid[1][1])
            self.playing = False

        if (self.grid[2][0] == self.grid[1][1] == self.grid[0][2])and self.grid[1][1] != '  ':
            self.winner = self.grid[1][1]
            self.the_winner(self.grid[1][1])
            self.playing = False

        # tie
        if len(self.available) == 0 and self.winner == None:

            self.winner = 'tie'
            self.the_winner('t')
            self.playing = False

    def ai_check_winner(self,board):
            # across
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != '  ':
                return board[i][0]

        # down
        for i in range(3):
            if (board[0][i] == board[1][i] == board[2][i]) and board[i][i] != '  ':
                return board[0][i]

        # diagnal
        if (board[0][0] == board[1][1] == board[2][2])and board[0][0] != '  ':
            return board[1][1]

        if (board[2][0] == board[1][1] == board[0][2])and board[1][1] != '  ':
            return board[1][1]

        # tie
        set_flag=0
        for i in range(3):
            for j in range(3):
                if board[i][j]=='  ':
                    set_flag=1
        
        if set_flag == 0:
            return 'tie'