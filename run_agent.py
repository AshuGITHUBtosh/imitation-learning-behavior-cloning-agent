import pygame
import torch
import random
from model import BCModel

WIDTH, HEIGHT = 600, 600
STEP = 20
TARGET_RADIUS = 25

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Imitation Learning Agent")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Load model
model = BCModel()
model.load_state_dict(torch.load("bc_model.pth"))
model.eval()

agent_pos = [100, 100]

def get_new_target():
    return [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)]

target_pos = get_new_target()
score = 0

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

running = True
while running:
    screen.fill((0, 0, 0))

    # Draw agent and target
    pygame.draw.circle(screen, (0,255,0), agent_pos, 10)
    pygame.draw.circle(screen, (255,0,0), target_pos, TARGET_RADIUS)

    # Score display
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10, 10))

    # ✅ RELATIVE STATE (IMPORTANT FIX)
    dx = target_pos[0] - agent_pos[0]
    dy = target_pos[1] - agent_pos[1]

    state = torch.tensor([dx, dy], dtype=torch.float32)

    # ✅ NORMALIZE
    state /= 600.0

    # Predict action
    with torch.no_grad():
        action = torch.argmax(model(state)).item()

    # Move agent
    if action == 0: agent_pos[1] -= STEP
    elif action == 1: agent_pos[1] += STEP
    elif action == 2: agent_pos[0] -= STEP
    elif action == 3: agent_pos[0] += STEP

    # ✅ BOUNDARY CHECK
    agent_pos[0] = max(0, min(WIDTH, agent_pos[0]))
    agent_pos[1] = max(0, min(HEIGHT, agent_pos[1]))

    # ✅ TARGET RESET
    if distance(agent_pos, target_pos) < TARGET_RADIUS:
        score += 1
        target_pos = get_new_target()

    # Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(10)

pygame.quit()