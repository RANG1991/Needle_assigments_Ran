from matplotlib import pyplot as plt
import numpy as np

NUM_POINTS = 800


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
    draw_two_half_circles_with_noise()


if __name__ == '__main__':
    main()
