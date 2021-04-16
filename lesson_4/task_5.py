# Задание 5

# import sys
import utils
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('rate', type=str)
parser.add_argument('-d', '--data', action='store_true', help='show data')
args = parser.parse_args()
answer = utils.currency_rates(args.rate)
if answer is None:
    print(answer)
elif args.data:
    print(*answer)
else:
    print(answer[1])


# def main(argv):
#     if not argv:
#         return 1
#     print(utils.currency_rates(argv[1]))
#     return 0
#
#
# if __name__ == '__main__':
#     exit(main(sys.argv))
