import sys

word = sys.argv
if len(word) >= 2:
    print(f"parameters: {len(word) - 1}")
    for i in word[1:]:
        print(f"{i}: {len(i)}")
else:
    print("none")