from collections import defaultdict, deque
from queue import PriorityQueue
import copy



class GameState():
    end_positions: dict = None
    
    def __init__(self, current_game_map: list[list[int]], empty_position= None, parent_state= None):
        self.parent_state = parent_state
        self.game_map = current_game_map
        
        if self.end_positions == None:
            self.end_positions= self.get_end_positions(len(self.game_map))
            
        if empty_position == None:
            for i in range(len(self.game_map)):
                check = False
                for j in range(len(self.game_map)):
                    
                    if self.game_map[i][j] == 0:
                        self.empty_position = [i, j]
                        check = True
                        break
                if check: break

        else: self.empty_position = empty_position
                
        if parent_state:
            self.path_cost = parent_state.path_cost + 1
        else:
            self.path_cost = 0
            
            
        self.estimated_cost = self.path_cost + self.heuristic_distance()
        
        
    
    def get_possible_move(self):
        possible_move = ['U', 'D', 'L', 'R']
        size = len(self.game_map)
        i, j = self.empty_position
        
        if i == 0: 
            possible_move.remove('U')
        
        elif i == size - 1: possible_move.remove('D')
        
        if j == 0: possible_move.remove('L')
        
        elif j == size - 1: possible_move.remove('R')
        
        return possible_move
        
    
    def get_next_states(self) -> list:
        
        possible_move = self.get_possible_move()
        next_states = []
        i, j = self.empty_position
        
        for move in possible_move:
            next_game_map = copy.deepcopy(self.game_map)
            next_i, next_j = i, j
            if move == 'U':
                next_game_map[i - 1][j], next_game_map[i][j] = next_game_map[i][j], next_game_map[i - 1][j]
                next_i -= 1
            elif move == 'D':
                next_game_map[i + 1][j], next_game_map[i][j] = next_game_map[i][j], next_game_map[i + 1][j]
                next_i += 1
            elif move == 'L':
                next_game_map[i][j - 1], next_game_map[i][j] = next_game_map[i][j], next_game_map[i][j - 1]
                next_j -= 1
            else:
                next_game_map[i][j + 1], next_game_map[i][j] = next_game_map[i][j], next_game_map[i][j + 1]
                next_j += 1
            next_states.append(GameState(next_game_map, [next_i, next_j], self))
            
        return next_states
                  
    def is_end_game(self):
        for key, value in self.get_current_positions().items():
            if value != self.end_positions[key]:
                return False
        return True
    
    
    def manhattan_distance(self, pos1: list[int], pos2: list[int]):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def heuristic_distance(self):
        current_positions: dict = self.get_current_positions()
        
        distance = 0
        for key, value in current_positions.items():
           
            distance += self.manhattan_distance(value, self.end_positions[key])
        return distance

    @staticmethod
    def get_end_positions(size: int) ->dict:
        true_position = {}
        # for i in range(size * size):
        #     row_idx = (i) // size
        #     col_idx = (i) % szie
        #     true_position[i] = [row_idx, col_idx]
        for i in range(1, size * size):
            row_idx = (i - 1) // size
            col_idx = (i - 1) % size
            true_position[i] = [row_idx, col_idx]
        true_position[0] = [size - 1, size - 1]
        return true_position
    
    def get_current_positions(self) ->dict:
        positions = {} 
        for i in range(size):
            for j in range(size):
                positions[self.game_map[i][j]] = [i, j]
            
        return positions
    def encode_to_string(self):
        res = ''
        for i in self.game_map:
            for j in i:
                res += str(j)
        
        return res
    
    
class NPuzzle():
    
    def __init__(self, size: int= None, game_map= None) -> None:
        if not size:
            
            self.size = int(input('Nhap kich thuoc'))
        
        if not game_map:
            game_map = self.get_input()
        
        # GameState.end_positions = GameState.get_end_positions(size= size)
        
        if not self.isSolvable(size, game_map):
            print('Khong the giai, vui long chon: ')
            print('Nhap lai(0) - ket thuc tro choi (1)')
            n = int(input())
            if n == 0: 
                game_map = self.get_input()       
            else: exit()
            
            
        self.game_map = game_map
        
        for i in range(size):
            for j in range(size):
                if self.game_map[i][j] == 0:
                    self.empty_position = [i, j]
                    break
        
    
    def getInvCount(self, size, arr):
        arr1=[]
        for y in arr:
            for x in y:
                arr1.append(x)
        arr=arr1
        inv_count = 0
        for i in range(size* size - 1):
            for j in range(i + 1,size * size):
                if (arr[j] and arr[i] and arr[i] > arr[j]):
                    inv_count+=1
            
        return inv_count


    def isSolvable(self, size, game_map)-> bool:
        # Count inversions in given puzzle
        invCount = self.getInvCount(size, game_map)

        # If grid is odd, return true if inversion
        # count is even.
        if (size & 1):
            return ~(invCount & 1)
        
        else:    # grid is even
            pos = self.findXPosition(size, game_map)
            if (pos & 1):
                return ~(invCount & 1)
            else:
                return invCount & 1
            

    def findXPosition(self, size, game_map):
        # start from bottom-right corner of matrix
        for i in range(size - 1,-1,-1):
            for j in range(size - 1,-1,-1):
                if (game_map[i][j] == 0):
                    return size - i
        
    def get_input(self):
        
        game_map = []
        print('Nhap bai toan')
        for i in range(size):
            input_ = input().split(sep = ' ', maxsplit= size)
            input_ = list(map(int, input_))
            game_map.append(input_)
            
        return game_map
    
    def solve_game(self):
        explored = []
        cnt = 0 
        
        start_state = GameState(self.game_map, empty_position= self.empty_position)
        
        if start_state.is_end_game():
            return self.synthesis_solution(start_state)
        
        pq = PriorityQueue()
        pq.put((start_state.estimated_cost, cnt, start_state))
        
        
        while not pq.empty():
            node = pq.get()
            current_state: GameState = node[2]
            
            
            if current_state.is_end_game(): 
                return self.synthesis_solution(current_state)
            
            explored.append(current_state.encode_to_string())
            
            for next in current_state.get_next_states():
                if next.encode_to_string() not in explored:
                    cnt += 1
                    # print(next.estimated_cost, ': ', next.encode_to_string())
                    # explored.append(next.estimated_cost)
                    pq.put((next.estimated_cost, cnt, next))
            
        
        return 
    
    def synthesis_solution(self, state: GameState):
        res = 0
        stack = deque([state.game_map])
        while state.parent_state != None:
            state = state.parent_state
            stack.append(state.game_map)
            res += 1
        
        while len(stack) != 0:
            current_game_map = stack.pop()
            self.print_game_map(current_game_map)
            if len(stack) == 0: continue
            print('\t|')
            print('\t\/')
        return res
    def print_game_map(self, game_map):
        print('-------------')
        for row in game_map:
            print('|', end= ' ')
            for ele in row:
                print(f'{ele} |', end= ' ')
            print('')
            print('-------------')

    
    
    
    
        
if __name__ == '__main__':
    size = 4
    puzzle = [[0, 4, 2, 7], [5, 13, 1, 11], [8, 6, 15, 3], [9, 12, 10, 14]]
    # puzzle = [[1, 2, 3, 3],
    #     [4, 5, 6, 7],
    #     [8, 9, 10, 11],
    #     [12, 13, 14, 15]]
    
    
    game = NPuzzle(size= size, game_map= puzzle)
    print(f'Min move: {game.solve_game()}')
    
    