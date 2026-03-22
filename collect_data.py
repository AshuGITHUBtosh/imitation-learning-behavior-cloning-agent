import pygame
import csv
import random
import math

WIDTH, HEIGHT = 600, 600
STEP = 20
TARGET_RADIUS = 25

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Collection")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

agent_pos = [100, 100]

def get_new_target():
    return [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)]

target_pos = get_new_target()

data = []
score = 0

def get_action(keys):
    if keys[pygame.K_UP]:
        return 0
    if keys[pygame.K_DOWN]:
        return 1
    if keys[pygame.K_LEFT]:
        return 2
    if keys[pygame.K_RIGHT]:
        return 3
    return None

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

running = True
while running:
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0,255,0), agent_pos, 10)
    pygame.draw.circle(screen, (255,0,0), target_pos, TARGET_RADIUS)

    score_text = font.render(f"Targets: {score}", True, (255,255,255))
    screen.blit(score_text, (10, 10))

    keys = pygame.key.get_pressed()
    action = get_action(keys)

    if action is not None:
        if action == 0: agent_pos[1] -= STEP
        elif action == 1: agent_pos[1] += STEP
        elif action == 2: agent_pos[0] -= STEP
        elif action == 3: agent_pos[0] += STEP

        # boundary
        agent_pos[0] = max(0, min(WIDTH, agent_pos[0]))
        agent_pos[1] = max(0, min(HEIGHT, agent_pos[1]))

        # ✅ RELATIVE STATE
        dx = target_pos[0] - agent_pos[0]
        dy = target_pos[1] - agent_pos[1]

        data.append([dx, dy, action])

    if distance(agent_pos, target_pos) < TARGET_RADIUS:
        score += 1
        target_pos = get_new_target()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)

with open("data/demo_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

pygame.quit()

print(f"Saved {len(data)} samples")