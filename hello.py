import sys

if len(sys.argv) > 1:
    print(f"Message from pipeline: {sys.argv[1]}")
else:
    print("Hello from pipeline!")
