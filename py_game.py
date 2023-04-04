import pygame

# initialize Pygame
pygame.init()

# create the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# set up the game objects
ball = pygame.Rect(screen_width//2 - 10, screen_height//2 - 10, 20, 20)
paddle1 = pygame.Rect(50, screen_height//2 - 70, 20, 140)
paddle2 = pygame.Rect(screen_width - 70, screen_height//2 - 70, 20, 140)
ball_speed_x, ball_speed_y = 7, 7
paddle_speed = 10

# set up the game loop
clock = pygame.time.Clock()
game_running = True

# game loop
while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    # handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and paddle1.bottom < screen_height:
        paddle1.move_ip(0, paddle_speed)
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN] and paddle2.bottom < screen_height:
        paddle2.move_ip(0, paddle_speed)
    
    # update game objects
    ball.move_ip(ball_speed_x, ball_speed_y)
    if ball.top < 0 or ball.bottom > screen_height:
        ball_speed_y *= -1
    if ball.left < 0:
        ball_speed_x *= -1
    if ball.right > screen_width:
        ball_speed_x *= -1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    
    # draw game objects
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    
    # update the screen
    pygame.display.update()
    
    # limit the frame rate
    clock.tick(60)

# quit Pygame
pygame.quit()
