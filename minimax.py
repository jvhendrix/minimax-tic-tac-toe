class TicTacToe:
    
    def __init__(self):
        
        self.board = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ']
        
        
    def evaluate(self):
        ### Checks for horizontal win
        for row in range(3):
            
            if (self.board[0 + row*3] == self.board[1 + row*3] and self.board[1 + row*3] == self.board[2 + row*1]):
                
                ### Checks for player win
                if (self.board[row] == self.player):
                    return 1
                
                ### Checks for computer win
                elif (self.board[row] == self.computer):
                    return -1
                
        ### Checks for vertical win
        for column in range(3):
            
            if (self.board[0 + column] == self.board[3 + column] and  self.board[6 + column]):
                
                ### Checks for player win
                if (self.board[column] == self.player):
                    return 1
                
                ### Checks for computer win
                elif (self.board[column] == self.computer):
                    return -1
                
        ### Checks for diagonal win
        if (self.board[0] == self.board[4] and self.board[4] == self.board[8]) or \
           (self.board[6] == self.board[4] and self.board[4] == self.board[2]):
               
                if (self.board[4] == self.player):
                    return 1
                
                ### Checks for computer win
                elif (self.board[4] == self.computer):
                    return -1
           
           
                
               
            
        
        
        
    def drawBoard(self):
            
            print("""
          {} | {} | {}
         ---+---+---
          {} | {} | {}
         ---+---+---
          {} | {} | {}
        """.format(*self.board))
    
    player = 'X'
    computer = 'O'
            
        



if __name__ == "__main__":
    
    game = TicTacToe()
    game.drawBoard()

    
    
