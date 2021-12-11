from matplotlib import pyplot as plt
import numpy as np
import scipy.stats

NUM_POINTS = 500


def draw_clump(mu_x, mu_y, std_x, std_y):
    x = np.random.normal(mu_x, std_x)
    y = np.random.normal(mu_y, std_y)
    plt.plot(x, y, "bo")


def draw_gaussian(mu, std):
    x = np.linspace(mu - std, mu + std, NUM_POINTS)
    y = scipy.stats.norm.pdf(x, mu, std)
    plt.plot(x, y, "bo")


def draw_half_circle_with_noise(start_x, end_x, start_y, end_y):
    noise = np.random.uniform(low=0, high=0.1, size=(NUM_POINTS,))
    y = np.linspace(start_y, end_y, num=NUM_POINTS)
    y = np.sin(y)
    y = y + noise
    x = np.linspace(start_x, end_x, num=NUM_POINTS)
    plt.plot(x, y, 'bo')


def draw_uniform_distribution(x1, x2, y1, y2):
    minimums = [x1, y1]
    maximums = [x2, y2]
    points = np.random.uniform(low=minimums, high=maximums, size=(NUM_POINTS, 2))
    x = points[:, 0]
    y = points[:, 1]
    plt.plot(x, y, 'bo')
    plt.savefig("./Two_uniform_dist.png", format="png")
    plt.close()


def draw_three_gaussians():
    mu = 0
    std_first = 0.5
    std_second = 1
    std_third = 2
    draw_gaussian(mu, std_first)
    draw_gaussian(mu, std_second)
    draw_gaussian(mu, std_third)
    plt.savefig("./Two_Three_Gaussians.png", format="png")
    plt.close()


def draw_four_clumps():
    draw_clump(0, 0, 4, 0.5)
    draw_clump(0, 2, 4, 0.5)
    draw_clump(5, 0, 4, 0.5)
    draw_clump(5, 2, 4, 0.5)
    plt.savefig("./Two_Four_Clumps.png", format="png")
    plt.close()


def draw_two_half_circles_with_noise():
    plt.axes().set_ylim(-1.1, 2.1)
    plt.axes().set_xlim(-1.1, 2.1)
    draw_half_circle_with_noise(-1.0, 1.0, 0, np.pi)
    draw_half_circle_with_noise(0.0, 2.0, np.pi, 2*np.pi)
    plt.savefig("./Two_Half_Circles.png", format="png")
    plt.close()


def main():
    draw_uniform_distribution(-10, 2, 18, 45)
    draw_three_gaussians()
    draw_two_half_circles_with_noise()
    draw_four_clumps()


if __name__ == '__main__':
    main()
