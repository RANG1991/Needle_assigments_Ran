from scipy import spatial


def main():
    A = [5, 5, 4, 4, 0]
    B = [1, 2, 0, 2, 0]
    C = [0, 2, 0, 1, 5]
    D = [2, 2, 1, 0, 1]
    print(1 - spatial.distance.cosine(A, B))
    print(1 - spatial.distance.cosine(A, C))
    print(1 - spatial.distance.cosine(A, D))
    print(1 - spatial.distance.cosine(B, C))
    print(1 - spatial.distance.cosine(B, C))
    print(1 - spatial.distance.cosine(C, D))


if __name__ == "__main__":
    main()
