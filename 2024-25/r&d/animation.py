# -*- coding: utf-8 -*-

light="🟀🟄🟉✶✷✹"
heavy="🟂✦🟊🟌✸"
pinwheel="🟃🟇✯🟍✵"#🟔"

import os
import time
os.system("")# fixes windows cmd?

def get_frame(frame):
    char=heavy[frame//2]
    if frame%2==0:
        return("\033[43;31m"+char+" \033[0m")
    else:
        return("\033[33;41m"+char+" \033[0m")

def explode():
    for i in range(5):
        char=heavy[i]
        print("\033[43;31m"+char+" \033[0m")
        time.sleep(.15)
        os.system("clear")

        char=heavy[i]
        print("\033[33;41m"+char+" \033[0m")
        time.sleep(.15)
        os.system("clear")
# print(" \U0001F1FA\U0001F1F8 🏴‍☠️🏳️‍🌈🏴")
#"💥💣✈"
# print(("🌊"*10 +"\n")*10)
# print(("🌫 "*10 +"\n")*10)
exposion_frames=10

x,y=6,5
for i in range(x+y+2 + exposion_frames + 1):
    os.system("clear")
    if i <=10:
        print("  "*i + "✈")
    else:
        print("")

    if i==x:
        print("  "*i + "💣")
    else:
        print("")
    grid =[["☁️ " if i < 10 else "\n" for i in range(11)] for j in range(10)]
    # print( "\033[44m" +   (" " + "☁️ "*10 +" \n")*10  + "\033[0m")  # clouds on blue background
    
    y2 = i-x
    print(y2)
    if 0<y2<y+2:
        grid[y2-1][x]="💣"
    elif y<y2<y+exposion_frames+2:
        # grid[y2][x]="💥"
        grid[y][x]=get_frame(y2-y-2)
        # explode()
    elif y2==y+exposion_frames+2:# final frame
        grid[y][x]="💥" # hit 
        grid[y][x]="🌊"   #or miss

    
    print("".join(["".join(row) for row in grid]))

    time.sleep(.5)
    

