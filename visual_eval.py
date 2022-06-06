import time
from gym_environment import GomokuEnv

nsteps = 200

env = GomokuEnv()

for step in range(nsteps):
    # action = env.action_space.sample()
    print("Enter column:")
    col = int(input())
    print("Enter row:")
    row = int(input())
    if row == -1 or col == -1:
        break
    action = row * (19) + col
    obs, reward, done, info = env.step(action)
    env.render()
    # env.render()
    # time.sleep(0.001)
    if done:
        print('Winning move: ', action)
        env.reset()

env.render()
env.close()

