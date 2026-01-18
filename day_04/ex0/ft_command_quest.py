import sys

print("=== Command Quest ===")

if len(sys.argv) == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
else:
    print(f"Program name: {sys.argv[0]}")
    print("Arguments received: ", len(sys.argv[1:]))
    for arg in sys.argv[1:]:
        print("Arguments : ", arg)

print(f"Total arguments: {len(sys.argv)}")
