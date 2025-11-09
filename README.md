Develop an understanding to identify appropriate performance measures and environment models for intelligent agents.

Apply various search algorithms for goal-based problem solving and planning in deterministic and non-deterministic environments.

Construct and apply appropriate knowledge representation models for logical inference.

Analyze and solve problems under uncertainty using probabilistic models and decision-theoretic reasoning.

Practical 1: Smart Light Agent (Simple Reflex Agent)
Title: Smart Light Control using Simple Reflex Agent
Problem Statement:
Design and implement a simple reflex agent to simulate a smart light system for a room. The agent decides
whether to turn the indoor light ON or OFF based on two percepts:
Outside light (sunlight available or not)
Human presence (someone present in the room or not)
The light should behave as follows:
If human is present and outside light is not available, the agent should turn ON the light.
In all other cases, the light should be turned OFF.

Practical 2: Two-Room Vacuum Cleaner Agent Simulation
Problem Statement:
Implement a vacuum cleaner agent that works in a two-room environment: Room A and Room B. Each
room may be clean or dirty. The agent starts in Room A and follows a simple rule:
If the current room is dirty, clean it.
If the current room is clean, move to the other room.
Repeat until both rooms are clean.

Practical 3: Shortest Path Using Greedy Best-First Search
Problem Statement:
An AI agent must reach the goal cell on a grid as fast as possible. The agent uses a Greedy Best-
First Search strategy — always choosing the cell that looks closest to the goal using a Manhattan
distance heuristic.
Example Grid (5x5):
S . . . .
. X X . .
. . . X .
. X . . G

Practical 4: Optimal Path Using A Search*
Problem Statement:
A robot moves in a city map where each move has a cost (e.g., traffic or terrain). The goal is to
find the lowest cost path to the destination using A search*, combining actual cost and heuristic
(distance).
Map Example (Grid + Weights):
[1, 1, 5]
[1, X, 1]
[1, 1, 1]

Practical 5: AI Route Planner using Greedy and A* Search
Problem Statement:
A self-driving car must navigate from a source to a destination on a city grid. Each block may
have obstacles or traffic delays, and the car must find the best path using:
 Greedy Best-First Search (focuses only on closeness)
 A* (considers cost and heuristic)
Use a Manhattan distance heuristic to estimate proximity to the goal. Implement both algorithms
and compare the paths and cost.

Practical 6: Map Coloring for Adjoining Regions using Min-Conflicts
Problem Statement:
You are given a simple map of 5 regions (A, B, C, D, E), with a few of them sharing borders.
Color each region using only 3 colors such that no neighboring regions share the same color.
 AI Concepts:
 CSP (variables: regions, domains: 3 colors)
 Local search (min-conflicts algorithm)
