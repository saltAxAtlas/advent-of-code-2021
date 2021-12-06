def check_board(board):
    for row in board:
        if all(x == -1 for x in row):
            return True
    for col in zip(*board):
        if all(x == -1 for x in col):
            return True
    return False

f = open('./input.txt', 'r')

order = [*map(int, f.readline().split(','))]
boards = []

white_space = f.readline()
while white_space:
    a = [*map(int, f.readline().split())]
    b = [*map(int, f.readline().split())]
    c = [*map(int, f.readline().split())]
    d = [*map(int, f.readline().split())]
    e = [*map(int, f.readline().split())]
    boards.append([a,b,c,d,e])
    white_space = f.readline()

for num in order:
    if len(boards) > 1:
        winning_boards = []
        for index, board in enumerate(boards):
            new_board = []
            for row in board:
                new_row = [-1 if x == num else x for x in row]
                new_board.append(new_row)
            boards[index] = new_board
            if check_board(new_board):
                winning_boards.append(index)
        boards = [board for index, board in enumerate(boards) if index not in winning_boards]
    else:
        new_board = []
        for row in boards[0]:
            new_row = [-1 if x == num else x for x in row]
            new_board.append(new_row)
        boards[0] = new_board
        if check_board(boards[0]):
            print(sum(sum([x for x in row if x != -1]) for row in boards[0]) * num)
            exit()
