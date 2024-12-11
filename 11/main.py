def read_stone(file):
    stones=file.split(" ")
    return stones
def blink(stones):
    new_stones=[]
    for stone in stones:
        if stone=='0':
            new_stones.append('1')
        elif len(stone)%2==0:
            lunghezza=int(len(stone)/2)
            new_stones.append(stone[:lunghezza])
            new_stones.append(str(int(stone[lunghezza:])))
        else:
            new_stones.append(str(int(stone)*2024))
    return new_stones
def blink_recursion(it,stones,tot,memo=None):
    if memo is None:
        memo = {}
    state = (it, tuple(stones))
    if state in memo:
        return memo[state]
    if it==0:
        return 1
    else:
        for stone in stones:
            if stone=='0':
                tot+=blink_recursion(it-1,['1'],0,memo)
            elif len(stone)%2==0:
                lunghezza=int(len(stone)/2)
                tot+=blink_recursion(it-1,[stone[:lunghezza]],0,memo)
                tot+=blink_recursion(it-1,[str(int(stone[lunghezza:]))],0,memo)
            else:
                tot+=blink_recursion(it-1,[str(int(stone)*2024)],0,memo)
        memo[state] = tot
        return tot
if __name__ == "__main__":
    with open("input.txt") as f:
        file=f.read()
        stones=read_stone(file)
        stones=[str(stone)for stone in stones]
        convs=75
        memo_dict = {}
        a=(blink_recursion(convs,stones,0,memo_dict))
        print(a)