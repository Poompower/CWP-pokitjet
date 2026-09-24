import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        return

    for filepath in sys.argv[1:]:
        try:
            with open(filepath, 'r') as f:
                content = f.read()

            result = checkmate(content)
            if not result:
                print("Error")
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()
