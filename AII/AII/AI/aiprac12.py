import numpy as np
import random
import matplotlib.pyplot as plt

# Environment parameters
grid_size = 5
goal_state = (4, 4)
n_actions = 4  # up, down, left, right
actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Move right, down, left, up

# Q-Table initialization
Q = np.zeros((grid_size, grid_size, n_actions))

# Parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 1000

# Helper function to get the next state
def get_next_state(state, action):
    new_state = (state[0] + action[0], state[1] + action[1])
    # Ensure the new state is within bounds
    if 0 <= new_state[0] < grid_size and 0 <= new_state[1] < grid_size:
        return new_state
    return state  # If out of bounds, stay in the same state

# Training the agent
for episode in range(episodes):
    state = (0, 0)  
    total_reward = 0
    while state != goal_state:
       
        if random.uniform(0, 1) < epsilon:
            action_index = random.randint(0, n_actions - 1)  
        else:
            action_index = np.argmax(Q[state[0], state[1]])  

        action = actions[action_index]
        next_state = get_next_state(state, action)
        reward = 10 if next_state == goal_state else -1

       
        best_next_action = np.max(Q[next_state[0], next_state[1]])
        Q[state[0], state[1], action_index] = (
            Q[state[0], state[1], action_index] +
            alpha * (reward + gamma * best_next_action - Q[state[0], state[1], action_index])
        )

        state = next_state
        total_reward += reward

    if episode % 100 == 0:
        print(f"Episode {episode}: Total Reward = {total_reward}")

print("Training complete!")


def plot_q_values(Q):
    fig, axs = plt.subplots(1, n_actions, figsize=(15, 5))
    for i in range(n_actions):
        ax = axs[i]
        ax.imshow(Q[:, :, i], cmap='viridis', vmin=0, vmax=np.max(Q))
        ax.set_title(f'Action {i}')
        ax.set_xticks(np.arange(grid_size))
        ax.set_yticks(np.arange(grid_size))
        ax.set_xticklabels(np.arange(grid_size))
        ax.set_yticklabels(np.arange(grid_size))
        for (j, k), val in np.ndenumerate(Q[:, :, i]):
            ax.text(k, j, f'{val:.2f}', ha='center', va='center', color='white')
    plt.tight_layout()
    plt.show()

plot_q_values(Q)

#
