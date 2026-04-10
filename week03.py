anxiety_scores = [4, 9, 15, 7, 21, 3, 11, 6]

def get_mean(scores):
    return sum(scores)/len(scores)
print("Mean score is " + str(get_mean(anxiety_scores)))

def get_max(scores):
    current_max = 4
    for values in scores:
        if values >= current_max:
            current_max = values
        else:
            current_max = current_max
    return current_max

print("The highest score is " + str(get_max(anxiety_scores)))

def count_severe(scores):
    count = 0
    for values in scores:
        if values >= 15:
            count = count + 1
        else:
            count = count
    return count
print("The number of patients with severe scores of anxiety symptoms is " + str(count_severe(anxiety_scores)))

