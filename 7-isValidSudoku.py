#Checking to see rows, and see if all numbers are digits between 0 and 9
#Checking to see if rows have any duplication
#Checking to see if columns have any duplication
#Looping through grids/sublists was tricky for me
#Got it from leetcode solutions
class Solution1(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            digit_check = [n for n in row if n != "." and (0 >= int(n) or int(n) > 9)]
            if digit_check:
              return False
            row_list = [n for n in row if n != "."]
            if len(set(row_list)) != len(row_list):
              return False

        for i in range(len(row)):
          col_list = []
          for row in board:
            col_list.append(row[i])
          col_list = [n for n in col_list if n != "."]
          if len(set(col_list)) != len(col_list):
            return False

        for i in (0, 3, 6):
          for j in (0, 3, 6):
            grid_list = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            grid_list = [n for n in grid_list if n != "."]
            if len(set(grid_list)) != len(grid_list):
              return False

        return True