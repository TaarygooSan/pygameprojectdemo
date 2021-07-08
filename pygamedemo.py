# -*- coding:utf-8 -*-
"""
作者：TaarygooSan
日期：2021年07月08日

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
import sys, pygame

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("PYG02-ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
