import pygame
import random


pygame.init()
clock = pygame.time.Clock()

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

FONT = pygame.font.SysFont("comicsans", 30, True)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Ball(object):
    def __init__(self):
        self.radius = 10
        self.color = WHITE
        self.facing_x = random.choice([1, -1])
        self.facing_y = random.choice([1, -1])
        self.vel = 3
        self.x = WINDOW_WIDTH // 2 - self.radius
        self.y = WINDOW_HEIGHT // 2 - self.radius

    def draw(self):
        pygame.draw.circle(WINDOW, self.color, (self.x, self.y), self.radius)

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
        pygame.draw.rect(WINDOW, Player.color,
                         (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y - Player.vel >= 5:
            self.y -= Player.vel

    def move_down(self):
        if self.y + Player.vel <= 495 - Player.height:
            self.y += Player.vel

    def draw_score(self):
        pass


def main():
    ball = Ball()

    player1 = Player(10, ((WINDOW_HEIGHT // 2 - Player.height // 2)))
    player2 = Player(
        WINDOW_WIDTH - 16, (WINDOW_HEIGHT // 2 - Player.height // 2))

    while True:
        clock.tick(100)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

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

        # Ball collision
        # Player 1 misses (Point for Player 2)
        if ball.x < -20:
            player2.score += 1
            ball = Ball()

        # Player 2 misses (Point for Player 1)
        if ball.x > WINDOW_WIDTH + 20:
            player1.score += 1
            ball = Ball()

        # Top
        if ball.y-(4 * ball.vel) < 10:
            ball.facing_y *= -1

        # Bottom
        if ball.y + (4 * ball.vel) > 500:
            ball.facing_y *= -1

        # Bouncing of Players
        # Player 1
        if ball.x <= 30 and ball.y-ball.radius <= player1.y + player1.height and ball.y + ball.radius >= player1.y:
            ball.facing_x *= -1

        # Player 2
        if ball.x >= WINDOW_WIDTH - 30 and ball.y-ball.radius <= player2.y + player2.height and ball.y + ball.radius >= player2.y:
            ball.facing_x *= -1

        ball.move()
        draw(ball, player1, player2)
        pygame.display.flip()


def draw(ball, player1, player2):
    WINDOW.fill(BLACK)
    ball.draw()
    player1.draw()
    player2.draw()
    text = FONT.render(
        f"{player1.score} --- {player2.score}", 1, (255, 255, 255))
    WINDOW.blit(text, (WINDOW_WIDTH // 2 - 30, 10))


if __name__ == "__main__":
    main()
