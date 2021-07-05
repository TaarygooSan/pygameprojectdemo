# -*- coding:utf-8 -*-
"""
作者：王振东
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
size = width, height = 600, 600  # 设置窗口大小参数
screen = pygame.display.set_mode(size)  # 生成窗口
speed = [1, 1]  # 设置速度列表
BLACK = 0, 0, 0  # RGB色域黑色
pygame.display.set_caption("pygame游戏之旅")  # 设置窗口名称
ball = pygame.image.load("PYG02-ball.gif")  # 导入图片，表示为surface对象
ballrect = ball.get_rect()  # 返回覆盖图像的矩形Rect对象
fps = 200
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
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
