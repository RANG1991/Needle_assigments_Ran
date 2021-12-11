import numpy as np


def main():
    d = {
        "A": [2, -1, -1, 0, 0, 0, 0, 0, 0],
        "B": [-1, 3, -1, 0, 0, 0, 0, -1, 0],
        "C": [-1, -1, 3, -1, 0, 0, 0, 0, 0],
        "D": [0, 0, -1, 3, -1, -1, 0, 0, 0],
        "E": [0, 0, 0, -1, 3, -1, -1, 0, 0],
        "F": [0, 0, 0, -1, -1, 2, 0, 0, 0],
        "G": [0, 0, 0, 0, -1, 0, 3, -1, -1],
        "H": [0, -1, 0, 0, 0, 0, -1, 3, -1],
        "I": [0, 0, 0, 0, 0, 0, -1, -1, 2]
    }
    l_rows = []
    keys = sorted(d.keys())
    for key in keys:
        l_rows.append(d[key])
    mat = np.array(l_rows)
    w, v = np.linalg.eig(mat)
    w = sorted(w, reverse=True)
    print(w)
    print(v)
    for i in range(len(w)):
        print("The {} eigen value of L is: ".format(i + 1), w[i])


if __name__ == "__main__":
    main()
