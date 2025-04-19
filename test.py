import gym
# import rware

# env_name = "rware-2color-tiny-2ag-easy-v1"

# env_args = {"fast_obs": True}

# env = gym.make(env_name, **env_args)

# obs = env.reset()  # a tuple of observations

# for step in range(10):
#     actions = env.action_space.sample()  # a tuple of actions
#     print(actions)  # (2, 0, 1, 3)  four agents
#     obs, reward, done, info = env.step(actions)
#     print(done)    # [False, False]
#     print(reward)  # [0.0, 0.0]

#     env.render()
#     print()

# env.close()

# When slow obs, the data like below: (default is fast_obs, that also have information about shelves)
# {
# 'self': 
#     {
#         'location': array([5, 4]), 
#         'carrying_shelf': [0], 
#         'direction': 1, 
#         'on_highway': [1]
#     }, 
# 'sensors': (
#       {'has_agent': [0], 'direction': 0, 'local_message': [], 'has_shelf': [0], 'shelf_requested': [0]}, 
#       {'has_agent': [0], 'direction': 0, 'local_message': [], 'has_shelf': [0], 'shelf_requested': [0]}, 
#       {'has_agent': [0], 'direction': 0, 'local_message': [], 'has_shelf': [0], 'shelf_requested': [0]}, 
#       {'has_agent': [0], 'direction': 0, 'local_message': [], 'has_shelf': [0], 'shelf_requested': [0]}, 
#       {'has_agent': [1], 'direction': 1, 'local_message': array([], dtype=float64), 'has_shelf': [0], 'shelf_requested': [0]}, 
#       {'has_agent': [0], 'direction': 0, 'local_message': [], 'has_shelf': [0], 'shelf_requested': [0]}, 
#       {'has_agent': [0], 'direction': 0, 'local_message': [], 'has_shelf': [0], 'shelf_requested': [0]}, 
#       {'has_agent': [0], 'direction': 0, 'local_message': [], 'has_shelf': [0], 'shelf_requested': [0]}, 
#       {'has_agent': [0], 'direction': 0, 'local_message': [], 'has_shelf': [0], 'shelf_requested': [0]}
#     )
# }

# Get the list of all registered environments
import PettingZoo
envs = gym.envs.registry

# Print them nicely
for env in envs.env_specs:
    print(env)

# rware-1color-tiny-1ag-easy-v1
# rware-2color-tiny-1ag-easy-v1
# rware-3color-tiny-1ag-easy-v1
# rware-4color-tiny-1ag-easy-v1
# rware-1color-tiny-2ag-easy-v1
# rware-2color-tiny-2ag-easy-v1
# rware-3color-tiny-2ag-easy-v1
# rware-4color-tiny-2ag-easy-v1
# ....
# rware-1color-large-19ag-hard-v1
# rware-2color-large-19ag-hard-v1
# rware-3color-large-19ag-hard-v1
# rware-4color-large-19ag-hard-v1
