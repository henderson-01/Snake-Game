import pygame
import random
import sys


pygame.init()

# Define Colors
NOKIA_GREEN = (199, 240, 216)  # C7F0D8
NOKIA_DARK = (67, 82, 61)  # #43523D
# Additional colors for game over message/highlights if needed
RED = (213, 50, 80)


# Display Dimensions
DIS_WIDTH = 550
DIS_HEIGHT = 500

dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

SNAKE_BLOCK = 15  # Increased block size for better visibility
SNAKE_SPEED = 8

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Score: " + str(score), True, NOKIA_DARK)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, NOKIA_DARK, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    # Center the message
    text_rect = mesg.get_rect(center=(DIS_WIDTH / 2, DIS_HEIGHT / 2))
    dis.blit(mesg, text_rect)


def gameLoop():
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    # Align starting position to grid
    x1 = round(x1 / SNAKE_BLOCK) * SNAKE_BLOCK
    y1 = round(y1 / SNAKE_BLOCK) * SNAKE_BLOCK

    x1_change = SNAKE_BLOCK
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Place food randomly aligned with the grid
    foodx = (
        round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    )
    foody = (
        round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    )

    while not game_over:
        while game_close:
            dis.fill(NOKIA_GREEN)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        input_processed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and not input_processed:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                    input_processed = True
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                    input_processed = True
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                    input_processed = True
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0
                    input_processed = True

        # Boundary Conditions (Wall Collision)
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(NOKIA_GREEN)

        # Draw Food
        pygame.draw.rect(dis, NOKIA_DARK, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        # Snake Movement Logic
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Self Collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Eating Food
        if x1 == foodx and y1 == foody:
            foodx = (
                round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK)
                * SNAKE_BLOCK
            )
            foody = (
                round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK)
                * SNAKE_BLOCK
            )
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    gameLoop()
