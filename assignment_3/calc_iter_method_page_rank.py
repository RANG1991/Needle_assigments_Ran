import numpy as np

mat_1 = np.array([[(1 / 3.0), (9 / 20.0), (1 / 10.0)],
                  [(1 / 3.0), (1 / 10.0), (9 / 20.0)],
                  [(1 / 3.0), (9 / 20.0), (9 / 20.0)]])

mat_2 = np.array([[(23 / 60.0), (30 / 60.0), (9 / 60.0)],
                  [(23 / 60.0), (9 / 60.0), (30 / 60.0)],
                  [(14 / 60.0), (21 / 60.0), (21 / 60.0)]])

mat_3 = np.array([[(3 / 20.0), (1 / 2.0), (1 / 2.0)],
                  [(1 / 2.0), (3 / 20.0), (1 / 2.0)],
                  [(7 / 20.0), (7 / 20.0), 0.0]])


def calc_rank(mat):
    r_old = np.array([(1 / 3.0), (1 / 3.0), (1 / 3.0)])
    r_new = np.zeros((3,))
    first_iter = True
    epsilon = 0.00000000000000001

    while np.linalg.norm(r_old - r_new, 1) > epsilon:
        if first_iter:
            first_iter = False
        else:
            r_old = r_new
        r_new = np.matmul(mat, r_old)
        # print(r_new, r_old, np.linalg.norm(r_old - r_new, 1))
    print("the fina rank of mat is: {}".format(r_new))


calc_rank(mat_1)
calc_rank(mat_2)
calc_rank(mat_3)
