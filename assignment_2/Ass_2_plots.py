from matplotlib import pyplot as plt
import numpy as np
import scipy.stats

NUM_POINTS = 500


def draw_uniform_distribution(x1, x2, y1, y2):
    minimums = [x1, y1]
    maximums = [x2, y2]
    points = np.random.uniform(low=minimums, high=maximums, size=(NUM_POINTS, 2))
    x = points[:, 0]
    y = points[:, 1]
    plt.plot(x, y, 'bo')
    plt.show()


def draw_three_gaussians():
    mu = 0
    std_first = 0.5
    std_second = 1
    std_third = 2
    x_first = np.linspace(mu - std_first, mu + std_first, NUM_POINTS)
    y_first = scipy.stats.norm.pdf(x_first, mu, std_first)
    x_second = np.linspace(mu - std_second, mu + std_second, NUM_POINTS)
    y_second = scipy.stats.norm.pdf(x_second, mu, std_second)
    x_third = np.linspace(mu - std_third, mu + std_third, NUM_POINTS)
    y_third = scipy.stats.norm.pdf(x_third, mu, std_third)
    plt.plot(x_first, y_first, "bo")
    plt.plot(x_second, y_second, "bo")
    plt.plot(x_third, y_third, "bo")
    plt.show()


def draw_two_half_circles_with_noise():
    noise = np.random.uniform(low=0, high=0.1, size=(NUM_POINTS,))
    y_first_func = np.linspace(0, np.pi, num=NUM_POINTS)
    y_first_func = np.sin(y_first_func)
    y_first_func = y_first_func + noise
    y_second_func = np.linspace(np.pi, 2*np.pi, num=NUM_POINTS)
    y_second_func = np.sin(y_second_func)
    y_second_func = y_second_func + noise
    x_first_func = np.linspace(-1.0, 1.0, NUM_POINTS)
    x_second_func = np.linspace(0.0, 2.0, NUM_POINTS)
    plt.axes().set_ylim(-1.0, 2.0)
    plt.plot(x_first_func, y_first_func, 'bo')
    plt.plot(x_second_func, y_second_func, 'bo')
    plt.show()


def main():
    draw_uniform_distribution(-10, 2, 18, 45)
    draw_three_gaussians()
    draw_two_half_circles_with_noise()


if __name__ == '__main__':
    main()
