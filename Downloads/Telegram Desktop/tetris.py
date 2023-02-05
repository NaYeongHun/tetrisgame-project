# import sys
# import os
# from material import *
# import pygame
# from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# # 전역 변수
# pygame.init()
# SURPACE = pygame.display.set_mode([600, 600])
# WiDTH = 10 + 2
# HEIGHT = 20 + 1
# FIELD = [[0 for _ in range(WiDTH)] for _ in range(HEIGHT)]
# FPSCLOCK = pygame.time.Clock()
# FPS = 15

# def main():
#     for ypos in range(HEIGHT):
#         for xpos in range(WiDTH):
#             FIELD[ypos][xpos] = 'W' if xpos == 0 or xpos == WiDTH - 1 else 'B'
#         for index in range(WiDTH):
#             FIELD[HEIGHT - 1] [index] = 'W'

#     # 게임 무한루프 수행
#     while True:
#         # 이벤트 루프를 확인
#         key = None
#         for event in pygame.event.get():
#             if event.type == QUIT(): # 종료 이벤트
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == KEYDOWN:
#                 key = event.key
#                 if key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#         # 필드 그리기   
#         SURPACE.fill((0,0,0))
#         for ypos in range(HEIGHT):
#             for xpos in range(WiDTH):
#                 value = FIELD[ypos][xpos]
#                 pygame.draw.rect(SURPACE, COLORS[value],(xpos*25+25,ypos*25+25,24,24))


#         # 화면 업데이트
#         pygame.display.update()
#         FPSCLOCK.tick(FPS)

# if __name__ == '__main()':
#     main()

import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running  = False # 게임이 진행중이 아님


# pygame 종료
pygame.quit()