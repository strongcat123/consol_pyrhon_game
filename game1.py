import os
import keyboard
import time
import random

screen_size = 10

x = 0
y = 0
count = 0

screen = [['▢' for j in range(screen_size)] for i in range(screen_size)]
screen[x][y] = '▣'


def reset_cursor():
    print("\033[H", end="")


def screen_watch():
    for i in range(screen_size):
        for j in range(screen_size):
            print(screen[i][j], end=' ')
        print()
    print(f"Position: ({x}, {y})")
    print(f"Items collected: {count}")


def item():
    global item_x, item_y

    while True:
        item_x = random.randint(0, screen_size - 1)
        item_y = random.randint(0, screen_size - 1)

        if item_x != x or item_y != y:
            break

    screen[item_x][item_y] = '❤️'


def move():
    global x, y

    nx, ny = x, y

    if keyboard.is_pressed('w'):
        nx -= 1
    elif keyboard.is_pressed('s'):
        nx += 1
    elif keyboard.is_pressed('a'):
        ny -= 1
    elif keyboard.is_pressed('d'):
        ny += 1

    if 0 <= nx < screen_size and 0 <= ny < screen_size:
        screen[x][y] = '▢'
        x, y = nx, ny


os.system('cls')

item()

while True:
    reset_cursor()
    screen_watch()
    move()

    if x == item_x and y == item_y:
        screen[item_x][item_y] = '▢'
        count += 1
        item()

    screen[x][y] = '▣'
    time.sleep(0.05)