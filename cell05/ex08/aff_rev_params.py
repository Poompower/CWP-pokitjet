import sys

txt = sys.argv
if len(sys.argv) > 2:
    for i in reversed(txt):
        print(i)
else:
    print("none")