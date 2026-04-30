import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
BALL_RADIUS = 15
WHITE = (255, 255, 255)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Paddles and ball setup
left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Speeds
ball_speed_x = 7
ball_speed_y = 7
paddle_speed = 10

# Score variables
left_score = 0
right_score = 0
font = pygame.font.SysFont(None, 55)

# Function to draw everything
def draw():
        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Draw the center line
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        # Draw scores
        left_text = font.render(str(left_score), True, WHITE)
        screen.blit(left_text, (WIDTH // 4 - left_text.get_width() // 2, 20))
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width() // 2, 20))

        pygame.display.flip()

# Main game loop
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        # Paddle controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
                left_paddle.y -= paddle_speed
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
                left_paddle.y += paddle_speed
        if keys[pygame.K_UP] and right_paddle.top > 0:
                right_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
                right_paddle.y += paddle_speed

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball_speed_y = -ball_speed_y

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
                ball_speed_x = -ball_speed_x

        # Scoring
        if ball.left <= 0:
                right_score += 1
                ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
                ball_speed_x = -ball_speed_x
        if ball.right >= WIDTH:
                left_score += 1
                ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
                ball_speed_x = -ball_speed_x

        draw()
        pygame.time.Clock().tick(FPS)
