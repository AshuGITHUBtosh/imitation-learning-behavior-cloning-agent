# Imitation Learning Agent (Behavior Cloning)

## 📌 Overview

This project demonstrates **Imitation Learning using Behavior Cloning**, where an agent learns to navigate toward a target by mimicking human demonstrations.

A neural network is trained on state-action pairs collected from manual control and then deployed to autonomously control the agent in a closed-loop environment.

---


### 1. Data Collection

* The user controls the agent using arrow keys
* The system records:

  ```
  (dx, dy) → action
  ```
* Where:

  * `dx = target_x - agent_x`
  * `dy = target_y - agent_y`

---

### 2. Model Training

* A feedforward neural network is trained using:

  * Input: `(dx, dy)`
  * Output: Action (Up, Down, Left, Right)
* Loss function: CrossEntropyLoss
* Optimizer: Adam

---

### 3. Inference (Deployment)

* The trained model predicts actions in real time
* The agent continuously updates its movement based on current state

---

## Project Structure

```
imitation_learning_project/
│
├── data/
│   └── demo_data.csv
│
├── collect_data.py   # Collect human demonstrations
├── train_model.py    # Train behavior cloning model
├── run_agent.py      # Run trained agent
├── model.py          # Neural network definition
```

---

## How to Run

### 1️⃣ Install dependencies

```bash
pip install pygame torch pandas
```

---

### 2️⃣ Collect Data

```bash
python collect_data.py
```

* Use arrow keys to move toward the red target
* Play for ~5–10 minutes

---

### 3️⃣ Train Model

```bash
python train_model.py
```

---

### 4️⃣ Run Agent

```bash
python run_agent.py
```

---

## 📊 Results

* The trained agent successfully learns to:

  * Move toward the target
  * Adapt movement based on relative position
* Using relative state `(dx, dy)` significantly improves performance over absolute coordinates

---

## 🧠 Key Learnings

* Behavior cloning is a form of supervised learning applied to control tasks
* State representation is critical for generalization
* Closed-loop systems introduce challenges like error accumulation (distribution shift)

