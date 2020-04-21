



class game:
    def __init__(self,mode,p1):
        self.grid = ['  ']*9
        self.playing=True
        self.move=1
        self.mode=mode
        
        if p1==1:
            self.marker=['','X','O']
        else:
            self.marker=['','O','X']

    def grid_values(self):
        return self.grid

    def update(self):
        for a in range(len(self.grid)):
            if a%2==0:
                self.grid[a]="X"
            else:
                self.grid[a]="O"
    
    def check_winner(self):
        playing = True
