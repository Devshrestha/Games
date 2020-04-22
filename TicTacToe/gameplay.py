



class game:
    def __init__(self,mode,p1):
        #self.grid=[['1','2','3'],['4','5','6'],['7','8','9']]
        self.grid = [['  ','  ','  '],['  ','  ','  '],['  ','  ','  ']]
        self.playing=True
        self.turn=1
        self.mode=mode
        
        if p1==1:
            self.marker=['','X','O']
        else:
            self.marker=['','O','X']

    def grid_values(self):
        return self.grid

    def update(self,j,i):
        if self.turn%2==0:
            self.grid[j][i]="X"
        else:
            self.grid[j][i]="O"
        self.turn+=1
    
    def status(self):
        # try to keep message len between 8 to 12
        stat="Making game"
        return stat
    
    def check_winner(self):
        playing = True
