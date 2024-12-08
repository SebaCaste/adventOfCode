def create_map(file):
    mappa=file.split('\n')
    mappa = [list(row) for row in mappa]
    elements={}
    rowlenght=len(mappa)
    maplenght=len(mappa[0])
    # print(rowlenght)
    # print(maplenght)
    for i,row in (enumerate(mappa)):
        for a,char in (enumerate(row)):
            if(char!='.'):
                print(i,a,char)
                elements.setdefault(char, []).append((i,a))
    # print(elements)
    count=0
    for el in elements:
        for coords in elements[el]:
            for coords2 in elements[el]:
                if coords !=coords2:
                    x,y=coords
                    x2,y2=coords2
                    if mappa[x][y]!="#":
                        mappa[x][y]="#"
                        count+=1
                    
                    difx=x-x2
                    dify=y-y2
                    mul=1
                    proposex=difx*mul+x
                    proposey=dify*mul+y
                    while(proposex>=0 and proposex<rowlenght and proposey>=0 and proposey<maplenght):
                        if mappa[proposex][proposey]!="#":
                            mappa[proposex][proposey]="#"
                            count+=1
                        mul+=1
                        proposex=difx*mul+x
                        proposey=dify*mul+y
                    # proposex=x-x2+x
                    # proposey=y-y2+y
                    # # print(x,y,x2,y2,proposex,proposey)
                    # if proposex>=0 and proposex<rowlenght and proposey>=0 and proposey<maplenght:
                    #     if mappa[proposex][proposey]=="#":
                    #         # print('insomma')
                    #         count=count-1
                    #     mappa[proposex][proposey]="#"
                    #     count+=1
    # for row in (mappa):
        # print (row)
    return count
if __name__ == "__main__":
    with open("input.txt") as f:
        file=f.read()
        ris=(create_map(file))
        print(ris)
