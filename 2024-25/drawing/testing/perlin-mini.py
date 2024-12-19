# this file will translate to java

import math
import random
import os


print(os.get_terminal_size())
sizex,sizey=os.get_terminal_size()
sizex//=2
print(sizex,sizey)

minumumWind=0.05 # -1 to 1, 

patterns={
    "3x3":          [(-1,-1),( 0,-1),(1,-1),(-1, 0),(0, 0),(1, 0),(-1, 1),(0, 1),(1, 1)],
    "3x3hollow":    [(-1,-1),( 0,-1),(1,-1),(-1, 0),(1, 0),(-1, 1),(0, 1),(1, 1)],
    "3x3+":      [( 0,-1),(-1, 0),(0, 0),( 1, 0),(0, 1)],
    "3x3x":         [(-1,-1),( 1,-1),(0, 0),(-1, 1),(1, 1)],
    "3x3/":          [(-1,-1),( 0, 0),(1, 1)],
    "3x3\\":         [(-1, 1),( 0, 0),(1,-1)],
    "5x5":          [(-2,-2),(-1,-2),(0,-2),( 1,-2),(2,-2),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(-2,0),(-1,0),(0,0),(1,0),(2,0),(-2,1),(-1,1),(0,1),(1,1),(2,1),(-2,2),(-1,2),(0,2),(1,2),(2,2)],
    "5x5hollow":    [(-2,-2),(-1,-2),(0,-2),( 1,-2),(2,-2),(-2,-1),(2,-1),(-2,0),(2,0),(-2,1),(2,1),(-2,2),(-1,2),(0,2),(1,2),(2,2)],
    "5x5+":      [(-1,-2),( 0,-2),(1,-2),(-2,-1),(2,-1),(-2,0),(2,0),(-1,1),(0,1),(1,1)],
    "5x5rounded":   [(-1,-2),( 0,-2),(1,-2),(-2,-1),(-1,-1),( 0,-1),( 1,-1),( 2,-1),(-2, 0),(-1, 0),( 0, 0),( 1, 0),( 2, 0),(-2, 1),(-1, 1),( 0, 1),( 1, 1),( 2, 1),(-1, 2),( 0, 2),( 1, 2)],
}

wind = random.choice(patterns["3x3hollow"])
print(wind)
# wind=(-1,-1)

grid = [ [random.random()*2-1 for i in range(sizex+4)] for j in range(sizey+4) ]


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
            grid2[y][x]/=fade
    return grid2

def mergePrint(grid1,grid2,buffer=False):
    string=""
    for y in range(len(grid1)):
        for x in range(len(grid1[y])):
            if buffer:
                if grid2[y][x] >minumumWind:
                    string+="\033[48;2;%d;%d;%dm" % (int((grid2[y][x]+1)*127.5),int((grid2[y][x]+1)*127.5),int((grid2[y][x]+1)*127.5) ) 
                string+="  "
                string+="\033[0m"
            else:
                if grid2[y][x] >minumumWind:
                    print("\033[48;2;%d;%d;%dm" % (int((grid2[y][x]+1)*127.5),int((grid2[y][x]+1)*127.5),int((grid2[y][x]+1)*127.5) ) , end = "")
                else:print("\033[48;2;%d;%d;%dm" % (0,0,int((grid1[y][x]+1) *127.5)), end="")
        if buffer:string+="\n"
        else:print()
    if buffer:return string

def translate(grid,wind=(0,0)):

    if wind[0]==-1:
        grid.pop(0)
        # grid.append([random.random()*2-1 for i in range(sizex-1)])
        grid.append([random.random()*2-1 for i in range(sizex)])
    elif wind[0]==1:
        grid.pop()
        # grid.insert(0,[random.random()*2-1 for i in range(sizex-1)])
        grid.insert(0,[random.random()*2-1 for i in range(sizex)])
        pass


    if wind[1]==-1:
        for y in range(sizey+1):
            grid[y].pop(0)
            grid[y].append(random.random()*2-1)
    elif wind[1]==1:
        for y in range(sizey+1):
            grid[y].pop()
            grid[y].insert(0,random.random()*2-1)


import time
if __name__ == "__main__":
    while True:
        time.sleep(1)
        translate(grid,wind)

        wetNoise=perlin(grid, patterns["5x5rounded"],fade=36) # wet noise 
        # string=fancyPrint(wetNoise,buffer=True)
        windNoise=perlin(grid, patterns["3x3"],fade=9) # wind noise
        # string2=fancyPrint(windNoise,buffer=True,wet=False)
        string3 = mergePrint(wetNoise,windNoise,buffer=True)
        os.system('cls' if os.name == 'nt' else 'clear')
        # print(string)
        # print(string2)
        print(string3)









