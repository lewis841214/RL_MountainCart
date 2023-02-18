import gym
from stable_baselines3 import HerReplayBuffer, DDPG, DQN, SAC, TD3
from stable_baselines3 import PPO, A2C
from stable_baselines3.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise
import numpy as np
# env = gym.make("CartPole-v1")
env = gym.make("MountainCar-v0")
# model = PPO("MlpPolicy", env, verbose=1)
model = DQN( 'MlpPolicy', env, verbose=1, learning_starts = 50000) #MultiInputPolicy
# model = DQN( 'MlpPolicy', env, verbose=1) #MultiInputPolicy

model.learn( total_timesteps=1000)


def run_(model):
    vec_env = model.get_env()
    obs = vec_env.reset()
    for i in range(1000):
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, info = vec_env.step(action)
        vec_env.render()
        # VecEnv resets automatically
        # if done:
        #   obs = env.reset()

    env.close()
run_(model)
breakpoint()