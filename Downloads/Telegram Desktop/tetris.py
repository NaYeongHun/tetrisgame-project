import pygame
from copy import deepcopy

WEIGHT, HEIGHT = 10, 20
TILE = 45
GAME_RES = WEIGHT * TILE, HEIGHT * TILE
FPS = 60

# 초기화
pygame.init()
# 스크린 생성 하고 이미지 위치하는 곳
SURPACE= pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

# 직사각형 좌표를 저장하기 위한 객체 : pygame.Rect
grid =[pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WEIGHT) for y in range(HEIGHT)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

# 2차원배열로 생성
blocks = [[pygame.Rect(x + WEIGHT// 2, y+1 , 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
block_rect = pygame.Rect(0, 0, TILE-2 , TILE-2 )

# 속도와 y축 대한 변수
count, speed, limit = 0, 60, 2000

block = deepcopy(blocks[3])

#블록이 벽을 벗어나지 않게 해주는 코드
def check_borders():
    if block[i].x < 0 or block[i].x > WEIGHT - 1:
        return False
    return True

while True:
    # x축 이동
    dx = 0
    SURPACE.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # x축 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx =-1
            elif event.key == pygame.K_RIGHT:
                dx = 1

    # 격자(화면) 그리기
    [pygame.draw.rect(SURPACE,(40,40,40), i_rect,1) for i_rect in grid]

    # x측 음직이기
    block_old = deepcopy(block)
    for i in range(4):
        block[i].x += dx
        if not check_borders():
                block =deepcopy(block_old)
                break
    # y축 움직이기
    count += speed
    if count > limit:
        count = 0
        block_old = deepcopy(block)
        for i in range(4):
            block[i].y += 1
            if not check_borders():
                    block =deepcopy(block_old)
                    break

    # 하나 블록 그리기
    for i in range(4):
        block_rect.x =block[i].x * TILE
        block_rect.y =block[i].y * TILE
        pygame.draw.rect(SURPACE, pygame.Color('white'),block_rect)
    

    pygame.display.flip()
    clock.tick(FPS)
