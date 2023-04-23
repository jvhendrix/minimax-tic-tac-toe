import copy
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
            
            if (self.board[0 + row*3] == self.board[1 + row*3] and self.board[1 + row*3] == self.board[2 + row*1]):
                
                ### Checks for player/computer win
                if (self.board[row] == self.player):
                    return 1
                
                elif (self.board[row] == self.computer):
                    return -1
                
        ### Checks for vertical win
        for column in range(3):
            
            if (self.board[0 + column] == self.board[3 + column] and  self.board[6 + column]):
                
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
   
        
    def setBoard(self, board):
        
        self.board = board
           
    def isValidMove(self, value):
        
        if (self.board[value] == ' '):   
            return True
        
        else:
            return False
    def makeMove(self):
        
        while True:
            move = int(input("Enter a move between 0 and 8"))
            if (move >= 0) and (move <= 8) and (self.isValidMove(move)):
                self.board[move] = self.player
                self.player_turn = False
                break
        
    def getDepth(self):
        return self.board.count(' ')
      
    def drawBoard(self):
            
            print("""
          {} | {} | {}
         ---+---+---
          {} | {} | {}
         ---+---+---
          {} | {} | {}
        """.format(*self.board))
    
        
class Node:
    
    def __init__(self, game_state :TicTacToe):
        self.value = 0
        self.children = []
        self.game_state = game_state
        
    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value

    def addChildren(self):
        
        for i in range(9):
            copy_game_state = copy.deepcopy(self.game_state)
            new_node = Node(copy_game_state)
            
            if (self.game_state.isValidMove(i)):
                
                if (self.game_state.player_turn):
                    new_node.game_state.board[i] = new_node.game_state.player
                    new_node.game_state.player_turn = False
                    
                else:
                    new_node.game_state.board[i] = new_node.game_state.computer
                    new_node.game_state.player_turn = True
                
                self.children.append(new_node)
        

def minimax(root :Node, depth, is_max):
    
    score = root.game_state.evaluate()
    root.addChildren()
     
    if (score != 0) or (depth == 0):
        return score
    
    if (is_max):
        
        max_val = -10
        for child in root.children:
            
            max_val = max(max_val, minimax(child, depth-1, False))
            return max_val
    else:
        
        min_val = 10
        for child in root.children:
            
            min_val = min(min_val, minimax(child, depth-1, True))
            return min_val


if __name__ == "__main__":
    
    game = TicTacToe()
    root = Node(game)
    
    while True:
        if (game.player_turn):
            game.makeMove()
            game.drawBoard()
        else:
            minimax(root, game.getDepth(), True)
            
            best_value = -2
            next_node = None
            
            for child in root.children:
                if child.getValue() > best_value:
                    best_value = child.getValue()
                    next_node = child
            
            root = next_node
            game = root.game_state
            game.player_turn = True
            game.drawBoard()

    
    
