def create_rules(s: str) -> int:
    a = s.split('\n')
    second_part=[]
    check=1
    rules={}
    for i in a:
        if check:
            if i =="":
                check=0
            else:
                if i[0:2] not in rules:
                    rules[i[0:2]]=[]    
                rules[i[0:2]].append(i[3:5])   
        else:
            second_part.append(i)
    return rules,second_part
def check_lists(rules,lists):
    total=0
    for list in lists:
        list=list.split(',')
        total+=int(check_list(rules,list))
    return total
def start_reorder(list, rules):
    dit = {}
    for l in list:
        dit[l] = []  
    for l in list:
        for j in list: 
            if l in rules and j in rules[l]: 
                dit[l].append(j)
    print(list, dit)
    new_list, check = reorder([], list, dit)
    return new_list
def reorder(new_list, list, dit):
    if not list:
        return new_list, True
    for candidate in list[:]:
        check_candidate = 1
        if candidate in dit:
            for must_be_after in dit[candidate]:
                if must_be_after in new_list: 
                    check_candidate = 0
                    break
        if check_candidate:
            next_list = list[:]
            next_list.remove(candidate)
            next_new_list = new_list + [candidate]
            final_list, check = reorder(next_new_list, next_list, dit)
            if check:
                return final_list, True
    return [], False

def check_list(rules, list):
    for position_element_in_list in range(len(list)):
        element = list[position_element_in_list]
        if element in rules:
            not_before = rules[element]
            for position_to_be_check in range(position_element_in_list):
                if list[position_to_be_check] in not_before:
                    list = start_reorder(list, rules)
                    return list[len(list)//2] 
    return 0
if __name__ == "__main__":
    with open("input.txt") as f:
        rules, lists=(create_rules(f.read()))
        # print(rules)
        print(check_lists(rules,lists))