import numpy as np
import random

# Define the environment (5x5 grid)
grid_size = 5
goal_state = (4, 4)
obstacle_states = [(1, 1), (2, 2), (3, 3)]

# Initialize the Q-table
q_table = np.zeros((grid_size, grid_size, 4))  # 4 possible actions: up, down, left, right

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 1000

# Action space (up, down, left, right)
actions = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

def get_next_state(state, action):
    new_state = (state[0] + actions[action][0], state[1] + actions[action][1])
    if 0 <= new_state[0] < grid_size and 0 <= new_state[1] < grid_size and new_state not in obstacle_states:
        return new_state
    else:
        return state  # Stay in the same state if moving out of bounds or into an obstacle

def get_reward(state):
    if state == goal_state:
        return 10  # Reward for reaching the goal
    else:
        return -1  # Small penalty for each step

# Q-learning algorithm
for episode in range(episodes):
    state = (0, 0)  # Start at the top-left corner

    while state != goal_state:
        if random.uniform(0, 1) < epsilon:
            # Explore: choose a random action
            action = random.choice(list(actions.keys()))
        else:
            # Exploit: choose the best action based on Q-table
            action = np.argmax(q_table[state[0], state[1]])

        next_state = get_next_state(state, action)
        reward = get_reward(next_state)

        # Update Q-value using the Q-learning formula
        q_table[state[0], state[1], action] = q_table[state[0], state[1], action] + \
            alpha * (reward + gamma * np.max(q_table[next_state[0], next_state[1]]) - q_table[state[0], state[1], action])

        state = next_state

# Print the learned Q-values
print("Learned Q-table:")
print(q_table)

# Simulate the learned policy
state = (0, 0)
steps = 0
print("\nSimulating the learned policy:")
while state != goal_state and steps < 20:
    action = np.argmax(q_table[state[0], state[1]])
    print(f"State: {state} -> Action: {action}")
    state = get_next_state(state, action)
    steps += 1

if state == goal_state:
    print(f"Reached the goal in {steps} steps!")
else:
    print("Did not reach the goal.")
