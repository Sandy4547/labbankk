def grade(score):
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

scores = [55, 85, 75, 45, 65] 
for i in range(len(scores)): 
    g = grade(scores[i])
    print(i+1, scores[i], g)