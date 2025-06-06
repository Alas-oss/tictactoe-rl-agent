# tictactoe-rl-agent

A reinforcement learning agent that learns to play TicTacToe using **Temporal Difference Learning (TD(0))** and an **ε-greedy exploration strategy**. This project was completed as part of an academic coursework for reinforcement learning and game AI.

## Features

- Text-based 3x3 TicTacToe implementation in Python.
- Supports three player types: Human, Random AI, and RL Agent.
- TD(0)-based learning with tunable hyperparameters.
- ELO-based performance evaluation after training.
- Includes functionality to **train**, **save**, and **evaluate** the RL policy.

# Algorithms & Approach

This project uses:
- **Temporal Difference Learning (TD(0))** for state-value updates.
- An **ε-greedy policy** to balance exploration vs. exploitation.
- A reward scheme designed and implemented by the student.
- Game state encoding using `getKey()` to map 2D board states to RL values.

### TD(0) Update Equation:
\[
V(S_t) = V(S_t) + \alpha \left[R_{t+1} + \gamma V(S_{t+1}) - V(S_t)\right]
\]

Where:
- \( \alpha \): Learning rate
- \( \gamma \): Discount factor
- \( \epsilon \): Exploration rate
- \( V(S) \): Value function over state `S`

# Hyperparameters used during training
learning_rate = 0.15
discount_rate = 0.9
epsilon = 0.2
episodes = 5000

Agents   | Won | Lost | Draw | Rating
---------|-----|------|------|--------
RL Agent |  6  |  2   |  2   | 1241.6
Random   |  2  |  6   |  2   | 1158.4

## Attribution

- Base code originally authored by **Dr. Jeffery Raphael** for KCL CS Coursework (2024).
- RL agent implementation, training pipeline, reward function, and performance evaluation by **Aliya Alasgarova** (2025).
- This project is used with permission from the original author.

- > This repository includes modified coursework originally developed by Dr. Jeffery Raphael and distributed as part of CS module homework at King’s College London. It is republished here with written permission for educational and portfolio purposes.
