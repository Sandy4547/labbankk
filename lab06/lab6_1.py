print("a.")
scores = [
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    [5, 7, 4, 3, 2],
    [0, 0, 0, 0, 0]
]

N = len(scores)
for i in range(N):
    print(scores[i])


print("b.")
print(scores[2])


print("c.")
print(scores[1][:3])

print("d.")
scores = [
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    [5, 0, 3, 2, 1]
]

scores[1] = [2, 0, 6, 8, 10]

N = len(scores)
for i in range(N):
    print(scores[i])


print("e.")
scores[2] = [0, 0, 0, 0, 0]
N = len(scores)
for i in range(N):
    print(scores[i])
