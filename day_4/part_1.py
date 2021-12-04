lines = open('day_4/input.txt', 'r').read().splitlines()

# List of numbers called
called = [int(num) for num in lines[0].split(',')]

# Create boards as 2D lists
boards_raw = '\n'.join(lines[2:]).split('\n\n')
boards = []

for board_raw in boards_raw:
    rows = board_raw.split('\n')
    board = []
    for row in rows:
        new_row = []
        cells = row.split()
        for cell in cells:
            new_row.append(int(cell))
        if len(new_row) > 0:
            board.append(new_row)
    if len(board) > 0:
        boards.append(board)
    
def check_win(board):
    # Check rows
    def check_row(row):
        for cell in row:
            if cell >= 0:
                return False
        return True
            
    for row in board:
        if check_row(row):
            # Entire row was negative, return true
            return True
    
    # Check columns
    def check_column(j):
        for i in range(len(board)):
            if board[i][j] >= 0:
                return False
        return True
    
    for j in range(len(board[0])):
        if check_column(j):
            # Entire column was negative, return true
            return True

    # Couldn't find a victory, return false
    return False
                

def find_winning_board_and_number(called, boards):
    # Call numbers until there's a winner
    for called_num in called:
        for board in boards:
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == called_num:
                        # Mark called numbers as negative and check for victory
                        if cell == 0:
                            board[i][j] = -99999 # Replace 0s with arbitrary negative (doesn't matter for now)
                        else:
                            board[i][j] = -cell
                        if check_win(board):
                            return (called_num, board)

if __name__ == '__main__':
    winning_num, winning_board = find_winning_board_and_number(called, boards)
    
    print(f'Winning number: {winning_num}')
    print(f'Winning board: {winning_board}')
    
    board_unmarked_sum = 0
    for row in winning_board:
        for cell in row:
            if cell > 0:
                board_unmarked_sum += cell
    
    print(f'Sum of unmarked numbers: {board_unmarked_sum}')
    print(f'Product of winning number and sum: {winning_num * board_unmarked_sum}')
