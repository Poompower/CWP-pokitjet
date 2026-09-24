original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for x in original_array:
    if x > 5:
        new_set.add(x + 2)

print(original_array)
print(new_set)
