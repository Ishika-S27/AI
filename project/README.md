## 🧠 N-queens AI solver

The **N-Queen problem** is one of the most fundamental challenges in Artificial Intelligence and computer science.  
It involves placing *N queens* on an *N×N chessboard* so that no two queens threaten each other — i.e., no two share the same row, column, or diagonal.

This problem represents a **Constraint Satisfaction Problem (CSP)** and serves as a foundation for understanding **AI search strategies**, **optimization**, and **problem-solving logic**.  
The goal is not just to find one solution but to understand how intelligent systems explore possibilities and make decisions efficiently.

---

### 🔹 AI Concepts Behind the N-Queen Problem

1. **Search Space Exploration:**  
   Each configuration of queens represents a unique state in the search space.  
   The challenge lies in efficiently navigating this space to reach a valid configuration.

2. **Constraint Satisfaction:**  
   Every queen placement must satisfy specific constraints — no conflict along rows, columns, or diagonals.  
   The algorithms enforce these constraints while exploring possible states.

3. **Optimization:**  
   For large N, brute-force exploration becomes infeasible.  
   Heuristic and metaheuristic methods (like Hill Climbing and Genetic Algorithms) aim to *optimize* the search to find near-optimal solutions quickly.

---

### ⚙️ Algorithms Implemented

- **Backtracking:**  
  A classical depth-first search algorithm that tries all valid configurations recursively.  
  It is guaranteed to find a solution but can be slow for large N due to exponential growth.

- **Hill Climbing:**  
  A heuristic approach that starts with a random configuration and makes incremental improvements by reducing conflicts.  
  It’s faster but may get trapped in local minima.

- **Genetic Algorithm:**  
  Inspired by natural evolution, this method evolves a population of candidate solutions using selection, crossover, and mutation.  
  It balances exploration and exploitation to efficiently find valid configurations.

---

### 💡 Significance in AI
The N-Queen problem is not just a puzzle — it’s a **learning model for AI reasoning**.  
It demonstrates how machines can:
- Represent complex problems,
- Apply logic-based or evolutionary approaches,
- Learn to make decisions under constraints.

This project bridges **theory and practice**, showing how different AI paradigms approach the same problem with varying efficiency and intelligence.

---

### 👩‍💻 Authors
**Deepa & Ishika**  
Artificial Intelligence and Data Science (AI & DS)  
Yeshwantrao Chavan College of Engineering 
