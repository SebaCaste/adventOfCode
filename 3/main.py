def serch_mul(s: str) -> int:
    total = 0
    length = len(s)
    i = 0
    check=1
    while i < length - 3:  
        if s[i] == 'd' and s[i+1] == 'o' and s[i+2] == '(' and s[i+3] == ')':
           check=1
           i += 4
        if s[i] == 'd' and s[i+1] == 'o' and s[i+2] == 'n' and s[i+3] == "'" and s[i+4] == 't' and s[i+5] == '('and s[i+6] == ')': 
            check=0
            i += 7
        if s[i] == 'm' and s[i+1] == 'u' and s[i+2] == 'l' and s[i+3] == '(':
            i += 4  
            num1 = 0
            while i < length and s[i].isdigit():
                num1 = num1 * 10 + int(s[i])
                i += 1
            if i < length and s[i] == ',':
                i += 1  
                num2 = 0
                while i < length and s[i].isdigit():
                    num2 = num2 * 10 + int(s[i])
                    i += 1
                if i < length and s[i] == ')' and check:
                    total += num1 * num2
        i += 1
    return total
if __name__ == "__main__":
    with open("input.txt") as f:
        print(serch_mul(f.read()))