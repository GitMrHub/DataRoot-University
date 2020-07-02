import random
import msvcrt
import time

from env.snake_env import SnakeEnv


def interact():
    """
    Human interaction with the environment
    """
    env = SnakeEnv()
    done = False
    r = 0
    action = random.randrange(4)

    while not done:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            # up
            if key == 'w':
                action = 0
            # down
            elif key == 's':
                action = 2
            # left
            elif key == 'a':
                action = 3
            # right
            elif key == 'd':
                action = 1

        obs, reward, done, info = env.step(action)
        env.render(mode='human')
        r += reward
        time.sleep(0.04)
    return r


if __name__ == '__main__':
    interact()