import sys
import numpy as np
def read_input(file):
    drone_position=[]
    drone_speed=[]
    for row in file.split("\n"):
        # print(row.split(" "))
        pos,vel=row.split(" ")
        # print(pos,vel)

        # print(pos,vel)
        drone_position.append((int(pos[2:pos.index(",")]),int(pos[pos.index(",")+1:])))
        drone_speed.append((int(vel[2:vel.index(",")]),int(vel[vel.index(",")+1:])))
    return drone_position,drone_speed

def position_after_seconds(w,h,drone_position,drone_speed,seconds):
    p=[]
    for i,pos in enumerate(drone_position):
        # print(pos[0])
        x=(pos[0]+seconds*drone_speed[i][0])%w
        y=(pos[1]+seconds*drone_speed[i][1])%h
        p.append((x,y))
    return p

if __name__ == "__main__":
    np.set_printoptions(threshold=sys.maxsize)
    with open("input.txt") as f:
        file=f.read()
        drone_position,drone_speed=read_input(file)
        w=101
        h=103
        # w=11
        # h=7
        # seconds=100
        count=0
        for i in range(100000):

            pos=position_after_seconds(w,h,drone_position,drone_speed,i)
            matrix=np.zeros((w,h))
            for p in pos:
                matrix[p[0],p[1]]+=1
            if np.count_nonzero(matrix == 1)>499:
                
                stampa=""
                for el in matrix:
                    for o in el:
                        if o==1:
                            stampa+="#"
                        else:
                            stampa+=" "
                    stampa+="\n"
                print(stampa)
                print(i)
                break
                

        print(count)
            # tl=(matrix[0:w//2,0:h//2]).T
            # bl=(matrix[0:w//2,h//2+1:]).T
            # tr=(matrix[w//2+1:,0:h//2]).T
            # br=(matrix[w//2+1:,h//2+1:]).T
            # value=np.sum(tl)*np.sum(bl)*np.sum(tr)*np.sum(br)
        # print(tl)
        # print(bl)
        # print(tr)
        # print(br)
        # print(value)
