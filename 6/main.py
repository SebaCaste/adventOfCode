
def turn_right(current_direction,directions):
    return (current_direction + 1) % len(directions)   
def create_map(s:str)->int:
    full_map=(s.split('\n'))
    full_map = [list(row) for row in full_map]
    directions=['<','^','>','v']
    current_direction=-1
    height=len(full_map)
    width=len(full_map[0])
    pos_height,pos_width=-1,-1
    for i in range(height):
        for j in range(width):
            if full_map[i][j] in directions:
                pos_height,pos_width=i,j
                current_direction=directions.index(full_map[i][j])
    
    if directions[current_direction]=='<':
        next_step_y,next_step_x=pos_height,pos_width-1
    if directions[current_direction]=='^':
        next_step_y,next_step_x=pos_height-1,pos_width
    if directions[current_direction]=='>':
        next_step_y,next_step_x=pos_height,pos_width+1
    if directions[current_direction]=='v':
        next_step_y,next_step_x=pos_height+1,pos_width
    while(next_step_y<height and next_step_y>=0 and next_step_x>=0 and next_step_x<width):
        if(full_map[next_step_y][next_step_x]=='#'):
            current_direction=turn_right(current_direction,directions)
        else:
            pos_height,pos_width=next_step_y,next_step_x
            print(full_map[pos_height][pos_width])
            full_map[pos_height][pos_width]='X'
        if directions[current_direction]=='<':
            next_step_y,next_step_x=pos_height,pos_width-1
        if directions[current_direction]=='^':
            next_step_y,next_step_x=pos_height-1,pos_width
        if directions[current_direction]=='>':
            next_step_y,next_step_x=pos_height,pos_width+1
        if directions[current_direction]=='v':
            next_step_y,next_step_x=pos_height+1,pos_width
    for row in full_map:
        print(''.join(row))
    count=0
    for i in range(height):
        for j in range(width):
            if full_map[i][j] in "X":
                count+=1
    return count

def loops(s:str):
    full_map=(s.split('\n'))
    full_map = [list(row) for row in full_map]
    directions=['<','^','>','v']
    current_direction=-1
    height=len(full_map)
    width=len(full_map[0])
    pos_height,pos_width=-1,-1
    for i in range(height):
        for j in range(width):
            if full_map[i][j] in directions:
                pos_height,pos_width=i,j
                current_direction=directions.index(full_map[i][j])
    
    if directions[current_direction]=='<':
        next_step_y,next_step_x=pos_height,pos_width-1
    if directions[current_direction]=='^':
        next_step_y,next_step_x=pos_height-1,pos_width
    if directions[current_direction]=='>':
        next_step_y,next_step_x=pos_height,pos_width+1
    if directions[current_direction]=='v':
        next_step_y,next_step_x=pos_height+1,pos_width
    while(next_step_y<height and next_step_y>=0 and next_step_x>=0 and next_step_x<width):
        if(full_map[next_step_y][next_step_x]=='#'):
            current_direction=turn_right(current_direction,directions)
        else:
            pos_height,pos_width=next_step_y,next_step_x

            if full_map[pos_height][pos_width]=='.':
                full_map[pos_height][pos_width]=directions[current_direction]
            else:
                full_map[pos_height][pos_width]=f"{directions[current_direction]}"
        if directions[current_direction]=='<':
            next_step_y,next_step_x=pos_height,pos_width-1
        if directions[current_direction]=='^':
            next_step_y,next_step_x=pos_height-1,pos_width
        if directions[current_direction]=='>':
            next_step_y,next_step_x=pos_height,pos_width+1
        if directions[current_direction]=='v':
            next_step_y,next_step_x=pos_height+1,pos_width
    return '\n'.join(''.join(row) for row in full_map)

def is_looping(s:str,Y,X)->bool:
    full_map=(s.split('\n'))
    full_map = [list(row) for row in full_map]
    directions=['<','^','>','v']
    current_direction=-1
    height=len(full_map)
    width=len(full_map[0])

    full_map[Y][X]='#'

    pos_height,pos_width=-1,-1
    for i in range(height):
        for j in range(width):
            if full_map[i][j] in directions:
                pos_height,pos_width=i,j
                current_direction=directions.index(full_map[i][j])
    
    if directions[current_direction]=='<':
        next_step_y,next_step_x=pos_height,pos_width-1
    if directions[current_direction]=='^':
        next_step_y,next_step_x=pos_height-1,pos_width
    if directions[current_direction]=='>':
        next_step_y,next_step_x=pos_height,pos_width+1
    if directions[current_direction]=='v':
        next_step_y,next_step_x=pos_height+1,pos_width
    while(next_step_y<height and next_step_y>=0 and next_step_x>=0 and next_step_x<width):
        
        if(full_map[next_step_y][next_step_x]==directions[current_direction]):
            return True
        elif(full_map[next_step_y][next_step_x]=='#'):
            current_direction=turn_right(current_direction,directions)
        else:
            pos_height,pos_width=next_step_y,next_step_x

            full_map[pos_height][pos_width]=directions[current_direction]
        if directions[current_direction]=='<':
            next_step_y,next_step_x=pos_height,pos_width-1
        if directions[current_direction]=='^':
            next_step_y,next_step_x=pos_height-1,pos_width
        if directions[current_direction]=='>':
            next_step_y,next_step_x=pos_height,pos_width+1
        if directions[current_direction]=='v':
            next_step_y,next_step_x=pos_height+1,pos_width
    return False
if __name__ == "__main__":
    with open("input.txt") as f:
        file=f.read()
        loop=(loops(file))

        loop = [list(row) for row in loop.split('\n')]
        full_map=(file.split('\n'))
        full_map = [list(row) for row in full_map]
        directions=['<','^','>','v']
        current_direction=-1
        height=len(full_map)
        width=len(full_map[0])
        count=0
        quan=0
        pos_height,pos_width=-1,-1

        for i in range(len(loop)):
            for j in range(len(loop[0])):
                if loop[i][j] in directions:

                    if(is_looping(file,i,j)):
                        count+=1

        print(count)


