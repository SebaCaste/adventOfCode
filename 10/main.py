def read_map_and_trailhead(file):
    mappa=file.split('\n')
    mappa=[list(row) for row in mappa]
    trailhead=[]
    for i,row in enumerate(mappa):
        for j,el in enumerate(row):
            if el=='0':
                trailhead.append((i,j))
    return trailhead,mappa
def checktrails_unique_paths(value,pos,mappa):
    sum=0
    if pos[1]>=0 and pos[0]>=0 and pos[0]<=len(mappa)-1 and pos[1]<=len(mappa[0])-1:
        if int(mappa[pos[0]][pos[1]])==value and value==9:
            return 1
        if int(mappa[pos[0]][pos[1]])==value:
            sum+=checktrails_unique_paths(value+1,(pos[0]-1,pos[1]),mappa)
            sum+=checktrails_unique_paths(value+1,(pos[0]+1,pos[1]),mappa)
            sum+=checktrails_unique_paths(value+1,(pos[0],pos[1]-1),mappa)
            sum+=checktrails_unique_paths(value+1,(pos[0],pos[1]+1),mappa)
        else: 
            return 0
    return sum
def checktrails(value,pos,mappa):
    unique_top=set()
    if pos[1]>=0 and pos[0]>=0 and pos[0]<=len(mappa)-1 and pos[1]<=len(mappa[0])-1:
        if int(mappa[pos[0]][pos[1]])==value:
            if value==9:
                unique_top.add(pos)
                return unique_top
            elif int(mappa[pos[0]][pos[1]])==value:
                unique_top.update(checktrails(value+1,(pos[0]-1,pos[1]),mappa))
                unique_top.update(checktrails(value+1,(pos[0]+1,pos[1]),mappa))
                unique_top.update(checktrails(value+1,(pos[0],pos[1]-1),mappa))
                unique_top.update(checktrails(value+1,(pos[0],pos[1]+1),mappa))
    return unique_top
def sum_trails_score(trailhead,mappa):
    tot=0
    for el in trailhead:
        print(mappa[el[0]][el[1]],el)
        trails_values=(checktrails(int(mappa[el[0]][el[1]]),el,mappa))
        print((trails_values))
        tot+=len(trails_values)
    return tot
def sum_trails_score_unique_path(trailhead,mappa):
    tot=0
    for el in trailhead:
        print(mappa[el[0]][el[1]],el)
        trails_values=(checktrails_unique_paths(int(mappa[el[0]][el[1]]),el,mappa))
        print((trails_values))
        tot+=(trails_values)
    return tot

if __name__ == "__main__":
    with open("input.txt") as f:
        file=f.read()
        trailhead,mappa=read_map_and_trailhead(file)
        ris=sum_trails_score_unique_path(trailhead,mappa)
        print(ris)