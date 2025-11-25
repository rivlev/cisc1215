import sys

y = 7
d = {'x':5, 'y':7}
     
def main():
    # do something
    x = 5
    print(x)
    print(sys.argv)
    print(sum([int(a) for a in sys.argv[1:]]))

# if __name__ == "__main__":
#     main()

import argparse

parser = argparse.ArgumentParser(description="A simple greeting program.")
parser.add_argument("name", help="The name to greet")
parser.add_argument("title", help="Your preferred title", choices="Mr. Ms. Prof. Dr. Lord".split(" "))
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()

if args.verbose:
    print("Running in verbose mode.")
print(f"Hello, {args.title} {args.name}!")