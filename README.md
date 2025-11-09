# 🤖 Artificial Intelligence Practicals

## 🎯 Course Outcomes

1. **Understand** appropriate performance measures and environment models for intelligent agents.  
2. **Apply** various search algorithms for goal-based problem solving and planning in deterministic and non-deterministic environments.  
3. **Construct** and apply suitable knowledge representation models for logical inference.  
4. **Analyze and solve** problems under uncertainty using probabilistic models and decision-theoretic reasoning.  

---

## 🧠 Practical 1: Smart Light Control using Simple Reflex Agent

**Title:** Smart Light Agent (Simple Reflex Agent)  
**Problem Statement:**  
Design and implement a simple reflex agent to simulate a smart light system for a room.  

**Description:**  
The agent decides whether to turn the indoor light **ON** or **OFF** based on two percepts:
- **Outside Light:** Sunlight available or not  
- **Human Presence:** Someone present in the room or not  

**Behavior Rules:**
- If **human is present** and **outside light is not available** → Turn **ON** the light  
- In all other cases → Turn **OFF** the light  

---

## 🧹 Practical 2: Two-Room Vacuum Cleaner Agent Simulation

**Problem Statement:**  
Implement a vacuum cleaner agent that works in a two-room environment: **Room A** and **Room B**.  
Each room may be **clean** or **dirty**.  

**Agent Rules:**
- If the current room is **dirty**, **clean it**  
- If the current room is **clean**, **move to the other room**  
- Continue until **both rooms are clean**  

---

## 🗺️ Practical 3: Shortest Path Using Greedy Best-First Search

**Problem Statement:**  
An AI agent must reach the goal cell on a grid as fast as possible using **Greedy Best-First Search**.  

**Heuristic Used:**  
- **Manhattan Distance** to estimate closeness to the goal.  

**Strategy:**  
- Always choose the next cell that **appears closest** to the goal.  

**Example Grid (5x5):**
S . . . .
. X X . .
. . X . .
. X . . G


---

## 🚗 Practical 4: Optimal Path Using A* Search

**Problem Statement:**  
A robot moves in a city map where each move has a **cost** (traffic or terrain).  
The goal is to find the **lowest-cost path** to the destination using **A\*** Search.  

**Concepts:**
- Combines **actual cost (g)** and **heuristic (h)** → `f(n) = g(n) + h(n)`  

**Example Map (Grid + Weights):**
[1, 1, 5]
[1, X, 1]
[1, 1, 1]


---

## 🛣️ Practical 5: AI Route Planner using Greedy and A* Search

**Problem Statement:**  
A self-driving car must navigate from a **source** to a **destination** on a city grid.  
Each block may have **obstacles** or **traffic delays**.  

**Tasks:**
- Implement and compare:
  - **Greedy Best-First Search** → Focuses only on closeness  
  - **A\*** → Considers both cost and heuristic  

**Heuristic Used:**  
- **Manhattan Distance**

**Comparison:**  
Evaluate both algorithms based on **path efficiency** and **total cost**.  

---

## 🗺️ Practical 6: Map Coloring for Adjoining Regions using Min-Conflicts

**Problem Statement:**  
Given a map with 5 regions (**A, B, C, D, E**) where some regions share borders,  
assign colors such that **no two neighboring regions** have the same color.  

**Concepts Used:**
- **Constraint Satisfaction Problem (CSP):**
  - **Variables:** Regions (A, B, C, D, E)  
  - **Domains:** 3 colors  
- **Local Search Algorithm:** **Min-Conflicts**

**Goal:**  
Color all regions using **3 colors** with **no color conflicts** between neighbors.  

---

## 🧩 Topics Covered
- Intelligent Agents and Environment Models  
- Search Algorithms: Greedy Best-First, A\*  
- Knowledge Representation and Reasoning  
- Constraint Satisfaction and Local Search  
- Simple Reflex and Goal-Based Agents  

---
