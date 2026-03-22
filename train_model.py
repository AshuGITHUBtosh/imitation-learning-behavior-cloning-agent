import torch
import pandas as pd
from model import BCModel

# Load data
data = pd.read_csv("data/demo_data.csv", header=None)

X = data.iloc[:, :2].values.astype('float32')
y = data.iloc[:, 2].values

# ✅ NORMALIZE
X /= 600.0

X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)

model = BCModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.CrossEntropyLoss()

for epoch in range(100):
    logits = model(X)
    loss = loss_fn(logits, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

torch.save(model.state_dict(), "bc_model.pth")

print("Model saved!")