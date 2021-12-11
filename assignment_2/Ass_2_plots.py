from matplotlib import pyplot as plt
import numpy as np
import scipy.stats
import sklearn

NUM_POINTS = 500


################################## private methods ###################################


def draw_clump(mu_x, mu_y, std_x, std_y, size):
    x = np.random.normal(mu_x, std_x, size=(size,))
    y = np.random.normal(mu_y, std_y, size=(size,))
    plt.plot(x, y, "bo")
    points = np.stack([x, y], axis=1)
    return points


def draw_gaussian(mu, std):
    x = np.linspace(mu - std, mu + std, NUM_POINTS)
    y = scipy.stats.norm.pdf(x, mu, std)
    plt.plot(x, y, "bo")
    points = np.stack([x, y], axis=1)
    return points


def draw_half_circle_with_noise(start_x, end_x, start_y, end_y):
    noise = np.random.uniform(low=0, high=0.1, size=(NUM_POINTS,))
    y = np.linspace(start_y, end_y, num=NUM_POINTS)
    y = np.sin(y)
    y = y + noise
    x = np.linspace(start_x, end_x, num=NUM_POINTS)
    plt.plot(x, y, 'bo')
    points = np.stack([x, y], axis=1)
    return points


################################## main methods ###################################


def draw_uniform_distribution(x1, x2, y1, y2):
    minimums = [x1, y1]
    maximums = [x2, y2]
    points = np.random.uniform(low=minimums, high=maximums, size=(NUM_POINTS, 2))
    x = points[:, 0]
    y = points[:, 1]
    plt.plot(x, y, 'bo')
    plt.savefig("./uniform_dist.png", format="png")
    plt.close()
    np.savetxt("./uniform_dist_data.txt", points, delimiter=",")


def draw_three_gaussians():
    mu = 0
    std_first = 0.5
    std_second = 1
    std_third = 2
    points_1 = draw_gaussian(mu, std_first)
    points_2 = draw_gaussian(mu, std_second)
    points_3 = draw_gaussian(mu, std_third)
    plt.savefig("./Three_Gaussians.png", format="png")
    plt.close()
    all_points = np.concatenate([points_1, points_2, points_3], axis=0)
    np.savetxt("./Three_Gaussians_data.txt", all_points, delimiter=",")


def draw_four_clumps():
    points_1 = draw_clump(0, 0, 0.5, 0.1, int(NUM_POINTS / 4))
    points_2 = draw_clump(0, 2, 0.5, 0.1, int(NUM_POINTS / 4))
    points_3 = draw_clump(5, 0, 0.5, 0.1, int(NUM_POINTS / 4))
    points_4 = draw_clump(5, 2, 0.5, 0.1, int(NUM_POINTS / 4))
    x_ticks = np.linspace(-2, 8, 6)
    y_ticks = np.linspace(-4, 6, 6)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.savefig("./Four_Clumps.png", format="png")
    plt.close()
    all_points = np.concatenate([points_1, points_2, points_3, points_4], axis=0)
    np.savetxt("./Four_Clumps_data.txt", all_points, delimiter=",")


def draw_two_half_circles_with_noise():
    points_1 = draw_half_circle_with_noise(-1.0, 1.0, 0, np.pi)
    points_2 = draw_half_circle_with_noise(0.0, 2.0, np.pi, 2*np.pi)
    x_ticks_labels = np.linspace(-1, 2, 7)
    y_ticks_labels = np.linspace(-1, 2, 7)
    locs_x, _ = plt.xticks()
    locs_y, _ = plt.yticks()
    plt.xticks(x_ticks_labels)
    plt.yticks(y_ticks_labels)
    plt.savefig("./Two_Half_Circles.png", format="png")
    plt.close()
    all_points = np.concatenate([points_1, points_2], axis=0)
    np.savetxt("./Two_Half_Circles_data.txt", all_points, delimiter=",")


def main():
    draw_uniform_distribution(-10, 2, 18, 45)
    draw_three_gaussians()
    draw_two_half_circles_with_noise()
    draw_four_clumps()


if __name__ == '__main__':
    main()
