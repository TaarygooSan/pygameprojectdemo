# -*- coding:utf-8 -*-
"""
作者：TaarygooSan
日期：2021年07月03日

 常用快捷键
 行首：Home
 行尾：End
 快速修正：Alt+Enter
 快速注释：Ctrl+/
 复制代码：Ctrl+D
 删除代码：Ctrl+Y
 复写代码：Ctrl+O
 选中代码或代码块：Ctrl+W
 快速查看文档：Ctrl+Q
 模块或项目重命名：Shift+F6
 向下插入一行：Shift+Enter
 向上插入一行：Ctrl+Alt+Enter

 快速进入代码；Ctrl+左键 或 Ctrl+B
 快速查看历史：Alt+左键 （与快速进入代码搭配使用进行快速跳转）
 快速切换方法：Alt+上下键

 切换视图：Ctrl+Tab
 查看资源文件：双击Shift
 查看方法在哪里被调用：Ctrl+Alt+H
 查看父类：Ctrl+U
 查看继承关系：Ctrl+H
"""

import pygame, sys  # 引用库

pygame.init()  # 初始化，必须
vInfo = pygame.display.Info()  # 获得当 前窗口信息
size = width, height = 400, 600
# size = width, height = vInfo.current_w, vInfo.current_h  # 设置窗口大小参数
# screen = pygame.display.set_mode(size)  # 生成窗口
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN)  # 生成窗口
screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # 生成窗口
speed = [1, 1]  # 设置速度列表
BLACK = 0, 0, 0  # RGB色域黑色
pygame.display.set_caption("pygame游戏之旅")  # 设置窗口名称
ball = pygame.image.load("PYG02-ball.gif")  # 导入图片，表示为surface对象
icon = pygame.image.load("ningmeng.png")
pygame.display.set_icon(icon)
ballrect = ball.get_rect()  # 返回覆盖图像的矩形Rect对象
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            #     esc退出游戏
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        #         跟随窗体变化改变窗体大小
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    if pygame.display.get_active():                   # 当窗口没有被最小化时
        ballrect = ballrect.move(speed[0], speed[1])  # 移动矩形
    # 设置反弹
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(BLACK)  # 填充背景颜色
    screen.blit(ball, ballrect)  # 将ball图像绘制到ballrect矩形上
    pygame.display.update()  # 刷新屏幕
    fclock.tick(fps)
