'''
Andy Siegel
CSC 110
Project 4
This program has several functions which let the user play 1D chess
'''

def create_board():
    '''
    This function returns an array which symbolizes the 1D chess board
    Args:
        None
    Returns:
        the array of board spaces
    '''
    return ["WKi", "WKn", "WKn", "EMPTY", "EMPTY", "EMPTY", "BKn", "BKn", "BKi"]

def printable_board(board_list):
    '''
    This function returns a string that is the graphical representation of the board given the board_list
    Args:
        board_list: list
    Returns:
        a string that is the graphical representation of the board
    '''
    separator = "+-----------------------------------------------------+"
    board = separator + "\n| " + " | ".join(board_list) + " |\n" + separator
    return board.replace("EMPTY", "   ")
def is_valid_move(board, index, player):
    '''
    This function returns a boolean that says whether the move is valid or not. 
    Args:
        board: list
        index: integer
        player: string ("WHITE" or "BLACK")
    Returns:
        a boolean which states whether the move is valid or not
    '''
    if player.upper() != "WHITE" and player.upper() != "BLACK":
        return False

    if not (0 <= index < len(board)):
        return False

    # player[0] will be "W" or "B"
    if player[0] not in board[index]: 
        return False
    
    return True

def move_king(board, position, direction):
    '''
    This function will move the king until it kills a piece or hits the end of the board.
    Args:
        board: list - the board
        position: integer - position of the king to move 
        direction: string - ("LEFT" or "RIGHT")
    Returns:
        None
    '''
    idx = position
    if direction.lower() == "left":
        idx -= 1
        while idx > 0:
            if board[idx] != "EMPTY":
                board[idx] = board[position]
                board[position] = "EMPTY"
                return
                
            idx -= 1
    elif direction.lower() == "right":
        idx += 1
        while idx < len(board)-1:
            if board[idx] != "EMPTY":
                board[idx] = board[position]
                board[position] = "EMPTY"
                return
            
            idx += 1


def move_knight(board, position, direction):
    '''
    This function will move a knight two spaces in the direction specified
    Args:
        board: list - the board
        position: integer - position of the piece to move 
        direction: string - ("LEFT" or "RIGHT")
    Returns:
        None
    '''
    if direction.lower() == "left" and position - 2 >= 0:
        board[position-2] = board[position]
        board[position] = "EMPTY"
    elif direction.lower() == "right" and position + 2 < len(board):
        board[position+2] = board[position]
        board[position] = "EMPTY"
    

def move(board, position, direction):
    '''
    This function will move the either a knight or king 
    dependent on what piece is specified in the position argument
    Args:
        board: list - the board
        position: integer - position of the piece to move 
        direction: string - ("LEFT" or "RIGHT")
    Returns:
        None
    '''
    player = ""
    if "B" in board[position]:
        player = "Black"  
    else: 
        player = "White"

    # print(board,position,player)
    if not is_valid_move(board, position, player):
        print("Returning because invalid move")
        return
    if "Kn" in board[position]:
        move_knight(board, position, direction)
    elif "Ki" in board[position]:
        move_king(board, position, direction)
    
        
    

def is_game_over(board):
    '''
    This function will determine whether the game is over
    Args:
        board: list - the board
    Returns:
        True or False
    '''
    if "BKi" not in board:
        return True
    elif "WKi" not in board:
        return True
    else:
        return False

def whos_the_winner(board):
    '''
    This function determines if the game is over
    Args:
        board: list - the board
    Returns:
        "White", "Black" or None
    '''
    if is_game_over(board) == False:
        return None
    
    if "WKi" not in board:
        return "Black"
    elif "BKi" not in board:
        return "White"
    
    return None

board = create_board()
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 2, "RIGHT")
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 6, "LEFT")
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 1, "RIGHT")
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 4, "LEFT")
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 0, "RIGHT")
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 7, "LEFT")
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 3, "RIGHT")
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 8, "LEFT")
print( printable_board(board) )

print( whos_the_winner(board) ) # None
move(board, 2, "RIGHT")
print( printable_board(board) )

print( is_game_over(board) ) # True
print( whos_the_winner(board) ) # WHITE