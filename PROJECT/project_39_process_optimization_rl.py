PROJECT = {
    "name": "Factory Process Optimization (Reinforcement Learning)",
    "icon": "🤖",
    "dataset": "Simulated Env (Gym)",
    "description": "Use RL (Q-learning) to optimize factory process steps.",
    "steps": "Define Env → Q-Learning → Improve Policy",
    "code": """
import numpy as np

# Simplified RL example
states = 5
actions = 3
Q = np.zeros((states, actions))

lr = 0.1
gamma = 0.9
episodes = 1000

for _ in range(episodes):
    s = np.random.randint(0, states)
    a = np.random.randint(0, actions)
    r = np.random.randn()  # random reward
    s_new = np.random.randint(0, states)

    Q[s,a] = Q[s,a] + lr * (r + gamma * np.max(Q[s_new]) - Q[s,a])

print("Optimized Q table:")
print(Q)
"""
}
