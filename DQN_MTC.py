import gym

from stable_baselines3 import DQN

env = gym.make("MountainCar-v0")





model = DQN("MlpPolicy", env, verbose=1, batch_size = 500, learning_rate = 1e-3, gamma = 0.59)
model.learn(total_timesteps=10000, log_interval=4)
model.save("dqn_MTC")

del model # remove to demonstrate saving and loading

model = DQN.load("dqn_MTC")

obs = env.reset()
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    print('obs',obs)
    env.render()
    if done:
      obs = env.reset()