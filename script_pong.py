import pygame
import random

# Initialization

pygame.init()
run = True
clock = pygame.time.Clock()

# Window

win_width = 700
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pong")

# Classes


class Ball(object):
    def __init__(self):
        self.radius = 10
        self.color = (255, 255, 255)
        self.facing_x = random.choice([1, -1])
        self.facing_y = random.choice([1, -1])
        self.vel = 3
        self.x = win_width // 2 - self. radius
        self.y = win_height // 2 - self.radius

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.vel * self.facing_x
        self.y += self.vel * self.facing_y


class Player(object):
    width = 10
    height = 80
    color = (255, 250, 255)
    vel = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0

    def draw(self):
        pygame.draw.rect(win, Player.color,
                         (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y-Player.vel >= 5:
            self.y -= Player.vel

    def move_down(self):
        if self.y+Player.vel <= 495-Player.height:
            self.y += Player.vel

    def draw_score(self):
        pass


def RedrawGameWindow():
    win.fill((0, 0, 0))
    ball.draw()
    player1.draw()
    player2.draw()
    text = font.render(
        f"{player1.score} --- {player2.score}", 1, (255, 255, 255))
    win.blit(text, (win_width // 2 - 30, 10))


ball = Ball()

player1 = Player(10, ((win_height // 2 - Player.height//2)))
player2 = Player(win_width-16, (win_height // 2 - Player.height//2))

font = pygame.font.SysFont("comicsans", 30, True)

# Main Loop

while run:

    clock.tick(100)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Ball collision
    # Top
    if ball.y-(4*ball.vel) < 10:
        ball.facing_y *= -1

    # Bottom
    if ball.y+(4*ball.vel) > 500:
        ball.facing_y *= -1

    # Player 1 (Point for Player 2)

    if ball.x < -20:
        player2.score += 1
        ball = Ball()

    # Player 2 (Point for Player 1)

    if ball.x > win_width+20:
        player1.score += 1
        ball = Ball()

# Bouncing of Player
    # Player 1
    if ball.x <= 30 and ball.y-ball.radius <= player1.y + player1.height and ball.y + ball.radius >= player1.y:
        ball.facing_x *= -1

    # Player 2
    if ball.x >= win_width - 30 and ball.y-ball.radius <= player2.y + player2.height and ball.y + ball.radius >= player2.y:
        ball.facing_x *= -1

# Player 1 movement

    if keys[pygame.K_w]:
        player1.move_up()

    if keys[pygame.K_s]:
        player1.move_down()

# Player 2 movement

    if keys[pygame.K_UP]:
        player2.move_up()

    if keys[pygame.K_DOWN]:
        player2.move_down()

    ball.move()
    RedrawGameWindow()
    pygame.display.flip()


pygame.quit()
