def play_turn(game_board: list, x: int, y: int, piece: str):
    
    if x > len(game_board[0]) - 1 or y > len(game_board[0]) - 1:
        return False
    elif x < 0 or y < 0:
        return False
    elif game_board[y][x] != "":
        return False
    else:    
        game_board[y][x] = piece
        return True

if __name__=='__main__':
    #game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    #print(play_turn(game_board, 2, 0, "X"))
    play_turn([['','',''],['','',''],['','','']], 0, 0, 'X')
    #print(game_board)
