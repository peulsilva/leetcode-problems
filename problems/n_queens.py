class Solution:
    def __init__(self):
        self.count = 0
        self.nqueens = 0
        self.niter =0

    def has_another_in_row(
        self,
        row
    ):
        if len(self.rows[row]) > 0:
            return True
        return False
    def has_another_in_col(
        self,
        col
    ):
        if len(self.cols[col]) > 0:
            return True
        return False

    def has_another_in_diagonal(
        self,
        i,
        j,
    ):
        left_diag_index = i - j
        if left_diag_index in self.diags_left:
            return True
        
        right_diag_index = i+j
        if right_diag_index in self.diags_right:
            return True
        
        return False

    def is_valid(
        self,
        i,
        j, 
    ):
        row_valid = not self.has_another_in_row(i)
        col_valid = not self.has_another_in_col(j)
        diagonal_valid = not self.has_another_in_diagonal(i,j)

        return row_valid and diagonal_valid and col_valid

    def valid_entries(
        self,
        chess_board
    ):
        valid_entries = []
        n = len(chess_board)

        for i in range(n):
            for j in range(n):
                if chess_board[i][j] == 0:
                    if (self.is_valid(i,j)):
                        valid_entries.append([i,j])

        return valid_entries

    def save_config(self, chess_board):
        d = []
        n = len(chess_board)
        for i in range(n):
            row = i
            col = self.cols[i].pop()
            d.append(tuple((i, col)))
            
            self.cols[i].add(col)

        self.configs.add(tuple(d))

    def solve_partial(self,chess_board):
        self.niter +=1

        valid_entries = self.valid_entries(chess_board)

        if len(valid_entries) == 0:
            return
        
        for (i,j) in valid_entries:
            chess_board[i][j] = 1
            self.rows[i].add(j)
            self.cols[j].add(i)
            self.diags_right.add(i+j)
            self.diags_left.add(i-j)

            self.nqueens += 1

            if self.nqueens == len(chess_board):
                self.count+=1
                self.save_config(chess_board)
                
            else:
                self.solve_partial(chess_board)

            chess_board[i][j] = 0
            self.rows[i].remove(j)
            self.cols[j].remove(i)
            self.diags_right.remove(i+j)
            self.diags_left.remove(i-j)

            self.nqueens -= 1

    def print_configs(self, n):
        all_configs = [ ]
        this_config = ['....' * n for _ in range(n)]

        for config in self.configs:
            for el in config:
                s = ''
                for i in range(n):
                    if i == el[1]:
                        s += 'Q'
                    else:
                        s += '.'
                this_config[el[0]] = s

            all_configs.append(this_config)

            this_config = ['....' * n for _ in range(n)]
        return all_configs

    def solveNQueens(self, n: int) :
        # self.configs = [set() for i in range(n)]
        self.configs = set()
        chess_board = [[0 for col in range(n)] for row in range(n)]

        self.rows = [set() for row in range(n)]
        self.cols = [set() for row in range(n)]
        self.diags_left = set()
        self.diags_right = set()

        self.solve_partial(chess_board)
        return self.print_configs(n)