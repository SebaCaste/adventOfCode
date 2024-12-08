def are_factors(res,current,fac):
    if(res<current or ( (not fac) and current!=res)):
       return False
    print(fac)
    if(res==current and (not fac)):
        return True
    if(are_factors(res,current+int(fac[0]),fac=fac[1:]) or are_factors(res,current*int(fac[0]),fac=fac[1:])or are_factors(res,int(str(current)+str(fac[0])),fac=fac[1:])):
        return True
def calculus(s:str)->int:
    full_tab=(s.split('\n'))
    count=0
    for equatin in full_tab:
        res,factors=equatin.split(':')
        res=int(res)
        fac=(factors.split(' '))
        if(are_factors(res,0,fac[1:])):
            count+=res
    print(count)
if __name__ == "__main__":
    with open("test.txt") as f:
        file=f.read()
        loop=(calculus(file))
