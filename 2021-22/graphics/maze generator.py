mazewalls=Group()
class Cell:
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    def __init__(self,x,y):
        self.x,self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}
    def has_all_walls(self):
        return all(self.walls.values())
    def knock_down_wall(self,other,wall):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False
class Maze:
    def __init__(self,nx,ny,ix=0,iy=0):
        self.nx,self.ny=nx,ny
        self.ix,self.iy=ix,iy
        self.maze_map=[[Cell(x,y) for y in range(ny)] for x in range(nx)]
    def cell_at(self,x,y):
        return self.maze_map[x][y]
    def __str__(self):
        maze_rows=['--+'* self.nx * 1]
        for y in range(self.ny):
            maze_row=['T']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['E']:
                    maze_row.append('  |')
                else:
                    maze_row.append('   ')
            maze_rows.append(''.join(maze_row))
            maze_row=['dow']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['S']:
                    maze_row.append('--+')
                else:
                    maze_row.append('  +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)
    def find_valid_neighbours(self,cell):
        delta=[('W',(-1,0)),
            ('E',(1,0)),
            ('S',(0,1)),
            ('N',(0,-1))]
        neighbours=[]
        for direction, (dx,dy) in delta:
            x2,y2=cell.x+dx,cell.y+dy
            if(0<= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour=self.cell_at(x2,y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction,neighbour))
        return neighbours
    def make_maze(self):
        n=self.nx*self.ny
        cell_stack=[]
        current_cell=self.cell_at(self.ix,self.iy)
        nv=1
        while nv<n:
            neighbours=self.find_valid_neighbours(current_cell)
            if not neighbours:
                current_cell=cell_stack.pop()
                continue
            direction,next_cell=choice(neighbours)
            current_cell.knock_down_wall(next_cell,direction)
            cell_stack.append(current_cell)
            current_cell=next_cell
            nv+=1
nx,ny=9,9
ix,iy=0,0
maze=Maze(nx,ny,ix,iy)
maze.make_maze()
print(maze)
### everything above this line is from https://scipython.com/blog/making-a-maze/


app.x1=0
app.y1=0
app.x2=-400/nx
app.y2=0
app.text=0
for i in range(rounded(len(str(maze))/3)+1):
    if '--+'==str(maze)[app.text*3:(app.text+1)*3]:
        app.x1+=400/nx
        app.x2+=400/nx
        app.text+=1
        mazewalls.add(Line(app.x1,app.y1,app.x2,app.y2))
    if'  +'==str(maze)[app.text*3:(app.text+1)*3]:
        app.x1+=400/nx
        app.x2+=400/nx
        app.text+=1
    if'   '==str(maze)[app.text*3-1:(app.text+1)*3-1]:
        app.x1+=400/nx
        app.x2+=400/nx
        app.text+=1
    if '  |'==str(maze)[app.text*3-1:(app.text+1)*3-1]:
        app.x1+=400/nx
        app.x2+=400/nx
        mazewalls.add(Line(app.x1,app.y1,app.x2,app.y2+400/ny))
        app.text+=1
    if 'T' in str(maze)[app.text*3-1:(app.text+1)*3-1]:
        app.x1=0
        app.x2=0
        app.text+=1
    if  'dow'==str(maze)[app.text*3:(app.text+1)*3]:
        app.y1+=400/ny
        app.y2+=400/ny
        app.x1=0
        app.x2=-400/nx
        app.text+=1
    print(app.text)