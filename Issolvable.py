
def getInvCount(size, arr):
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


def isSolvable(size, game_map)-> bool:
    # Count inversions in given puzzle
    invCount = getInvCount(size, game_map)

    # If grid is odd, return true if inversion
    # count is even.
    if (size & 1):
        return ~(invCount & 1)
    
    else:    # grid is even
        pos = findXPosition(size, game_map)
        if (pos & 1):
            return ~(invCount & 1)
        else:
            return invCount & 1
        

def findXPosition(size, game_map):
    # start from bottom-right corner of matrix
    for i in range(size - 1,-1,-1):
        for j in range(size - 1,-1,-1):
            if (game_map[i][j] == 0):
                return size - i