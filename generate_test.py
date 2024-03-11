from random import randint

size = 5
move_step = 60


def get_possible_move(i , j):
    possible_move = ['U', 'D', 'L', 'R']
    
    if i == 0: 
        possible_move.remove('U')
    
    elif i == size - 1: possible_move.remove('D')
    
    if j == 0: possible_move.remove('L')
    
    elif j == size - 1: possible_move.remove('R')
    
    return possible_move

def get_end_game_first(size: int) ->dict:
       
    game_map = [[0] * size for i in range(size)]
    for i in range(size * size):
        row_idx = (i ) // size
        col_idx = (i ) % size
        game_map[row_idx][col_idx] = i
       
    # game_map[size - 1][size -1] = 0
    
    return game_map
def get_end_game_last(size: int) ->dict:
   
    game_map = [[0] * size for i in range(size)]
    for i in range(1, size * size):
        row_idx = (i - 1) // size
        col_idx = (i - 1) % size
        game_map[row_idx][col_idx] = i
       
    game_map[size - 1][size -1] = 0
    
    return game_map

def find_empty_position(size, game_map):
        # start from bottom-right corner of matrix
        for i in range(size - 1,-1,-1):
            for j in range(size - 1,-1,-1):
                if (game_map[i][j] == 0):
                    return [i, j]

game_map = get_end_game_first(size)
# print(game_map)
# exit()
prev_move = ''
for i in range(move_step):
    i, j = find_empty_position(size= size, game_map= game_map)
    possible_move = get_possible_move(i , j)
    
    try:
        if  prev_move == 'U':
            possible_move.remove('D')
        elif prev_move == 'D':
            possible_move.remove('U')
            
        elif prev_move == 'L':
            possible_move.remove('R')
            
        else:
            possible_move.remove('L')
            
    except Exception:
        pass
    
    move = possible_move[randint(0, len(possible_move) - 1)]
    prev_move = move
    if  move == 'U':
        game_map[i - 1][j], game_map[i][j] = game_map[i][j], game_map[i - 1][j]
    elif move == 'D':
        game_map[i + 1][j], game_map[i][j] = game_map[i][j], game_map[i + 1][j]
        
    elif move == 'L':
        game_map[i][j - 1], game_map[i][j] = game_map[i][j], game_map[i][j - 1]
        
    else:
        game_map[i][j + 1], game_map[i][j] = game_map[i][j], game_map[i][j + 1]
            
        
        
print(game_map)
    

