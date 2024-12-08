def calculate_similarity_score(filename):
    list1 = []
    list2 = []
    with open(filename, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    total_score = 0

    for num in list1:

        frequency = list2.count(num)

        score = num * frequency
        total_score += score
    
    print(f"Similarity Score: {total_score}")
    return total_score
calculate_similarity_score('input.txt')  