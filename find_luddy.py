# find_luddy.py : a simple maze solver
#
# Submitted by : Amogh Batwal

import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, d, row, col):
    # Adding the directions N/S/W/E as per the move direction in coordinates
    
    # Start of citation -Idea for the below line in code was taken from
    # "https://stackoverflow.com/questions/16641119/why-does-append-always-return-none-in-python"
    moves = ((row+1,col, d + ["S"]), (row-1,col,d + ['N']), (row,col-1,d + ['W']), (row,col+1,d + ['E']))
    # End of citation
    
    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
def search1(IUB_map):
    # Find my start position
    you_loc = [(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    direction = []           # List 'direction' created to keep track of the path which is followed along the shortest path
    visited = [(you_loc)]      # List 'visited' created to keep track of the visited nodes during traversal
    fringe = [(you_loc,0,direction)]   # Maintaining a fringe which stores - the starting location, current distance travelled and 
                                       # direction at starting point(which will be an empty list)
    
    while fringe:
        (curr_move, curr_dist, d) = fringe.pop(0)   # Implementing BFS: Popping out the First element in the fringe (FIFO)
        for move in moves(IUB_map, d, *curr_move):  # Sending (the map, direction popped and current location) to the 'moves' function
            valid_moves  = (move[0],move[1])    # Capturing each valid move in a tuple for future processing
            if ((move[0],move[1]) not in visited):  # Checking if the move is already visited in past
                if IUB_map[move[0]][move[1]] == "@":           # If goal is found, return the distance travelled and the directions taken to reach the goal
                    return curr_dist+1, move[-1]
                else:
                    visited.append(valid_moves)     # If goal is not found, add the valid moves to visited 
                    fringe.append(((move[0],move[1]), curr_dist + 1, move[2]))   # Add the queue with the visited move, distance taken to 
                                                                                 # reach that valid move and direction in which move was taken
    return "Inf"    # If no path is found between # and @, return "Inf"

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])    # Accept first user input (map) while running the python code
    print("Shhhh... quiet while I navigate!")
    solution = search1(IUB_map)
    print("Here's the solution I found:")
    if solution == "Inf":   # If function returns with no path, provide output as Inf
        print(solution)
    else:     # If a path is found from # to @, provide the no. of the steps taken via the shortest path along with its path to reach the goal state 
        # Start of citation - Idea for the below line in code was taken from
        # "https://stackoverflow.com/questions/4166641/how-can-i-optimally-concat-a-list-of-chars-to-a-string"
        print(solution[0], ''.join(solution[-1]))
        # End of citation
