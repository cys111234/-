# !usr/bin/env/python
# _*_coding:utf-8_*_
"""
代码功能需求：1在画布上整齐排列三张图片（应该会用到坐标）2供玩家选择，3将三张图片赋值再进行比对
如果大小不相等，进行下一轮比对，不计分；如果大小相等，两人各加10分，进行下一轮循环。直到100次来回结束为止
"""
import pygame
import sys
pygame.init()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE,)  # 注意是元组传递
pygame.display.set_caption("1")
# 颜色定义
White = (255, 255, 255)
Black = (0, 0, 0)
# 加载图片
try:
    image_path = "1.png"
    image = pygame.image.load(image_path).convert_alpha()
except:
    # 如果图片加载失败，创建一个替代的Surface
    image = pygame.Surface((400, 400))  # 传递参数为大小
    image.fill((100, 100, 150))
    """
    四个参数：Surface对象，颜色,位置及大小，矩形边框的宽度或者厚度
    第三个参数传递一个Rect对象或者一个元组，(left, top, width, height),左上角坐标位置
    """
    pygame.draw.rect(image, (0, 255, 0), (200, 200, 300, 300), 3)
    font = pygame.font.SysFont(None, 30)
    text = font.render("布图片未找到", True, White)
    image.blit(text, (300, 300))
# 获取图片的矩形区域，用于定位
image_rect = image.get_rect()
image_rect.center = (screen_width // 4, screen_height // 4)
try:
    image2_path = "2.png"
    image2 = pygame.image.load(image2_path).convert_alpha()
# 上面失败则采用下面的应对方案
except:
    image2 = pygame.Surface((400, 400))  # 参数数值与上相同，第一步先绘制画布
    image2.fill((255, 0, 0))  # 第二步给画布填充颜色
    pygame.draw.rect(image2, (0, 255, 0), (200, 400, 300, 300), 3)  # 第三步绘制矩形区域
    font = pygame.font.SysFont(None, 30)  # 第四步创建字体变量
    text = font.render("石头图片未找到", True, Black)  # 第五步调用字体库方法创建文本框
    image2.blit(text, (300, 500))  # 第六步绘制带文本框的图片（或者Surface对象）
# 第七步定位矩形框
image2_rect = image.get_rect()
image2_rect.center = (screen_width // 4, 500)
image3_path = "3.png"
image3 = pygame.image.load(image3_path).convert_alpha()
image3_rect = image.get_rect()
image3_rect.center = (300, 700)
image4_path = "1.png"
image4 = pygame.image.load(image4_path).convert_alpha()
image4_rect = image.get_rect()
image4_rect.center = (900, 200)
image5_path = "2.png"
image5 = pygame.image.load(image5_path).convert_alpha()
image5_rect = image.get_rect()
image5_rect.center = (900, 500)
image6_path = "3.png"
image6 = pygame.image.load(image6_path).convert_alpha()
image6_rect = image.get_rect()
image6_rect.center = (900, 700)

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    # screen.blit(image, image_rect)  # 这行代码如果放在上面，图片则不能加载。原因：覆盖。
    # screen屏幕，Surface对象绘制在这个Screen上，这行代码如果先执行，那么会被接下来的接收了参数的Screen覆盖
    screen.fill((255, 255, 255))  # 报错的原因是没有传递元组，不符合规范  # 清屏操作
    screen.blit(image, image_rect)
    screen.blit(image2, image2_rect)
    screen.blit(image3, image3_rect)
    screen.blit(image4, image4_rect)
    screen.blit(image5, image5_rect)
    screen.blit(image6, image6_rect)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
sys.exit()
