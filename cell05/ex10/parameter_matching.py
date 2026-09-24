import sys

if len(sys.argv) == 2:
    key = sys.argv[1]
    ans = input("What was the parameter? ")
    if ans == key:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")