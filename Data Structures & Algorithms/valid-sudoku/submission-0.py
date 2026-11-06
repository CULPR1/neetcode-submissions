class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        freq_map = {}
        freq_map_square = [{} for x in range(size)]
        for i in range(size):
            freq_map_row = {}
            freq_map_column = {}
            for j in range(size):
                if board[i][j] != ".":
                    freq_map_row[board[i][j]] = freq_map_row.get(board[i][j],0) + 1
                    sq_dict =freq_map_square[(i//3) * 3 + (j//3)]
                    sq_dict[board[i][j]] = sq_dict.get(board[i][j],0) + 1
                if board[j][i] != ".":
                    freq_map_column[board[j][i]] = freq_map_column.get(board[j][i],0) + 1

            if len(freq_map_row) != sum(freq_map_row.values()):
                return False
            if len(freq_map_column) != sum(freq_map_column.values()):
                return False
                    
        print(freq_map_square)
        for x in freq_map_square:
            print(f"{len(x)} total_values : {sum(x.values())}")
            if len(x) != sum(x.values()):
                return False

        return True