import time
from gym_environment import GomokuEnv

nsteps = 30

env = GomokuEnv()

for step in range(nsteps):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    env.render()
    time.sleep(0.001)
    if done:
        env.reset()

env.close()

