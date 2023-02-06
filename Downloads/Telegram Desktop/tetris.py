import pygame

WEIGHT, HEIGHT = 10, 20
TILE = 45
GAME_RES = WEIGHT * TILE, HEIGHT * TILE
FPS = 60

# 초기화
pygame.init()
SURPACE= pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

grid =[pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WEIGHT) for y in range(HEIGHT)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

blocks = [[pygame.Rect(x + WEIGHT// 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
block_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)

block = blocks[0]

while True:
    SURPACE.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # 격자(화면) 그리기
    [pygame.draw.rect(SURPACE,(40,40,40), i_rect,1) for i_rect in grid]

    # 블록 그리기
    for i in range(4):
        block_rect.x =block[i].x * TILE
        block_rect.y =block[i].y * TILE
        pygame.draw.rect(SURPACE, pygame.Color('white'),block_rect)
    

    pygame.display.flip()
    clock.tick(FPS)
