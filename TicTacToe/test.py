from math import inf as infinity
from gameplay import game


app=game(1,1)
scores={'X':1,'O':-1,'tie':0}

def minimax(board,depth,isMaximizing):
    global scores
    app.check_winner()
    
    if app.winner != None:
        score=scores[app.winner]
        return score
    if isMaximizing:
        bestscore = -infinity
        for i in range(3):
            for j in range(3): 
                if app.grid[i][j]=='  ':
                    app.grid[i][j]="X"
                    score = minimax(app.grid,depth+1,False)
                    app.grid[i][j]="  "
                    bestscore=max(bestscore,score)
                        
        
        return bestscore
    else:
        bestscore = infinity
        for i in range(3):
            for j in range(3): 
                if app.grid[i][j]=='  ':
                    app.grid[i][j]="O"
                    score = minimax(app.grid,depth+1,True)
                    app.grid[i][j]="  "
                    bestscore=min(bestscore,score)
                       
        
        return bestscore
    

def printing(bo):
    print(f"   {app.grid[0][0]}  |   {app.grid[1][0]}    |   {app.grid[2][0]} ")
    print('__________________')
    print(f"   {app.grid[0][1]}  |   {app.grid[1][1]}    |   {app.grid[2][1]} ")
    print('__________________')
    print(f"   {app.grid[0][2]}  |   {app.grid[1][2]}    |   {app.grid[2][2]} \n\n")


def best_play():
    #global app.grid
    bestscore = -infinity
    for i in range(3):
        for j in range(3): 
            if app.grid[i][j]=='  ':
                app.grid[i][j]="X"
                score = minimax(app.grid,0,False)
                app.grid[i][j]="  "
                if score>bestscore:
                    bestscore=score
                    best_move=[i,j]

    #ai move
    app.grid[best_move[0]][best_move[1]]='X'        
    


def player_move():
    #global app.grid
    while True:
        a=int(input('row'))
        b=int(input('column'))
        if app.grid[a][b]=='  ':
            app.grid[a][b]='O'
            break


for x in range(10):
    print(app.winner)
    best_play()
    printing(app.grid)
    player_move()
    printing(app.grid)
