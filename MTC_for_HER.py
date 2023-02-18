
class MTC_for_HER(Env):
    '''
    he position is clipped to the range `[-1.2, 0.6]`
    velocity is clipped to the range `[-0.07, 0.07]`
    '''
    spec = EnvSpec("MountainCartWithGoal-v0")
    def __init__(self, mtc) -> None:
        super().__init__()
        self.MTC = mtc
        self.desired_goal = [0.6, 0.05]
        self.observation_space = spaces.Dict(
            {
                "observation": self.MTC.observation_space,
                "achieved_goal": self.MTC.observation_space,
                "desired_goal": self.MTC.observation_space,
            }
        )
        self.action_space = MTC.action_space
    def step(self, action):
        obs, reward, done, info = self.MTC.step(action)
        # First adjust obs
        self.new_obs = {
            "observation": obs, 
            "achieved_goal": obs, 
            "desired_goal" :self.desired_goal
        }
        obs = self.new_obs
        # second adjust reward by checking whether desired result have reached or not
        reward += self.goal_check()

        return obs, reward, done, info
    def goal_check(self):
        if self.new_obs['achieved_goal'][0] > self.desired_goal[0]:
            return 1
        else:
            0
    def reset(self):
        self.MTC.reset()