import numpy as np
def read_input(file):
    file= file.split("\n\n")
    Ba=[]
    Bb=[]
    prize=[]
    for machine in file:
        a,b,p=machine.split("\n")
        Ba.append((int(a[a.index('X+')+2:a.index(',')]),int(a[a.index('Y+')+2:])))
        Bb.append((int(b[b.index('X+')+2:b.index(',')]),int(b[b.index('Y+')+2:])))
        prize.append((int(p[p.index('X=')+2:p.index(',')]),int(p[p.index('Y=')+2:])))


    return Ba,Bb,prize
def min_token(Ba,Bb,prize):

    # Ba[0]*n+Bb[0]*m=prize[0]
    # Ba[1]*n+Bb[1]*m=prize[1]
    m=((prize[1]/Bb[1])-((Ba[1]*prize[0])/(Ba[0]*Bb[1])))/(1-((Ba[1]*Bb[0])/(Bb[1]*Ba[0])))
    n=(prize[0]-(Bb[0]*m))/Ba[0]

    if m.is_integer() and n.is_integer() and n<100 and m<100:
        return 3*n+m
    else:
        return 0

def min_token_brute(Ba,Bb,prize):
    for i in range(101,0,-1):
        for j in range(101,0,-1):
            if Ba[0]*i+Bb[0]*j==prize[0] and Ba[1]*i+Bb[1]*j==prize[1]:
                return i*3+j
    return 0
def mim_token_lib(Ba,Bb,prize):

    equations=np.array([[Ba[0],Bb[0]],[Ba[1],Bb[1]]])

    prize_i=prize[0]+10000000000000
    prize_j=prize[1]+10000000000000

    solution=np.array([prize_i,prize_j])
    sol=np.linalg.solve(equations,solution)

    n=round(sol[0])
    m=round(sol[1])

    if Ba[0]*n+Bb[0]*m==prize_i and Ba[1]*n+Bb[1]*m==prize_j:
        return (3*(n))+(m)
    else:
        return 0
if __name__ == "__main__":
    with open("input.txt") as f:
        file=f.read()
        Ba,Bb,prize=read_input(file)
        tot_token=0
        for machines in range(len(Ba)):
            tot_token+=mim_token_lib(Ba[machines],Bb[machines],prize[machines])
        print(tot_token)