import matplotlib.pyplot as plt
import numpy as np


def draw_tree(ax, x, y, length, angle, depth):
    if depth == 0:
        return

    x1 = x + length * np.cos(angle)
    y1 = y + length * np.sin(angle)

    ax.plot([x, x1], [y, y1], color='brown', lw=1)

    new_length = length * 0.7
    draw_tree(ax, x1, y1, new_length, angle + np.pi / 4, depth - 1)
    draw_tree(ax, x1, y1, new_length, angle - np.pi / 4, depth - 1)  


def main():
    recursion_depth = int(input("Введіть рівень рекурсії: "))

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    x, y = 0, 0
    length = 100
    angle = np.pi / 2

    draw_tree(ax, x, y, length, angle, recursion_depth)

    plt.show()


if __name__ == "__main__":
    main()
