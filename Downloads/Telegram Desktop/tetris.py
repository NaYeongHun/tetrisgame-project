import pygame
from copy import deepcopy
from random import choice, randrange

WEIGHT, HEIGHT = 10, 20
TILE = 45
GAME_RES = WEIGHT * TILE, HEIGHT * TILE
RES = 750, 950
FPS = 60

# 초기화
pygame.init()

# 스크린 생성 하고 이미지 위치하는 곳
FULL_SURPACE = pygame.display.set_mode(RES)
SURPACE= pygame.Surface(GAME_RES)
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
field = [[0 for i in range(WEIGHT)] for j in range(HEIGHT)]

# 속도와 y축 대한 변수
count, speed, limit = 0, 60, 2000

block = deepcopy(choice(blocks))
# 다음 블록
next_block = deepcopy(choice(blocks))

# 타이틀(제목)
main_font = pygame.font.Font('font/font.ttf',65)
# font = pygame.font.Font('font/font.ttf',45)

title_tetris = main_font.render('테트리스', True, pygame.Color('white'))

# 블록 색깔 랜덤으로 정해주기
get_color = lambda : (randrange(30,256),randrange(30,256),randrange(30,256))
color = get_color()
# 다음 블록 색깔
next_color = get_color()
#블록이 벽을 벗어나지 않게 해주는 코드
def check_borders():
    if block[i].x < 0 or block[i].x > WEIGHT - 1:
        return False

    # 맨 밑에 막아주기(쌓기)    
    elif block[i].y > HEIGHT - 1 or field[block[i].y][block[i].x]:
        return False
    return True

while True:
    # x축 이동
    dx = 0
    # 블록 회전
    rotate = False
    # 게임공간 공간늘리기.blit()
    FULL_SURPACE.blit(SURPACE,(20,20))
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
            # 다운 키를 눌렀을때 빨리 내려오기
            elif event.key == pygame.K_DOWN:
                limit = 100
            # 블록 회전
            elif event.key == pygame.K_UP:
                rotate =True

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
                for i in range(4):
                    field[block_old[i].y][block_old[i].x] = color

                block = next_block
                color = next_color
                next_block = deepcopy(choice(blocks))
                next_color = get_color()
                # color = get_color()
                # block =deepcopy(choice(blocks))
                # 이 숫자가 커야 다음 블록도 빨리 안떨어짐
                limit =2000
                break

    # 블록 회전하기
    # 가운데를 기준으로 돌리기
    center = block[0]
    block_old = deepcopy(block)
    if rotate :
        for i in range(4):
            x = block[i].y - center.y
            y = block[i].x - center.x
            block[i].x = center.x - x
            block[i].y = center.y + y
            if not check_borders():
                block =deepcopy(block_old)
                break

    # 밑에 줄 차면 지우기
    line = HEIGHT - 1
    for row in range(HEIGHT - 1, -1, -1):
        del_count = 0
        for i in range(WEIGHT):
            if field[row][i]:
                del_count += 1
            field[line][i] = field[row][i]
        if del_count < WEIGHT:
            line -= 1

    # 격자(화면) 그리기
    [pygame.draw.rect(SURPACE,(40,40,40), i_rect,1) for i_rect in grid]

    # 하나 블록 그리기
    for i in range(4):
        block_rect.x =block[i].x * TILE
        block_rect.y =block[i].y * TILE
        pygame.draw.rect(SURPACE, color, block_rect)

    # 필드 그리기
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                block_rect.x, block_rect.y = x * TILE, y * TILE
                pygame.draw.rect(SURPACE, col, block_rect)

    # 다음 블록 그리기
    for i in range(4):
        block_rect.x = next_block[i].x * TILE + 380
        block_rect.y = next_block[i].y * TILE + 180
        pygame.draw.rect(FULL_SURPACE, next_color, block_rect)  

    # 타이틀(제목 삽입)
    FULL_SURPACE.blit(title_tetris,(480,10))    

    pygame.display.flip()
    clock.tick(FPS)
