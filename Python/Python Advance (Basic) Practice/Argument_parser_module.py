import argparse

# Using Argument parser module with Positional Argument
# parser = argparse.ArgumentParser()
# parser.add_argument("Number1", type=int, help="Enter first Number")
# parser.add_argument("Number2", type=int, help="Enter second Number")
# parser.add_argument("Operation", type=str, help="Choose you operation", choices=["add","sub","mul","div"])
# args = parser.parse_args()

# # print(args.Number1)
# if args.Operation == "add":
#     print(args.Number1 + args.Number2)
# elif args.Operation == "sub":
#     print(args.Number1 - args.Number2)
# elif args.Operation == "mul":
#     print(args.Number1 * args.Number2)
# elif args.Operation == "div":
#     print(args.Number1 / args.Number2)
# else:
#     print("Something went wrong! Please try again.")

# Using Argument parser module with Optional Argument
parser = argparse.ArgumentParser()
parser.add_argument("--Number1", type=int, help="Enter first Number")
parser.add_argument("--Number2", type=int, help="Enter second Number")
parser.add_argument("--Operation", type=str, help="Choose you operation", choices=["add","sub","mul","div"])
args = parser.parse_args()

# print(args.Number1)
if args.Operation == "add":
    print(args.Number1 + args.Number2)
elif args.Operation == "sub":
    print(args.Number1 - args.Number2)
elif args.Operation == "mul":
    print(args.Number1 * args.Number2)
elif args.Operation == "div":
    print(args.Number1 / args.Number2)
else:
    print("Something went wrong! Please try again.")