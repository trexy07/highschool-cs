import math
import random
import os

# sizex,sizey=10,10 # plain board
# sizex,sizey=110,20
print(os.get_terminal_size())
sizex,sizey=os.get_terminal_size()
sizex//=2
print(sizex,sizey)


patterns={
    "3x3":          [(-1,-1),( 0,-1),(1,-1),(-1, 0),(0, 0),(1, 0),(-1, 1),(0, 1),(1, 1)],
    "3x3hollow":    [(-1,-1),( 0,-1),(1,-1),(-1, 0),(1, 0),(-1, 1),(0, 1),(1, 1)],
    "3x3plus":      [( 0,-1),(-1, 0),(0, 0),( 1, 0),(0, 1)],
    "3x3x":         [(-1,-1),( 1,-1),(0, 0),(-1, 1),(1, 1)],
    "3x3/":          [(-1,-1),( 0, 0),(1, 1)],
    "3x3\\":         [(-1, 1),( 0, 0),(1,-1)],
    "5x5":          [(-2,-2),(-1,-2),(0,-2),( 1,-2),(2,-2),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(-2,0),(-1,0),(0,0),(1,0),(2,0),(-2,1),(-1,1),(0,1),(1,1),(2,1),(-2,2),(-1,2),(0,2),(1,2),(2,2)],
    "5x5hollow":    [(-2,-2),(-1,-2),(0,-2),( 1,-2),(2,-2),(-2,-1),(2,-1),(-2,0),(2,0),(-2,1),(2,1),(-2,2),(-1,2),(0,2),(1,2),(2,2)],
    "5x5plus":      [(-1,-2),( 0,-2),(1,-2),(-2,-1),(2,-1),(-2,0),(2,0),(-1,1),(0,1),(1,1)],
    "5x5rounded":   [(-1,-2),( 0,-2),(1,-2),(-2,-1),(-1,-1),( 0,-1),( 1,-1),( 2,-1),(-2, 0),(-1, 0),( 0, 0),( 1, 0),( 2, 0),(-2, 1),(-1, 1),( 0, 1),( 1, 1),( 2, 1),(-1, 2),( 0, 2),( 1, 2)],
}

# print(random.random()*2-1)

# wind=(random.random()*2-1,random.random()*2-1)

wind = random.choice(patterns["3x3hollow"])
print(wind)
# wind=(-1,-1)

grid = [ [random.random()*2-1 for i in range(sizex+4)] for j in range(sizey+4) ]

def fancyPrint(grid,buffer=False,wet=True):
    string=""
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            #ESC[48;2;{r};{g};{b}m
            if buffer:
                
                if wet:
                    string+="\033[48;2;%d;%d;%dm" % (
                        0,0,     
                        (grid[y][x]+1) * 127.5      )
                else:
                    if grid[y][x]>0.1:
                        string+="\033[48;2;%d;%d;%dm" % (
                            int((grid[y][x]+1)*127.5),
                            int((grid[y][x]+1)*127.5),
                            int((grid[y][x]+1)*127.5) ) 
                    else:
                        string+="\033[m"
                    # grey/clouds

                string+="  "
                string+="\033[0m"
                
                pass
            else:
                if wet:
                    print("\033[48;2;%d;%d;%dm" % (0,0,int((grid[y][x]+1) *127.5)), end="")
                else:
                    print("\033[48;2;%d;%d;%dm" % (
                        int((grid[y][x]+1)*127.5),
                        int((grid[y][x]+1)*127.5),
                        int((grid[y][x]+1)*127.5) ) 
                        , end = "")
                # print("%1.2f" % grid[x][y], end=" ")
                print("  ", end = "")

                print("\033[0m", end="")
        if buffer:
            string+="\n"
        else:
            print()
    if buffer:
        return string

# fancyPrint(grid)
def perlin(grid,blend=patterns["3x3"],fade=9):

    grid2=[[0 for i in range(sizex)] for j in range(sizey)]

    for x in range(sizex-1):
        for y in range(sizey-1):
            
            val=grid[y][x]
            for dx,dy in blend:
                nx,ny=x+dx+0,y+dy+0
                if nx>=0 and nx<sizex and ny>=0 and ny<sizey:
                    grid2[ny][nx]+=val

    for x in range(sizex):
        for y in range(sizey):
            ### this is difusion/average of the summed values 
            # grid2[y][x]/=9
            # grid2[y][x]/=25
            # grid2[y][x]/=36
            grid2[y][x]/=fade
            # grid2[y][x]*=1.2
    return grid2

def mergePrint(grid1,grid2,buffer=False):
    string=""
    for y in range(len(grid1)):
        for x in range(len(grid1[y])):
            #ESC[48;2;{r};{g};{b}m
            if buffer:
                if grid2[y][x] >0.1:
                    string+="\033[48;2;%d;%d;%dm" % (
                            int((grid2[y][x]+1)*127.5),
                            int((grid2[y][x]+1)*127.5),
                            int((grid2[y][x]+1)*127.5) ) 
                else:
                    string+="\033[48;2;%d;%d;%dm" % (
                        0,0,     
                        (grid1[y][x]+1) * 127.5      )
                string+="  "
                string+="\033[0m"
                # string+="\033[48;2;%d;%d;%dm" % (
                #     int((grid1[y][x]+1)*127.5),
                #     int((grid1[y][x]+1)*127.5),
                #     int((grid1[y][x]+1)*127.5) ) 
                # string+="  "
                # string+="\033[0m"
                
                pass
            else:
                if grid2[y][x] >0.1:
                    print("\033[48;2;%d;%d;%dm" % (
                            int((grid2[y][x]+1)*127.5),
                            int((grid2[y][x]+1)*127.5),
                            int((grid2[y][x]+1)*127.5) ) 
                            , end = "")
                else:
                    print("\033[48;2;%d;%d;%dm" % (0,0,int((grid1[y][x]+1) *127.5)), end="")
                pass
        if buffer:
            string+="\n"
        else:
            print()
    if buffer:
        return string


# fancyPrint(perlin(grid))


def move(grid,wind=(0,0)):

    if wind[0]==-1:
        grid.pop(0)
        # grid.append([random.random()*2-1 for i in range(sizex-1)])
        grid.append([random.random()*2-1 for i in range(sizex)])
    elif wind[0]==1:
        grid.pop()
        # grid.insert(0,[random.random()*2-1 for i in range(sizex-1)])
        grid.insert(0,[random.random()*2-1 for i in range(sizex)])
        pass
    else:
        # wind =0
        pass

    if wind[1]==-1:
        for y in range(sizey+1):
            grid[y].pop(0)
            grid[y].append(random.random()*2-1)
    elif wind[1]==1:
        for y in range(sizey+1):
            grid[y].pop()
            grid[y].insert(0,random.random()*2-1)
    else:
        # wind =0
        pass
    #-1->0, 0->node, 1->1

    # return grid
import time
# import os
while True:
# if True:
    time.sleep(1)

    move(grid,wind)
    # print("\n\n\n")
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print("\x1b[0;0H", end = "")
    # print("\033[H")


    wetNoise=perlin(grid, patterns["5x5rounded"],fade=36) # wet noise 
    string=fancyPrint(wetNoise,buffer=True)

    windNoise=perlin(grid, patterns["3x3"],fade=9) # wind noise
    
    # for row in windNoise:
    #     for point in row:
    #         if point<0:
    #             point=None
            # point=max(point,0)
    string2=fancyPrint(windNoise,buffer=True,wet=False)

    string3 = mergePrint(wetNoise,windNoise,buffer=True)



    os.system('cls' if os.name == 'nt' else 'clear')
    print(string)
    print(string2)
    print(string3)
    # print(windNoise)
    # print(WetNoise)





# either move with wind or bounce the colors

# sea floor + ocean surface + clouds(clearish) +wind
# fog will avoid the game baords

