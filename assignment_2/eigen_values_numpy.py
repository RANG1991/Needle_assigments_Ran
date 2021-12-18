import numpy as np
from sklearn.preprocessing import normalize


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

    bitton_vec = np.array([(5 + np.sqrt(13)) / 2, (3 + np.sqrt(13)) / 2, (1 + np.sqrt(13)) / 2,
                           (5 + np.sqrt(13)) / -2, (5 + np.sqrt(13)) / -2, (5 + np.sqrt(13)) / -2,
                           -1, 1, 0])
    bitton_vec = normalize(bitton_vec[:, np.newaxis], axis=0).ravel()
    print("bitton's vec normalized is: {}".format(bitton_vec))

    bitton_vec_2 = np.array([(-3 - np.sqrt(13)) / 2, (-1 - np.sqrt(13)) / 2, -2,
                             1, 2, (1 + np.sqrt(13)) / 2,
                             (-1 + np.sqrt(13)) / 2, 0, 1])
    bitton_vec_2 = normalize(bitton_vec_2[:, np.newaxis], axis=0).ravel()
    print("bitton's vec 2 normalized is: {}".format(bitton_vec_2))

    l_rows = []
    keys = sorted(d.keys())
    for key in keys:
        l_rows.append(d[key])
    mat = np.array(l_rows)
    print(mat)
    w, v = np.linalg.eigh(mat)
    w_list = np.real(w).tolist()
    v_list = np.real(v).tolist()
    list_tuples = zip(w_list, v_list)
    list_tuples = sorted(list_tuples, key=lambda x: x[0], reverse=True)
    for i in range(len(list_tuples)):
        normalized_vec = normalize(np.array(list_tuples[i][1])[:, np.newaxis], axis=0).ravel()
        print("The {} eigen value of L is: {}".format(i + 1, list_tuples[i][0]))
        print("The normalized vector is:\n{}".format("\n".join([str(x) for x in normalized_vec.tolist()])))
        print("The sum of the eigen vector is: {}".format(np.sum(normalized_vec)))
        print("The norm 2 of the eigen vector is: {}".format(np.sqrt(np.sum(normalized_vec * normalized_vec))))


if __name__ == "__main__":
    main()
