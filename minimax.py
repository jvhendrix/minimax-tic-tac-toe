### Main game class
class TicTacToe:
            
    def __init__(self):
        
        self.player = 'X'
        self.computer = 'O'
        self.player_turn = True
        
        self.board = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ']
        
    ### Evaluate values at the final state of the game  
    def evaluate(self):
        
        ### Checks for horizontal win
        for row in range(3):
            
            if ((self.board[0 + row*3] == self.board[1 + row*3]) and (self.board[1 + row*3] == self.board[2 + row*3])):
                
                ### Checks for player/computer win
                if (self.board[row*3] == self.player):
                    return 1
                
                elif (self.board[row*3] == self.computer):
                    return -1
                
        ### Checks for vertical win
        for column in range(3):
            
            if (self.board[0 + column] == self.board[3 + column] and self.board[3 + column] == self.board[6 + column]):
                
                ### Checks for player/computer win
                if (self.board[column] == self.player):
                    return 1
                
                elif (self.board[column] == self.computer):
                    return -1
                
        ### Checks for diagonal win
        if (self.board[0] == self.board[4] and self.board[4] == self.board[8]) or \
           (self.board[6] == self.board[4] and self.board[4] == self.board[2]):
               
                ### Checks for player/computer win
                if (self.board[4] == self.player):
                    return 1
            
                elif (self.board[4] == self.computer):
                    return -1
        return 0
    
    ### Set board    
    def setBoard(self, board):
        
        self.board = board
    
    ### Check if move is valid       
    def isValidMove(self, value):
        
        if (self.board[value] == ' '):   
            return True
        
        else:
            return False
        
    ### Make a valid move for the player
    def makeMove(self):
        
        while True:
            move = int(input("\nEnter a move between 0 and 8\n"))
            if (move >= 0) and (move <= 8) and (self.isValidMove(move)):
                
                if (self.player_turn):
                    self.board[move] = self.player
                else:
                    self.board[move] = self.computer
                    
                self.player_turn = not self.player_turn
                break
            
            print("\nPlease enter a valid move! Your options are:")
            
            for i in range(9):
                if self.board[i] == ' ':
                    print(str(i))
            
            
    ### Get which level the game is in (starts at 9, each move the level gets decreased by 1)    
    def getDepth(self):
        return self.board.count(' ')
    
    ### Check if a win condition has been achieved
    def checkWin(self):
        return self.evaluate()
    
    ### Print game instructions
    def printInstructions(self):
        
        print("\n=============================")
        print("Welcome to Minimax TicTacToe!")
        print("=============================\n")
        print("You are going to play against the minimax AI algorithm, which is used to find")
        print("the best possible move, assuming your opponent will also play the best move")
        print("You are going to be playing as " + "'X' " + "while the computer will play as " + "'O'")
        print("The board is mapped as follows:")
        print("""
          0 | 1 | 2
         ---+---+---
          3 | 4 | 5
         ---+---+---
          6 | 7 | 8
        """)
        print("The game will now start, good luck!!!")
        print("=========================================\n")
            
    
    ### Draw a fancy board
    def drawBoard(self):
            
            print("""
          {} | {} | {}
         ---+---+---
          {} | {} | {}
         ---+---+---
          {} | {} | {}
        """.format(*self.board))
    

### Tree class
### All the possible variations of the game are stored in this class 
### Each node is a different game state
### The children of a node are the neighbor game states of the parent node (with only one move of difference)
### Each node has its own value, which will be the the best/worst evaluated leaf of that node (depends on whose turn it is)       
class Node:
    
    def __init__(self, game_state :TicTacToe):
        self.value = 0
        self.children = []
        self.game_state = game_state
    
    ### Set node value    
    def setValue(self, value):
        self.value = value
    ### Get node value    
    def getValue(self):
        return self.value

    ### Add one layer of children to the node (neighbor game states)
    def addChildren(self):
        self.children = []
        
        for i in range(9):
            
            new_board = self.game_state.board.copy()
            
            if (self.game_state.isValidMove(i)):
                
                if (self.game_state.player_turn):
                    new_board[i] = self.game_state.player
                    
                else:
                    new_board[i] = self.game_state.computer
                
                new_game = TicTacToe()
                new_game.player_turn = not self.game_state.player_turn
                new_game.board = new_board
                new_node = Node(new_game)
                
                self.children.append(new_node)
        
### Recursive algorithm
### Will choose the best move, considering the opponent will also play the best move
### The player win has value +1, the computer win has value -1 and a draw has value 0
### So the computer will choose the minimal value neighbor children, considering the
### player will always try to choose the maximal value neighbor
def minimax(root :Node, depth, is_max):
    
    ### Get evaluation of current game state
    score = root.game_state.evaluate() 
    
    ### Base case of recursion
    ### Checks if the game is in a final state
    if (score != 0) or (depth == 0):
        root.setValue(score)
        return score
    
    ### If not in final state, add children to current node
    root.addChildren()
     
    ### Check if minimize or maximize  
    if (is_max):
        
        ### if maximize
        max_val = -10
        
        ### choose child with maximal value
        for child in root.children:
            max_val = max(max_val, minimax(child, depth-1, False))
            
        root.setValue(max_val)
        return max_val
    
    else:
        
        ### if minimize
        min_val = 10
        
        ### choose child with minimal value
        for child in root.children:
            
            min_val = min(min_val, minimax(child, depth-1, True))
            
        root.setValue(min_val)
        return min_val


if __name__ == "__main__":
    
    game = TicTacToe()
    root = Node(game)
    
    game.printInstructions()
    
    ### Game loop
    while True:
        
        if game.player_turn:
            
            ### player turn
            game.makeMove()
            ### update game state in tree 
            root.game_state = game
            
            print("==============================")
            print("You played: ")
            game.drawBoard()
            print("==============================")
            
            ### check for win/draw
            win_condition = game.checkWin()
            if win_condition == 1:
                
                print("YOU WIN!")
                break
                        
            elif ' ' not in game.board:
                print("\nDRAW! :/\n")
                break
            
        else:
            
            ### computer turn, minimax to get values of nodes (computer is trying to minimize)
            minimax(root, game.getDepth(), False)
            
            best_score = 10
            best_node = None
            
            ### choosing the child with minimal value
            for child in root.children:
                
                if child.getValue() < best_score:
                    
                    best_score = child.getValue()
                    best_node = child
            
            ### updating game state and tree        
            root = best_node
            game.board = best_node.game_state.board
            game.player_turn = True
            
            print("The computer played: ")
            game.drawBoard()
            print("==============================")
            
            ### check for computer win
            win_condition = game.checkWin()
            if win_condition == -1:
                
                print("\nYOU LOSE! :(\n")
                break
            
            
            

