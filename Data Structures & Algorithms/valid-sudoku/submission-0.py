class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        store = defaultdict(int)
        
        #check rows
        for row in board:
            for digit in row:
                if digit == '.':
                    continue
                else:
                    store[digit] += 1
                    if store[digit] > 1:
                        return False
            store.clear()

        #check cols
        for i in range (9):
            for j in range (9):
                digit = board[j][i]
                if digit == '.':
                    continue
                else:
                    store[digit] += 1
                    if store[digit] > 1:
                        return False
            store.clear()

        #check boxes
        for i in range (0,9,3): # rows of box
            for j in range (0,9,3): # cols of box
                for k in range(3):
                    for m in range (3):
                        digit = board[i+k][j+m]
                        print(digit)
                        if digit == '.':
                            continue
                        else:
                            store[digit] += 1
                            if store[digit] > 1:
                                return False
                store.clear()

        return True





