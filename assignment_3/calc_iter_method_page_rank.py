import numpy as np

mat = np.array([[(9 / 20.0), (7 / 20.0), (7 / 30.0)],
                [(7 / 20.0), (1 / 10.0), (7 / 30.0)],
                [0.0, (7 / 20.0), (1 / 10.0)]])

r_old = np.array([(1 / 3.0), (1 / 3.0), (1 / 3.0)])
r_new = np.zeros((3,))
first_iter = True
epsilon = 0.000000001

while np.linalg.norm(r_old - r_new, 1) > epsilon:
    if first_iter:
        first_iter = False
    else:
        r_old = r_new
    r_new = np.matmul(mat, r_old)
    print(r_new, r_old, np.linalg.norm(r_old - r_new, 1))

print(r_new)
