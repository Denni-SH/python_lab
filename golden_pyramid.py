import random
import argparse


def calculate(tr):
    for i in range(len(tr) - 2, -1, -1):
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
    return tr[0][0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('level',  type=int, help="Enter level")
    args = parser.parse_args()

    golden_list = [[random.randint(1, 9) for j in range(i)] for i in range(1, args.level+1)]
    print("Pyramid: ", golden_list)
    print("Max length is", calculate(golden_list))



