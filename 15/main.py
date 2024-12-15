def read_input(file):
    mappa,commands=file.split("\n\n")
    mappa= [list(row) for row in mappa.split("\n")]
    for i,row in enumerate(mappa):
        for j,el in enumerate(row):
            if el =="@":
                robot_position=(i,j)
    commands=commands.replace('\n', '')
    return mappa,commands,robot_position
def contapunti(mappa):
    punti=0
    for i,row in enumerate(mappa):
        # print(row)
        for j,el in enumerate(row):
            # print(el,"seba",i,j)
            # print(punti)
            if el =='O':
                # print(el,100*i+j," insomma")
                punti+=100*i+j
    return punti
if __name__ == "__main__":
    with open("input.txt") as f:
        file=f.read()
        mappa,commands,robot_position=read_input(file)
        # print(mappa,commands,robot_position)
        
        # print(mappa[robot_position[0]][robot_position[1]])
        direction={"<":(0,-1),">":(0,1),"^":(-1,0),"v":(1,0)}
        position_check=robot_position
        # for row in mappa:
        #     print(row)
        # print("---------------------------------------------------------")
        for d in commands:
            # print(d)
            # print(direction[d])
            # print(position_check)
            # print(mappa[position_check[0]][position_check[1]])
            position_check=(position_check[0]+direction[d][0],position_check[1]+direction[d][1])
            

            # print(mappa[position_check[0]][position_check[1]])
            stack=[]
            while(mappa[position_check[0]][position_check[1]]=="O"):
                stack.append(position_check)
                position_check=(position_check[0]+direction[d][0],position_check[1]+direction[d][1])
            if(mappa[position_check[0]][position_check[1]]=="#"):
                position_check=robot_position
            if(mappa[position_check[0]][position_check[1]]=="."):
                # print("qui")
                while(stack!=[]):
                    x,y=stack.pop()
                    mappa[position_check[0]][position_check[1]]=mappa[x][y]
                    position_check=(x,y)
                mappa[robot_position[0]][robot_position[1]]="."
                robot_position=(robot_position[0]+direction[d][0],robot_position[1]+direction[d][1])
                mappa[robot_position[0]][robot_position[1]]="@"

            robot_position+=direction[d]
        #     for row in mappa:
        #         print(row)
        #     print("---------------------------------------------------------")
        for row in mappa:
            print(row)
        print("---------------------------------------------------------")

        punti=contapunti(mappa)
        print(punti)

       
        
            
