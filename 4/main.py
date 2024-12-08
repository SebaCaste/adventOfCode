def serch_xmax(s: str) -> int:
    a = s.split('\n')
    count=0
    number_lines=(len(a))
    elements_line=(len(a[0]))
    for i in range(number_lines):
        for j in range(elements_line):
            if(a[i][j]=="X"):
                if(i+3<number_lines):
                    if(a[i+1][j]=="M" and a[i+2][j]=="A" and a[i+3][j]=="S" ):
                        count+=1
                if(j+3<elements_line):
                    if(a[i][j+1]=="M" and a[i][j+2]=="A" and a[i][j+3]=="S" ):
                        count+=1
                if(j+3<elements_line and i+3<number_lines ):
                    if(a[i+1][j+1]=="M" and a[i+2][j+2]=="A" and a[i+3][j+3]=="S" ):
                        count+=1
                if(i-3>=0):
                    if(a[i-1][j]=="M" and a[i-2][j]=="A" and a[i-3][j]=="S" ):
                        count+=1
                if(j-3>=0):
                    if(a[i][j-1]=="M" and a[i][j-2]=="A" and a[i][j-3]=="S" ):
                        count+=1
                if(j-3>=0 and i-3>=0):
                    if(a[i-1][j-1]=="M" and a[i-2][j-2]=="A" and a[i-3][j-3]=="S" ):
                        count+=1
                if(j-3>=0 and i+3<number_lines):
                    if(a[i+1][j-1]=="M" and a[i+2][j-2]=="A" and a[i+3][j-3]=="S" ):
                        count+=1
                if(j+3<elements_line and i-3>=0):
                    if(a[i-1][j+1]=="M" and a[i-2][j+2]=="A" and a[i-3][j+3]=="S" ):
                        count+=1
                
                
    return count
def serch_x_max(s: str) -> int:
    a = s.split('\n')
    count=0
    number_lines=(len(a))
    elements_line=(len(a[0]))
    for i in range(number_lines):
        for j in range(elements_line):
            if(a[i][j]=="A" and i>=1 and j>=1 and i<number_lines-1 and j<elements_line-1):
                if (((a[i-1][j-1]=="M" and a[i+1][j+1]=="S") or (a[i-1][j-1]=="S" and a[i+1][j+1]=="M"))
                    and ((a[i-1][j+1]=="M" and a[i+1][j-1]=="S") or (a[i-1][j+1]=="S" and a[i+1][j-1]=="M"))):
                    count+=1
    return count
if __name__ == "__main__":
    with open("input.txt") as f:
        print(serch_x_max(f.read()))