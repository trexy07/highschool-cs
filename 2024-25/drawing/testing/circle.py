
rad=3
h=5
k=5
words="launch"
for y in range(15):
    for x in range(15):
        if (x-h)**2 + (y-k)**2 <= rad**2:

            word="  "
            if y==k and h-len(words)/4<= x <= h+len(words)/4 +1/2:
                # print(x)
                # word=f"{x} "

                i= x - h + len(words)//4
                word=f"{x}{i}"   
                # if i*2+2>len(words):
                #     word=words[i*2: i*2+1] + " "
                # else:         
                #     word=words[i*2: i*2+2]           



                # word=words[x-(h//2)-rad/2: x-(h//2)-rad/2+2  ]


            print(f'\x1b[41m{word}\033[0m', end='')
        else:
            print('  ', end='')
    print()