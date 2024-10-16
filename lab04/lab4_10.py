def averageList(xs):
    return sum(xs) / len(xs)

xs = [4, 8, 6, 6]

result = averageList(xs)

print(f"List: {xs}")
print(f"Average is {result:.1f}.")