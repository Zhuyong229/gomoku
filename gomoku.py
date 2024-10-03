"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 28, 2022
"""

def is_empty(board):
    for i in range(0,len(board)):
        for k in range(0,len(board)):
            if board[i][k] != " ":
                return False
    return True

      
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if y_end == len(board)-1:
        if x_end-length*d_x+1 == 0 or x_end-length*d_x+1 == len(board)-1:
            if d_y == 0:
                if board[y_end][x_end+1] == " ":
                    return "SEMIOPEN"
                else: 
                    return "CLOSED"
            else:
                return "CLOSED"
        elif d_y==0:
            if x_end == len(board)-1:
                if board[y_end][x_end-length*d_x] == " ":
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
            else:
                if board[y_end][x_end+1] == " " and board[y_end][x_end-length*d_x] == " ":
                    return "OPEN"
                elif board[y_end][x_end+1] != " " and board[y_end][x_end-length*d_x] != " ":
                    return "CLOSED"
                else:
                    return "SEMIOPEN"
        else:
            if board[y_end-length*d_y][x_end-length*d_x] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"

    elif x_end == len(board)-1:
        if y_end-length*d_y+1 == 0:
            if d_x == 0:
                if board[y_end+1][x_end] == " ":
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
            else:
                return "CLOSED"
        elif d_x == 0:
            if y_end == len(board)-1:
                if board[y_end-length*d_y][x_end] == " ":
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
            else:
                if board[y_end+1][x_end] == " " and board[y_end-length*d_y][x_end] == " ":
                    return "OPEN"
                elif board[y_end+1][x_end] != " " and board[y_end-length*d_y][x_end] != " ":
                    return "CLOSED"
                else:
                    return "SEMIOPEN"
        else:
            if board[y_end-length*d_y][x_end-length*d_x] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
    elif x_end == 0:
        if y_end-length*d_y+1 == 0:
            if d_x == 0:
                if board[y_end+1][0] == " ":
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
            else:
                return "CLOSED"
        elif d_x == 0:
            if y_end == len(board)-1:
                if board[y_end-length*d_y][0] == " ": 
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
            else:
                if board[y_end+1][0] == " " and board[y_end-length*d_y][0] == " ":
                    return "OPEN"
                elif board[y_end+1][0] != " " and board[y_end-length*d_y][0] != " ":
                    return "CLOSED"
                else:
                    return "SEMIOPEN"
        else:
            if board[y_end-length*d_y][x_end-length*d_x] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
    elif y_end == 0:
        if x_end-length*d_x+1 == 0:
            if board[0][x_end+1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end == len(board)-1:
            if board[0][x_end-length*d_x] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        else:
            if board[0][x_end+1] == " " and board[0][x_end-length*d_x] == " ":
                return "OPEN"
            elif board[0][x_end+1] != " " and board[0][x_end-length*d_x] != " ":
                return "CLOSED"
            else:
                return "SEMIOPEN"
    else:
        if x_end-length*d_x+1==0 or x_end-length*d_x+1==len(board)-1 or y_end-length*d_y+1==0:
            if board[y_end+d_y][x_end+d_x] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        else:
            if board[y_end+d_y][x_end+d_x] == " " and board[y_end-length*d_y][x_end-length*d_y] == " ":
                return "OPEN"
            elif board[y_end+d_y][x_end+d_x] != " " and board[y_end-length*d_y][x_end-length*d_y] != " ":
                return "CLOSED"
            else:
                return "SEMIOPEN"
            
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    L = []
    L.append(board[y_start][x_start])
    if d_y != 0 and d_x != 0:
        while y_start+d_y != len(board) and x_start+d_x != len(board) and x_start+d_x!= -1:
            L.append(board[y_start+d_y][x_start+d_x])
            y_start += d_y
            x_start += d_x   
    elif d_y == 0 and d_x != 0:
        while x_start+d_x != len(board):
            L.append(board[y_start+d_y][x_start+d_x])
            y_start += d_y
            x_start += d_x 
    else:
        while y_start+d_y != len(board):
            L.append(board[y_start+d_y][x_start+d_x])
            y_start += d_y
            x_start += d_x 
    
    
    count = 0
    semi_count = 0
    open_count = 0
    for i in range(0, len(L)):
        if L[i] == col:
            count += 1
            if count == length:
                if i == len(L)-1 or (L[i+1] != col and L[i+1] !=" "):
                    if L[i-length] == " " and i-length >= 0:
                        semi_count+=1
                elif i-length == -1 or (L[i-length] != " " and L[i-length] != col):
                    if L[i+1] == " " and i+1 <= len(L)-1:
                        semi_count +=1
                elif L[i+1] == " " and i+1 <= len(L)-1 and L[i-length] == " " and i-length >= 0:
                    open_count +=1
        else:
            count = 0
    tuple=(open_count,semi_count)
    return tuple

    
def detect_rows(board, col, length):
    ####CHANGE ME
    open_seq_count, semi_open_seq_count = 0, 0
    semi_count1,semi_count2,semi_count3,semi_count4,semi_count5,semi_count6=0,0,0,0,0,0
    open_count1,open_count2,open_count3,open_count4,open_count5,open_count6=0,0,0,0,0,0
    for i in range (0, len(board)):
        open_count1 += detect_row(board, col, i, 0, length, 0, 1)[0]
        semi_count1 += detect_row(board, col, i, 0, length, 0, 1)[1]
        #start from left bound, horizontal
        open_count2 += detect_row(board, col, 0, i, length, 1, 0)[0]
        semi_count2 += detect_row(board, col, 0, i, length, 1, 0)[1]
        #start from top bound, vertical
        open_count3 += detect_row(board, col, i, 0, length, 1, 1)[0]
        semi_count3 += detect_row(board, col, i, 0, length, 1, 1)[1]
        #start from left bound, 1,1
        open_count4 += detect_row(board, col, 0, i, length, 1, -1)[0]
        semi_count4 += detect_row(board, col, 0, i, length, 1, -1)[1]
        #start from top bound, 1,-1
    for i in range (1,len(board)):   
        open_count5 += detect_row(board, col, 0, i, length, 1, 1)[0]
        semi_count5 += detect_row(board, col, 0, i, length, 1, 1)[1]
        #start from top bound, 1,1
        open_count6 += detect_row(board, col, i, len(board)-1, length, 1, -1)[0]
        semi_count6 += detect_row(board, col, i, len(board)-1, length, 1, -1)[1]
        #start from right bound, 1,-1
    open_seq_count = open_count1+open_count2+open_count3+open_count4+open_count5+open_count6
    semi_open_seq_count = semi_count1+semi_count2+semi_count3+semi_count4+semi_count5+semi_count6
    #all_tuple = (open_seq_count, semi_open_seq_count)
    #return all_tuple
    return open_seq_count, semi_open_seq_count


    
def search_max(board):
    d = {}
    for move_y in range(0,len(board)):
        for move_x in range(0,len(board)):
            if board[move_y][move_x] == " ":
                board[move_y][move_x] = "b"
                d[score(board)] = move_y,move_x
                board[move_y][move_x] = " "
    return d[max(d.keys())]
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_full(board):
    for i in range(0, len(board)):
        for k in range (0, len(board)):
            if board[i][k] == " ":
                return False
    return True

def detect_5(board, col, y_start, x_start, d_y, d_x):
#search for number of sequence of 5 of color col starting with one edge point
    L = []
    L.append(board[y_start][x_start])
    if d_y != 0 and d_x != 0:
        while y_start+d_y != len(board) and x_start+d_x != len(board) and x_start+d_x!= -1:
            L.append(board[y_start+d_y][x_start+d_x])
            y_start += d_y
            x_start += d_x   
    elif d_y == 0 and d_x != 0:
        while x_start+d_x != len(board):
            L.append(board[y_start+d_y][x_start+d_x])
            y_start += d_y
            x_start += d_x 
    else:
        while y_start+d_y != len(board):
            L.append(board[y_start+d_y][x_start+d_x])
            y_start += d_y
            x_start += d_x 
    
    count = 0
    count_5 = 0
    for i in range(0, len(L)):
        if L[i] == col:
            count += 1
            if count == 5:
                if i == len(L)-1:
                    count_5 += 1
                    return count_5
                else:
                    if L[i+1]!=col:
                        count_5+=1
                        return count_5
                 
        else:
            count = 0
    return count_5
        

def detect_5s(board, col):
    count_5_tot = 0
    count_5_a,count_5_b,count_5_c,count_5_d,count_5_e,count_5_f = 0,0,0,0,0,0
    for i in range (0, len(board)):
        count_5_a += detect_5(board, col, i, 0, 0, 1)
        #start from left bound, horizontal
        count_5_b += detect_5(board, col, 0, i, 1, 0)
        #start from top bound, vertical
        count_5_c += detect_5(board, col, i, 0, 1, 1)
        #start from left bound, 1,1
        count_5_d += detect_5(board, col, 0, i, 1, -1)
        #start from top bound, 1,-1
    for i in range (1,len(board)):   
        count_5_e += detect_5(board, col, 0, i, 1, 1)
        #start from top bound, 1,1
        count_5_f += detect_5(board, col, i, len(board)-1, 1, -1)
        #start from right bound, 1,-1
    
    count_5_tot = count_5_a+count_5_b+count_5_c+count_5_d+count_5_e+count_5_f
    return count_5_tot

def is_win(board):
    if detect_5s(board,"b") >= 1:
        return "Black won"
    elif detect_5s(board,"w") >= 1:
        return "White won"
    else:
        if is_full(board) == True:
            return "Draw"
        else:
            return "Continue playing"

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
  
print (easy_testset_for_main_functions())         
if __name__ == '__main__':
    print(play_gomoku(8))
    