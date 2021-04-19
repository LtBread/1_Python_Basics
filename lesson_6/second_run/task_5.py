import sys
import argparse
import task_4


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('left_file', action='store', type=str)
    parser.add_argument('right_file', action='store', type=str)
    parser.add_argument('center_file', action='store', type=str)
    args = parser.parse_args()
    task_4.combined_file(
        args.left_file,
        args.right_file,
        args.center_file
    )


def classic(argv):
    if not argv:
        return 1
    left_file, right_file, center_file = argv[1:4]
    task_4.combined_file(left_file, right_file, center_file)
    return 0


if __name__ == '__main__':
    try:
        exit(classic(sys.argv))
        # cli()
    except StopIteration as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
